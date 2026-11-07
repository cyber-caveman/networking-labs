#!/usr/bin/env python3
"""Independent artifact checks and bounded routing-policy model; not an IOS emulator."""
from pathlib import Path
import json, re, ipaddress as ip, zipfile, heapq
import xml.etree.ElementTree as ET
P=Path(__file__).resolve().parent
count=0
def check(ok,msg):
 global count
 count+=1
 if not ok: raise AssertionError(msg)
def parse(text):
 blocks={}; cur=None
 for line in text.splitlines():
  if not line or line.startswith('!'): continue
  if not line.startswith(' '):
   cur=line; blocks[cur]=[]
  elif cur: blocks[cur].append(line.strip())
 return blocks
def addr(c):
 return {k:next(x for x in v if x.startswith('ip address ')) for k,v in c.items() if k.startswith('interface ')}
def ospf(c,vrf='BLUE'): return c[f'router ospf {10 if vrf=="BLUE" else 20} vrf {vrf}']
def binding(cmds): return next((x.split()[-1] for x in cmds if x.startswith('ip vrf forwarding ')),'global')
def area(cmds): return int(next(x for x in cmds if re.match(r'ip ospf (10|20) area ',x)).split()[-1])
def net(cmd):
 x=cmd.split();return ip.ip_interface(x[2]+'/'+x[3])
def auth(c,cmds):
 a=area(cmds)
 override=next((x.removeprefix('ip ospf authentication') .strip() for x in cmds if x.startswith('ip ospf authentication') and not x.startswith('ip ospf authentication-key')),None)
 inherited=next((x.removeprefix(f'area {a} authentication').strip() for x in ospf(c,binding(cmds)) if x.startswith(f'area {a} authentication')),None)
 method=override if override is not None else inherited
 if method is None or method=='null':return ('null',)
 if method=='':return ('simple',next(x.split()[-1] for x in cmds if x.startswith('ip ospf authentication-key ')))
 if method=='message-digest':return ('md5',tuple(sorted(x.removeprefix('ip ospf message-digest-key ') for x in cmds if x.startswith('ip ospf message-digest-key '))))
 if method.startswith('key-chain '):
  key=c['key chain '+method.split()[-1]]
  return ('sha',tuple(key))
 raise AssertionError(method)
