#!/usr/bin/env python3
"""Rebuild deterministic topology/config artifacts; package with package.py afterwards."""
from pathlib import Path
import json, copy, uuid, html
P=Path(__file__).resolve().parent
ROOT=P.parent.parent
NS=uuid.UUID('c7725108-57d9-4e17-a213-bc5f32d23514')
def uid(s): return str(uuid.uuid5(NS,s))
def write(p,s):
 p=P/p; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s)
base=json.loads((ROOT/'new-gns3-labs/enarsi-bgp-peer-templates/project.gns3').read_text())
template=base['topology']['nodes'][0]
# router, port, router, port, area, subnet third octet
links=[(1,0,2,0,0,12),(1,1,3,0,0,13),(2,1,3,1,0,23),(2,2,4,0,10,24),(3,2,4,1,10,34),(1,2,5,0,0,15),(1,3,6,0,0,16),(6,1,7,0,20,67),(3,3,8,0,30,38)]
positions={1:(0,0),2:(-300,-220),3:(-300,220),4:(-650,0),5:(0,-300),6:(350,0),7:(650,0),8:(-300,480)}
areas={1:0,2:0,3:0,4:10,5:0,6:0,7:20,8:30}
interfaces={r:[] for r in range(1,9)}
for a,ap,b,bp,area,net in links:
 for r,port,peer,host in [(a,ap,b,1),(b,bp,a,2)]:
  interfaces[r].append(dict(name=f'Ethernet0/{port}',ip=f'10.255.{net}.{host}',mask='255.255.255.252',area=area,peer=peer))
for r in interfaces:
 interfaces[r].sort(key=lambda x:x['name'])
 interfaces[r].append(dict(name='Loopback0',ip=f'10.255.0.{r}',mask='255.255.255.255',area=areas[r]))
for k in list(range(6))+[8,250]: interfaces[4].append(dict(name=f'Loopback{100+k}',ip=f'10.10.{k}.1',mask='255.255.255.0',area=10))
for r,octet,values in [(5,20,[16,17,18,19,99]),(7,21,[32,33,34,35])]:
 for i,k in enumerate(values): interfaces[r].append(dict(name=f'Loopback{100+i}',ip=f'172.{octet}.{k}.1',mask='255.255.255.0',area=None))
interfaces[8].append(dict(name='Loopback100',ip='10.30.0.1',mask='255.255.255.0',area=30))
# Original domain becomes BLUE; RED shares addresses on separate physical ports.
for items in interfaces.values():
 for i in items: i['vrf']='BLUE'
redlinks=[(1,0,2,0,0,12),(1,1,5,0,0,15),(2,1,4,0,10,24)]
redrouters=[1,2,4,5]
for a,ap,b,bp,ar,net in redlinks:
 for r,port,peer,host in [(a,ap,b,1),(b,bp,a,2)]:
  interfaces[r].append(dict(name=f'Ethernet1/{port}',ip=f'10.255.{net}.{host}',mask='255.255.255.252',area=ar,peer=peer,vrf='RED'))
for r in redrouters:
 interfaces[r].append(dict(name='Loopback1000',ip=f'10.255.0.{r}',mask='255.255.255.255',area=10 if r==4 else 0,vrf='RED'))
for k in range(4):
 interfaces[4].append(dict(name=f'Loopback{1100+k}',ip=f'10.10.{k}.1',mask='255.255.255.0',area=10,vrf='RED'))
 interfaces[5].append(dict(name=f'Loopback{1100+k}',ip=f'172.20.{16+k}.1',mask='255.255.255.0',area=None,vrf='RED'))
interfaces[5].append(dict(name='Loopback1900',ip='198.51.100.5',mask='255.255.255.255',area=0,vrf='RED'))
for r in [1,5]:
 interfaces[r].append(dict(name='Loopback900',ip=f'198.18.0.{r}',mask='255.255.255.255',area=0,vrf='BLUE',startup_vrf='global'))