project=json.loads((P/'project.gns3').read_text());nodes=project['topology']['nodes'];links=project['topology']['links']
check(project['revision']==9 and project['version']=='2.2.0','known-working format')
check(len(nodes)==8 and len(links)==12,'topology dimensions')
check(len({n['node_id'] for n in nodes})==8,'UUID uniqueness')
check(len({n['properties']['application_id'] for n in nodes})==8,'IOU ID uniqueness')
check(len({l['link_id'] for l in links})==12,'link UUID uniqueness')
byid={n['node_id']:n['name'] for n in nodes}
sets={folder:{f'R{r}':parse((P/folder/f'R{r}.cfg').read_text()) for r in range(1,9)} for folder in ['startup-configs','final-configs','checkpoints/nssa-asbr-final-configs','extensions/hmac-sha256/final-configs']}
final=sets['final-configs']; metadata=json.loads((P/'addressing.json').read_text())
for n in nodes:
 name=n['name'];props=n['properties'];r=int(name[1:])
 check(n['node_type']=='iou' and n['compute_id']=='local' and n['console'] is None,'IOU console/compute')
 check(n['console_type']=='telnet' and not n['console_auto_start'],'console properties')
 check(n['template_id']=='b3b10b90-adfb-43f8-b289-b68bcf322ad8','template')
 check((props['ethernet_adapters'],props['serial_adapters'],props['ram'],props['nvram'])==(4,4,768,512),'resources')
 check(props['path']=='x86_64_crb_linux-adventerprisek9-ms.bin' and props['md5sum']=='4a2fce8de21d1831fbceffd155e41ae7','image')
 start=(P/'startup-configs'/f'{name}.cfg').read_text()
 check(start==(P/'project-files/iou'/n['node_id']/'startup-config.cfg').read_text(),'startup copy')
 check(not any(x in start for x in ['router ospf','ip ospf','ip route ','redistribute','key chain']),'clean starting state')
 for folder,cs in sets.items():
  c=cs[name]
  check(addr(c)==addr(sets['startup-configs'][name]),'addresses preserved '+folder+name)
  check(set(addr(c))=={'interface '+i['name'] for i in metadata[name]},'interface inventory')
  check(all('no shutdown' in c[k] for k in addr(c)),'interfaces enabled')
  for i in metadata[name]:
   cmds=c['interface '+i['name']]
   expected_vrf=i.get('startup_vrf',i['vrf']) if folder=='startup-configs' else i['vrf']
   check(binding(cmds)==expected_vrf,'interface tenant '+name+i['name'])
   if expected_vrf!='global':
    check(cmds.index('ip vrf forwarding '+expected_vrf)<next(j for j,x in enumerate(cmds) if x.startswith('ip address ')),'binding precedes address')
  check(c['ip vrf BLUE']==['rd 65000:10'],'BLUE RD')
  if name in ['R1','R2','R4','R5']:check(c['ip vrf RED']==['rd 65000:20'],'RED RD')
  check('ip vrf STAGING' not in c,'temporary VRF absent')
  if folder=='startup-configs':continue
  o=ospf(c)
  check(f'router-id {r}.{r}.{r}.{r}' in o and 'passive-interface default' in o,'RID/passive default')
  check('capability vrf-lite' in o,'BLUE PE checks suppressed')
  check(not any(x.startswith('network ') for x in o),'interface activation only')
  check(not any(k.startswith('ip route ') for k in c),'no static shortcuts')
  for i in metadata[name]:
   cmds=c['interface '+i['name']]
   check(f'ip address {i["ip"]} {i["mask"]}' in cmds,'address metadata')
   if i['area'] is None:
    check(not any(x.startswith('ip ospf') for x in cmds),'external interface not OSPF activated')
   else:
    check(area(cmds)==i['area'],'correct area')
    if i['mask']!='255.255.255.255':check('ip ospf network point-to-point' in cmds,'preserve /24 and p2p Ethernet')
   io=ospf(c,i['vrf'])
   check(('no passive-interface '+i['name'] in io)==('peer' in i),'hello scope')
   if i['area'] is not None:check(f'ip ospf {10 if i["vrf"]=="BLUE" else 20} area {i["area"]}' in cmds,'process bound to tenant')
redgraph={r:{} for r in ['R1','R2','R4','R5']}
used=set();graph={f'R{r}':{} for r in range(1,9)};core={r:{} for r in graph};linkinfo=[]
for link in links:
 ends=[]
 for e in link['nodes']:
  key=(e['node_id'],e['adapter_number'],e['port_number'])
  check(key not in used,'unique physical endpoint');used.add(key)
  check(e['adapter_number'] in [0,1] and 0<=e['port_number']<4,'valid endpoint')
  name=byid[e['node_id']];intf=f'interface Ethernet{e["adapter_number"]}/{e["port_number"]}'
  cmds=final[name][intf];address=net(next(x for x in cmds if x.startswith('ip address ')))
  ends.append((name,intf,address,area(cmds)))
 (a,ai,aa,ar),(b,bi,ba,br)=ends
 check(aa.network==ba.network and aa.ip!=ba.ip,'subnet peer match');check(ar==br,'area peer match')
 vrf=binding(final[a][ai]);check(vrf==binding(final[b][bi]),'link same tenant')
 g=graph if vrf=='BLUE' else redgraph
 g[a][b]=g[b][a]=10
 if ar==0 and vrf=='BLUE':core[a][b]=core[b][a]=10
 linkinfo.append((a,ai,b,bi,ar))
 for folder,cs in sets.items():
  if folder=='startup-configs':continue
  ca,cb=cs[a],cs[b];effective=auth(ca,ca[ai]);check(effective==auth(cb,cb[bi]),'authentication peer match '+folder)
  expected={0:('md5',('20 md5 CoreNew20',)),10:('simple','A10plain'),20:('md5',('7 md5 NssaKey7',)),30:('null',)}[ar]
  if vrf=='RED':expected=('md5',('20 md5 RedCore20',)) if ar==0 else ('simple','RedPlain')
  if folder.startswith('extensions') and ar==20:
   check(effective==('sha',('key 20','key-string NssaSHA256-Lab','cryptographic-algorithm hmac-sha-256')),'SHA SA')
  else:check(effective==expected,'effective auth policy')
  for c,i in [(ca,ai),(cb,bi)]:check('ip ospf cost 10' in c[i],'link cost')