def config(r,stage='final'):
 final=stage!='startup'
 s=['! OSPFv2 VRF-Lite Summarization and Authentication Lab',f'hostname R{r}','no ip domain-lookup','ip cef','!']
 for vrf,num in [('BLUE',10)]+([('RED',20)] if r in redrouters else []):
  s += ['ip vrf '+vrf,f' rd 65000:{num}','!']
 if stage=='sha' and r in [6,7]:
  s+=['key chain OSPF20',' key 20','  key-string NssaSHA256-Lab','  cryptographic-algorithm hmac-sha-256','!']
 for i in interfaces[r]:
  vrf=i['vrf'] if final else i.get('startup_vrf',i['vrf'])
  pid=10 if i['vrf']=='BLUE' else 20
  s+=['interface '+i['name'],' description '+i['vrf']+' '+(f'TO-R{i["peer"]} AREA {i["area"]}' if 'peer' in i else 'LAB PREFIX')]
  if vrf!='global': s+=[' ip vrf forwarding '+vrf]
  s+=[' ip address '+i['ip']+' '+i['mask']]
  if final and i['area'] is not None:
   s+=[f' ip ospf {pid} area {i["area"]}']
   if i['name'].startswith('Ethernet') or i['mask']!='255.255.255.255': s+=[' ip ospf network point-to-point']
   if 'peer' in i:
    s+=[' ip ospf cost 10']
    if i['vrf']=='RED':
     s+=[' ip ospf message-digest-key 20 md5 RedCore20'] if i['area']==0 else [' ip ospf authentication-key RedPlain']
    elif i['area']==0: s+=[' ip ospf message-digest-key 20 md5 CoreNew20']
    elif i['area']==10: s+=[' ip ospf authentication-key A10plain']
    elif i['area']==20:
     s+=[' ip ospf authentication key-chain OSPF20'] if stage=='sha' else [' ip ospf authentication message-digest',' ip ospf message-digest-key 7 md5 NssaKey7']
    elif i['area']==30: s+=[' ip ospf authentication null']
  s+=[' no shutdown','!']
 if final and r in [5,7]:
  vals=[16,17,18,19,99] if r==5 else [32,33,34,35]
  octet=20 if r==5 else 21
  for seq,k in enumerate(vals,1): s+=[f'ip prefix-list EXT-R{r} seq {seq*10} permit 172.{octet}.{k}.0/24']
  s+=['!',f'route-map CONNECTED-R{r} permit 10',f' match ip address prefix-list EXT-R{r}','!']
 if final:
  s+=['router ospf 10 vrf BLUE',' capability vrf-lite',f' router-id {r}.{r}.{r}.{r}',' passive-interface default']
  s += [' no passive-interface '+i['name'] for i in interfaces[r] if 'peer' in i and i['vrf']=='BLUE']
  if r in [1,2,3,5,6]: s+=[' area 0 authentication message-digest']
  if r in [2,3,4]: s+=[' area 10 authentication']
  if r in [2,3]:
   cost=50 if r==2 else 80
   s += [f' area 10 range 10.10.0.0 255.255.252.0 cost {cost}',f' area 10 range 10.10.4.0 255.255.254.0 cost {cost}',' area 10 range 10.10.250.0 255.255.255.0 not-advertise']
  if r in [3,8]: s+=[' area 30 authentication message-digest',' area 30 stub'+(' no-summary' if r==3 else '')]
  if r==5: s+=[' summary-address 172.20.16.0 255.255.252.0 tag 505',' summary-address 172.20.99.0 255.255.255.0 not-advertise',' redistribute connected subnets metric 40 metric-type 1 route-map CONNECTED-R5']
  if r==6:
   s+=[' area 20 nssa default-information-originate']
   if stage!='nssa-asbr': s+=[' summary-address 172.21.32.0 255.255.252.0 tag 707']
  if r==7:
   s+=[' area 20 nssa',' redistribute connected subnets metric 30 metric-type 2 tag 707 route-map CONNECTED-R7']
   if stage=='nssa-asbr': s+=[' summary-address 172.21.32.0 255.255.252.0 tag 707']
  s+=['!']
 if final and r in redrouters:
  if r==5:
   for k in range(4): s += [f'ip prefix-list RED-EXT-R5 seq {(k+1)*10} permit 172.20.{16+k}.0/24']
   s += ['route-map RED-CONNECTED-R5 permit 10',' match ip address prefix-list RED-EXT-R5','!']
  s += ['router ospf 20 vrf RED',' capability vrf-lite',f' router-id 20.20.20.{r}',' passive-interface default']
  s += [' no passive-interface '+i['name'] for i in interfaces[r] if 'peer' in i and i['vrf']=='RED']
  if r in [1,2,5]: s += [' area 0 authentication message-digest']
  if r in [2,4]: s += [' area 10 authentication']
  if r==2: s += [' area 10 range 10.10.0.0 255.255.252.0 cost 70']
  if r==5: s += [' redistribute connected subnets metric 60 metric-type 2 route-map RED-CONNECTED-R5',' summary-address 172.20.16.0 255.255.252.0 tag 1505']
  s+=['!']
 s+=['line con 0',' logging synchronous',' exec-timeout 0 0','!','end','']
 # Establish VRF-bound processes before interface-level activation on clean import.
 if final:
  routing=[];other=[];idx=0
  while idx<len(s):
   if s[idx].startswith('router ospf '):
    routing.append(s[idx]);idx+=1
    while idx<len(s) and s[idx].startswith(' '):
     routing.append(s[idx]);idx+=1
    routing.append('!')
   else:
    other.append(s[idx]);idx+=1
  first=next(j for j,line in enumerate(other) if line.startswith('interface '))
  s=other[:first]+routing+other[first:]
 return '\n'.join(s)
nodes=[]
for r,(x,y) in positions.items():
 n=copy.deepcopy(template); n.update(name=f'R{r}',node_id=uid(f'R{r}'),x=x,y=y,console=None);n['label'].update(text=f'R{r}',x=20,y=-25); n['properties']['application_id']=r; nodes.append(n)
 start=config(r,'startup');write(Path('startup-configs')/f'R{r}.cfg',start);write(Path('project-files/iou')/n['node_id']/'startup-config.cfg',start)
 write(Path('final-configs')/f'R{r}.cfg',config(r))
 for stage,folder in [('nssa-asbr','checkpoints/nssa-asbr-final-configs'),('sha','extensions/hmac-sha256/final-configs')]: write(Path(folder)/f'R{r}.cfg',config(r,stage))
glinks=[]
for vrf,adapter,tenantlinks in [('BLUE',0,links),('RED',1,redlinks)]:
 for a,ap,b,bp,area,net in tenantlinks:
  ends=[]
  for r,p in [(a,ap),(b,bp)]:
   ends.append(dict(node_id=uid(f'R{r}'),adapter_number=adapter,port_number=p,label=dict(text=f'e{adapter}/{p}',rotation=0,style=template['label']['style'],x=0,y=0)))
  glinks.append(dict(link_id=uid(f'link-{vrf}-{a}-{b}'),nodes=ends,suspend=False,filters={}))
def textsvg(text,w=360): return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="26"><text x="4" y="19" font-family="Arial" font-size="14" fill="#24354b">{html.escape(text)}</text></svg>'
drawings=[]
for name,x,y in [('BLUE AREA 0 | MD5',80,-130),('BLUE AREA 10 | dual ABRs | simple authentication',-720,-130),('BLUE AREA 20 | NSSA | interface MD5',410,90),('BLUE AREA 30 | totally stubby | null exception',-460,570),('R5 | external origin',-50,-350),('R7 | NSSA external origin',560,-60),('RED: R4 -- R2 -- R1 -- R5 | Ethernet1/x',-500,-440)]:
 drawings.append(dict(drawing_id=uid(name),x=x,y=y,z=0,rotation=0,locked=False,svg=textsvg(name,430)))
base.update(name='ENARSI OSPFv2 VRF-Lite Summarization and Authentication',project_id=uid('project-vrf-v2'),scene_width=2000,scene_height=1500)
base['topology']=dict(computes=[],nodes=nodes,links=glinks,drawings=drawings)
write(Path('project.gns3'),json.dumps(base,indent=2)+'\n')
write(Path('addressing.json'),json.dumps({f'R{r}':v for r,v in interfaces.items()},indent=2)+'\n')
rows=['# Addressing and topology','', 'Eight routers, twelve physical links: nine BLUE and three RED. No VLAN trunks, MPLS or route leaking. All interfaces are addressed in the starter. BLUE/RED VRFs and bindings are preprovisioned except Loopback900 on R1/R5, which starts global for Activity V1. OSPF is not configured.','', 'BLUE uses process 10 and router IDs r.r.r.r; RED uses process 20 and IDs 20.20.20.r. RDs are 65000:10 (BLUE), 65000:20 (RED). IP addresses deliberately overlap across VRFs.','', '| VRF | Link | First interface (.1) | Second interface (.2) | Subnet | Area |','|---|---|---|---|---|---|']
for vrf,adapter,tenantlinks in [('BLUE',0,links),('RED',1,redlinks)]:
 for a,ap,b,bp,area,net in tenantlinks: rows.append(f'| {vrf} | R{a}–R{b} | R{a} Ethernet{adapter}/{ap} | R{b} Ethernet{adapter}/{bp} | 10.255.{net}.0/30 | {area} |')