check([len(graph[f'R{r}']) for r in range(1,9)]==[4,3,4,2,1,2,1,1],'neighbor counts')
def distance(g,a,b):
 q=[(0,a)];seen=set()
 while q:
  d,n=heapq.heappop(q)
  if n==b:return d
  if n in seen:continue
  seen.add(n)
  for dest,w in g[n].items():
   if dest not in seen:heapq.heappush(q,(d+w,dest))
 return float('inf')
check(all(distance(graph,a,b)<float('inf') for a in graph for b in graph),'physical reachability both directions')
# Parse exact area-range policy and mathematically evaluate component coverage.
def ranges(c):
 return [(ip.ip_network(x.split()[3]+'/'+x.split()[4]),x.split()[5:]) for x in ospf(c) if x.startswith('area 10 range ')]
campus={ip.ip_network(f'10.10.{i}.0/24') for i in range(6)}
expected_ranges={ip.ip_network('10.10.0.0/22'),ip.ip_network('10.10.4.0/23')}
for r,cost in [('R2',50),('R3',80)]:
 rr=ranges(final[r]);adv={n for n,opts in rr if 'not-advertise' not in opts}
 check(adv==expected_ranges,'minimum exact cover')
 check({s for n in adv for s in n.subnets(new_prefix=24)}==campus,'no unassigned subnet covered')
 check(all(opts==['cost',str(cost)] for n,opts in rr if n in adv),'summary cost')
 check((ip.ip_network('10.10.250.0/24'),['not-advertise']) in rr,'suppression')
 check(not any(ip.ip_network('10.10.8.0/24').subnet_of(n) for n in adv),'independent .8')
check(min((distance(core,'R1',r)+cost,r) for r,cost in [('R2',50),('R3',80)])==(60,'R2'),'normal preferred summary')
check(distance(core,'R1','R3')+80==90,'R2 campus link failure metric')
check(distance(core,'R1','R2')+50==60,'R3 campus link failure metric')
for summary in expected_ranges:
 contributors={n for n in campus if n.subnet_of(summary)}
 check(len(contributors)>1,'multiple contributors')
 check(bool(contributors-{sorted(contributors)[0]}),'one component failure retains summary')
 check(not contributors-contributors,'all components failure withdraws summary')
# Exact redistribution allowlists; implicit deny prevents infrastructure leakage.
for r,octet,values,metric,typ in [('R5',20,[16,17,18,19,99],40,1),('R7',21,[32,33,34,35],30,2)]:
 c=final[r]
 prefixes={ip.ip_network(k.split()[-1]) for k in c if k.startswith('ip prefix-list EXT-'+r+' ')}
 check(prefixes=={ip.ip_network(f'172.{octet}.{i}.0/24') for i in values},'exact redistribution scope')
 connected={net(x).network for k,x in addr(c).items() if binding(c[k])=='BLUE'}
 check(prefixes<=connected,'redistributed origins exist')
 check(c['route-map CONNECTED-'+r+' permit 10']==['match ip address prefix-list EXT-'+r],'selector route-map')
 redis=[x for x in ospf(c) if x.startswith('redistribute ')]
 expected=f'redistribute connected subnets metric {metric} metric-type {typ}'+(' tag 707' if r=='R7' else '')+' route-map CONNECTED-'+r
 check(redis==[expected],'external type/metric/selector/tag')