rows+=['','| Router | Interface | Address | Startup → final VRF | Target area / role |','|---|---|---|---|---|']
for r,ints in interfaces.items():
 for i in ints:
  if 'peer' not in i:
   rows.append(f'| R{r} | {i["name"]} | {i["ip"]}/{32 if i["mask"].endswith("255") else 24} | {i.get("startup_vrf",i["vrf"])} → {i["vrf"]} | {i["area"] if i["area"] is not None else "Redistribution only"} |')
rows+=['','```mermaid','graph LR',' subgraph BLUE',' B5[R5] ---|area 0| B1[R1]',' B1 ---|area 0| B2[R2]',' B1 ---|area 0| B3[R3]',' B2 ---|area 0| B3',' B2 ---|area 10| B4[R4]',' B3 ---|area 10| B4',' B1 ---|area 0| B6[R6]',' B6 ---|area 20 NSSA| B7[R7]',' B3 ---|area 30 stub| B8[R8]',' end',' subgraph RED',' R4 ---|area 10| R2',' R2 ---|area 0| R1',' R1 ---|area 0| R5',' end','```','', 'The two diagrams show logical VRF domains on the same physical routers, not sixteen devices.']
write(Path('TOPOLOGY.md'),'\n'.join(rows)+'\n')
# Separate panels keep parallel links and duplicate addresses unambiguous.
s=['<svg xmlns="http://www.w3.org/2000/svg" width="1500" height="1320" viewBox="0 0 1500 1320">','<rect width="1500" height="1320" fill="#f6f8fb"/>','<text x="45" y="45" font-family="Arial" font-size="25" fill="#18334d">OSPFv2 VRF-Lite • BLUE and RED on the same eight routers</text>']
xy={r:(x+750,y+400) for r,(x,y) in positions.items()}
colors={0:'#466b8b',10:'#b66a11',20:'#087f72',30:'#7957a4'}
for a,ap,b,bp,area,net in links:
 x1,y1=xy[a];x2,y2=xy[b];mx,my=(x1+x2)/2,(y1+y2)/2
 s += [f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{colors[area]}" stroke-width="3"/>',f'<rect x="{mx-90}" y="{my-22}" width="180" height="43" rx="5" fill="#f6f8fb"/>',f'<text x="{mx}" y="{my-5}" text-anchor="middle" font-family="Arial" font-size="13">BLUE 10.255.{net}.0/30 · A{area}</text>',f'<text x="{mx}" y="{my+13}" text-anchor="middle" font-family="Arial" font-size="11">R{a} e0/{ap} (.1) ↔ R{b} e0/{bp} (.2)</text>']
for r,(x,y) in xy.items():
 s += [f'<circle cx="{x}" cy="{y}" r="29" fill="#18334d"/>',f'<text x="{x}" y="{y+6}" text-anchor="middle" font-family="Arial" font-size="19" fill="white">R{r}</text>']
s+=['<text x="45" y="975" font-family="Arial" font-size="20" fill="#a52c3a">RED: independent OSPF 20, overlapping addresses, no leaks to BLUE/global</text>']
rx={4:120,2:520,1:920,5:1320}
for a,ap,b,bp,area,net in redlinks:
 mx=(rx[a]+rx[b])/2
 s += [f'<line x1="{rx[a]}" y1="1080" x2="{rx[b]}" y2="1080" stroke="#a52c3a" stroke-width="3"/>',f'<text x="{mx}" y="1040" text-anchor="middle" font-family="Arial" font-size="14">10.255.{net}.0/30 · area {area}</text>',f'<text x="{mx}" y="1125" text-anchor="middle" font-family="Arial" font-size="13">R{a} e1/{ap} (.1) ↔ R{b} e1/{bp} (.2)</text>']
for r,x in rx.items():
 s += [f'<circle cx="{x}" cy="1080" r="29" fill="#a52c3a"/>',f'<text x="{x}" y="1086" text-anchor="middle" font-family="Arial" font-size="19" fill="white">R{r}</text>']
s+=['<text x="45" y="1210" font-family="Arial" font-size="15">BLUE: original dual-ABR campus, external services, NSSA and stub branch.</text>','<text x="45" y="1240" font-family="Arial" font-size="15">RED: duplicate campus/service addresses; unique 198.51.100.5/32 isolation probe on R5.</text>','<text x="45" y="1270" font-family="Arial" font-size="15">R1/R5 Loopback900: pre-addressed globally, migrate to BLUE during V1.</text>','</svg>']
write(Path('topology.svg'),'\n'.join(s))
print('Built 8 routers, 12 links, BLUE/RED VRFs and all four configuration sets.')