check('summary-address 172.20.16.0 255.255.252.0 tag 505' in ospf(final['R5']),'E1 aggregate/tag')
check('summary-address 172.20.99.0 255.255.255.0 not-advertise' in ospf(final['R5']),'external suppression')
check(distance(graph,'R1','R5')+40==50,'E1 cost model')
for folder,cs in sets.items():
 if folder=='startup-configs':continue
 check('area 20 nssa default-information-originate' in ospf(cs['R6']),'NSSA default origin')
 check('area 20 nssa' in ospf(cs['R7']),'NSSA agreement')
 check('area 30 stub no-summary' in ospf(cs['R3']) and 'area 30 stub' in ospf(cs['R8']),'stub agreement/default')
 owner='R7' if folder.startswith('checkpoints') else 'R6'
 for r in ['R6','R7']:
  check(('summary-address 172.21.32.0 255.255.252.0 tag 707' in ospf(cs[r]))==(r==owner),'NSSA stage placement')
 check(not any(x.startswith('redistribute ') for x in ospf(cs['R6'])),'ABR translates, does not redistribute')
 # Internal forwarding-address candidates remain routable out of area 20.
 check('ip ospf 10 area 20' in cs['R7']['interface Loopback0'],'FA loopback advertised')
 check(not any(x.startswith('area 20 range ') for x in ospf(cs['R6'])),'no internal FA suppression')
for r in final:
 check(not any('discard-route' in x for x in ospf(final[r])),'default discard protection')
 # Compare entire parsed variants after removing only the intended changes.
 for folder in ['checkpoints/nssa-asbr-final-configs','extensions/hmac-sha256/final-configs']:
  variant=sets[folder][r]
  def normalize(c):
   result={}
   for heading,commands in c.items():
    if heading=='key chain OSPF20':continue
    result[heading]=[x for x in commands if not (
     x=='summary-address 172.21.32.0 255.255.252.0 tag 707' or
     (r in ['R6','R7'] and heading==('interface Ethernet0/1' if r=='R6' else 'interface Ethernet0/0') and
      (x.startswith('ip ospf authentication ') or x.startswith('ip ospf message-digest-key '))))]
   return result
  check(normalize(final[r])==normalize(variant),'variant preserves all other configuration '+folder+r)
# Model the specific external visibility and next-hop exit requirements (not full SPF).
external={ip.ip_network('172.20.16.0/22'),ip.ip_network('172.21.32.0/22')}
check(all(ip.ip_network(f'172.20.{i}.0/24').subnet_of(next(n for n in external if str(n).startswith('172.20'))) for i in range(16,20)),'E1 exact components')
check(all(ip.ip_network(f'172.21.{i}.0/24').subnet_of(next(n for n in external if str(n).startswith('172.21'))) for i in range(32,36)),'NSSA exact components')
for aggregate in external:
 components=set(aggregate.subnets(new_prefix=24))
 check(len(components)==4 and bool(components-{min(components)}),'external partial withdrawal retains aggregate')
 check(not components-components,'external complete withdrawal removes aggregate')
 check(not ip.ip_network('172.20.99.0/24').subnet_of(aggregate),'suppressed prefix cannot sustain service aggregate')
for source in ['R4','R8']:
 for origin in ['R5','R7']:
  check(distance(graph,source,origin)<float('inf') and distance(graph,origin,source)<float('inf'),'service/return physical paths')
check(graph['R7']=={'R6':10} and graph['R8']=={'R3':10},'single exit for NSSA/stub defaults')
# VRF-specific policy checks and router/VRF graph separation.
check([len(redgraph[r]) for r in ['R1','R2','R4','R5']]==[2,2,1,1],'RED adjacency counts')
check(all(distance(redgraph,a,b)<float('inf') for a in redgraph for b in redgraph),'RED connectivity')
for folder,cs in sets.items():
 for r,c in cs.items():
  expected_processes=set() if folder=='startup-configs' else {'router ospf 10 vrf BLUE'}|({'router ospf 20 vrf RED'} if r in redgraph else set())
  check({k for k in c if k.startswith('router ospf ')}==expected_processes,'only intended VRF-bound processes')
  check(not any(k.startswith(('router bgp','ip route ','ip route vrf ','mpls ')) for k in c),'no alternate route leaking')
  check(not any(x.startswith(('route-target','ip policy','import ','export ')) for v in c.values() for x in v),'no import/export/PBR')
  scoped={}
  for k,x in addr(c).items():
   key=(binding(c[k]),net(x).ip)
   check(key not in scoped,'unique IP within router/VRF');scoped[key]=k
  if folder=='startup-configs':continue
  check(all(binding(c[k])!='global' for k in addr(c)),'no final addressed global interfaces')
  if r in redgraph:
   ro=ospf(c,'RED')
   check(f'router-id 20.20.20.{r[1:]}' in ro and 'capability vrf-lite' in ro,'RED RID and PE checks')
   check('passive-interface default' in ro and not any(x.startswith('network ') for x in ro),'RED passive/interface activation')
   check(not any(x.startswith('redistribute ') for x in ro) or r=='R5','RED ASBR only R5')
   expected_summary=['area 10 range 10.10.0.0 255.255.252.0 cost 70'] if r=='R2' else []
   check([x for x in ro if x.startswith('area 10 range ')]==expected_summary,'RED summary only at its ABR')
  if r=='R5':
   ro=ospf(c,'RED')
   prefixes={ip.ip_network(k.split()[-1]) for k in c if k.startswith('ip prefix-list RED-EXT-R5 ')}
   check(prefixes=={ip.ip_network(f'172.20.{i}.0/24') for i in range(16,20)},'RED exact redistribution selector')
   check(c['route-map RED-CONNECTED-R5 permit 10']==['match ip address prefix-list RED-EXT-R5'],'RED map')
   check('redistribute connected subnets metric 60 metric-type 2 route-map RED-CONNECTED-R5' in ro,'RED E2 metric/selector')
   check('summary-address 172.20.16.0 255.255.252.0 tag 1505' in ro,'RED external tag')
   connected={net(x).network for k,x in addr(c).items() if binding(c[k])=='RED'}
   check(prefixes<=connected,'RED contributors belong to RED')
   check(binding(c['interface Loopback1900'])=='RED' and 'ip ospf 20 area 0' in c['interface Loopback1900'],'unique RED marker')
check(distance(redgraph,'R1','R2')+70==80,'RED campus metric 80 versus BLUE 60')
# Model transport edges as (router, VRF), with no implicit cross-VRF edge.
scoped_graph={(r,v):{} for v,g in [('BLUE',graph),('RED',redgraph)] for r in g}
for v,g in [('BLUE',graph),('RED',redgraph)]:
 for r,peers in g.items():
  scoped_graph[(r,v)]={(peer,v):w for peer,w in peers.items()}
check(distance(scoped_graph,('R1','BLUE'),('R5','RED'))==float('inf'),'no modeled BLUE-to-RED path')
check(distance(scoped_graph,('R1','RED'),('R5','BLUE'))==float('inf'),'no modeled RED-to-BLUE path')
failed={r:dict(peers) for r,peers in redgraph.items()};del failed['R1']['R5'];del failed['R5']['R1']
check(distance(failed,'R4','R5')==float('inf') and distance(graph,'R4','R5')<float('inf'),'RED-only failure independence')
# Confirm original lab behavior/configuration is preserved within BLUE.
contract=json.loads((P/'blue-baseline-contract.json').read_text())
for folder,routers in contract.items():
 for r,original in routers.items():
  actual=sets[folder][r]
  for heading,commands in original.items():
   current_heading='router ospf 10 vrf BLUE' if heading=='router ospf 10' else heading
   got=actual[current_heading]
   def normalize(v):return [x for x in v if not x.startswith(('description ','ip vrf forwarding ')) and x!='capability vrf-lite']
   check(normalize(commands)==normalize(got),'original BLUE functional config preserved '+folder+r+heading)

for d in project['topology']['drawings']:ET.fromstring(d['svg'])
ET.parse(P/'topology.svg')
check(len(list((P/'faults').glob('*.cfg')))==8,'eight fault tickets')
archive=P/'ENARSI OSPFv2 Summarization and Authentication IOU.gns3project'
with zipfile.ZipFile(archive) as z:
 check(z.testzip() is None,'archive CRC')
 expected={str(f.relative_to(P)) for f in P.rglob('*') if f.is_file() and f.suffix!='.gns3project' and '__pycache__' not in f.parts}
 check(set(z.namelist())==expected,'archive manifest')
 for name in expected:check(z.read(name)==(P/name).read_bytes(),'archive equality '+name)
print(f'PASS: {count} static assertions across 8 routers, 12 links and 4 config sets.')
print('PASS: peer addressing/authentication; exact prefix covers; policies, stage placement and bounded cost/failure models.')
print('NOT RUN: GNS3 import, IOU boot/CLI parsing, actual LSDB/RIB/FIB convergence, key rollover or packet forwarding.')
