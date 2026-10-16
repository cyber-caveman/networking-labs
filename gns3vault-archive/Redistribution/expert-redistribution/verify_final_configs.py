"""Finite steady-state policy model; NOT an IOS, DUAL, RIP timer or NBMA emulator."""
from pathlib import Path
import re, ipaddress, itertools
B=Path(__file__).resolve().parent
C={p.stem:p.read_text() for p in (B/'final-configs').glob('*.cfg')}
R=list(C); interfaces={}; processes={}; lists={}; maps={}
for r,t in C.items():
 interfaces[r]={}; processes[r]={}; lists[r]={}; maps[r]={}
 for name,body in re.findall(r'^interface (\S+)\n((?: .+\n)*)',t,re.M):
  m=re.search(r' ip address (\S+) (\S+)',body)
  if m: interfaces[r][name]=str(ipaddress.ip_network('/'.join(m.groups()),strict=False))
 for name,body in re.findall(r'^router (.+)\n((?: .+\n)*)',t,re.M): processes[r][name]=body
 for name,p in re.findall(r'^ip prefix-list (\S+) seq \d+ permit (\S+)',t,re.M): lists[r].setdefault(name,set()).add(p)
 for name,act,seq,body in re.findall(r'^route-map (\S+) (permit|deny) (\d+)\n((?: .+\n)*)',t,re.M): maps[r].setdefault(name,[]).append((int(seq),act,body))
P=sorted(set(p for x in interfaces.values() for p in x.values()))
def membership(r,i,proto):
 p=ipaddress.ip_network(interfaces[r][i]); b=processes[r][proto]
 for line in b.splitlines():
  w=line.split()
  if w and w[0]=='network':
   if len(w)>2: net=ipaddress.IPv4Network((w[1],w[2]),strict=False)
   else:
    octet=int(w[1].split('.')[0]); net=ipaddress.ip_network(w[1]+'/'+str(8 if octet<128 else 16 if octet<192 else 24),strict=False)
   if p.network_address in net: return True
 return False

def policy(r,name,p,tag,iface):
 for _,act,b in sorted(maps[r][name]):
  m=re.search(r'match ip address prefix-list (\S+)',b)
  if m and p not in lists[r][m[1]]: continue
  m=re.search(r'match tag (\d+)',b)
  if m and tag!=int(m[1]): continue
  m=re.search(r'match interface (\S+)',b)
  if m and iface!=m[1]: continue
  if act=='deny': return None
  m=re.search(r'set tag (\d+)',b); tag=int(m[1]) if m else tag
  m=re.search(r'set metric (.+)',b)
  metric=list(map(int,m[1].split())) if m else None
  return tag,metric
 return None

def run(down=frozenset()):
 active={(r,i):p for r in R for i,p in interfaces[r].items() if (r,i) not in down}
 # Route tuple: distance, comparison metric, protocol, next hop, tag, origin interface.
 rib={(r,p):(0,0,'connected',None,0,i) for (r,i),p in active.items()}
 native=[]; graphs={}
 for proto in {x for r in R for x in processes[r]}:
  members=[(r,i,p) for (r,i),p in active.items() if proto in processes[r] and membership(r,i,proto)]
  graphs[proto]={r:{} for r in R}
  for r,i,p in members:
   native.append((r,p,proto,0,False,0,i))
   if i!='Loopback0':
    for s,j,q in members:
     if s!=r and q==p and j!='Loopback0': graphs[proto][r][s]=i
 for iteration in range(100):
  seeds=list(native)
  for r in R:
   for target,b in processes[r].items():
    for line in b.splitlines():
     if not line.startswith(' redistribute '): continue
     w=line.split(); source=w[1]+(' '+w[2] if w[1] in ['ospf','eigrp'] else '')
     rm=w[w.index('route-map')+1]
     for p in P:
      route=rib.get((r,p))
      if route is None: continue
      ad,cost,proto,nh,tag,iface=route
      if proto!=source and not (proto=='connected' and source in processes[r] and membership(r,iface,source)): continue
      val=policy(r,rm,p,tag,iface)
      if val is None: continue
      tag,metric=val
      cost=(10**7/metric[0]+metric[1]) if target.startswith('eigrp') else (metric[0] if target=='rip' else 20)
      seeds.append((r,p,target,cost,True,tag,iface))
  candidates={k:[v] for k,v in rib.items() if v[2]=='connected'}
  for origin,p,proto,cost,external,tag,iface in seeds:
   # Every domain in this lab is one shared segment / the full mesh FR segment.
   for r in graphs[proto][origin]:
    if proto.startswith('eigrp'):
     m=re.search(r'distribute-list route-map (\S+) in',processes[r][proto])
     if m and policy(r,m[1],p,tag,None) is None: continue
     ad=170 if external else 90; metric=cost+10
    elif proto=='rip':
     metric=cost+1
     if metric>=16: continue
     ad=120
     if r=='Amber': ad=120 if p in {'4.4.4.0/24','7.7.7.0/24','192.168.45.0/24'} else 175
    else: ad=180; metric=cost+64+(100000 if external else 0)
    candidates.setdefault((r,p),[]).append((ad,metric,proto,origin,tag,None))
  new={k:min(v,key=lambda x:(x[0],x[1],x[2],x[3] or '')) for k,v in candidates.items()}
  if new==rib: break
  rib=new
 else: raise AssertionError(('no steady state',down))
 # Check all forwarding chains for all available subnets; only physically isolated destinations may fail.
 def physical_reach(r,p):
  seen={r}; todo=[r]
  while todo:
   x=todo.pop()
   if p in [q for (s,i),q in active.items() if s==x]: return True
   for (s,i),q in active.items():
    if s!=x: continue
    for (z,j),v in active.items():
     if z not in seen and z!=s and v==q and not i.startswith('Loopback') and not j.startswith('Loopback'):
      seen.add(z); todo.append(z)
  return False
 checks=0
 for r,p in itertools.product(R,P):
  if not physical_reach(r,p): continue
  seen=[]; x=r
  while True:
   assert x not in seen,('forwarding loop',down,r,p,seen,x)
   seen.append(x); route=rib.get((x,p)); assert route,('missing route',down,r,p,x)
   if route[2]=='connected': break
   if not down and p!='192.168.234.0/24': assert route[2]!='ospf 234',('serial in healthy topology',r,p,seen,route)
   x=route[3]
  checks+=1
 return checks,iteration+1,rib
if __name__=='__main__':
 cases=[frozenset()]+[frozenset({(r,i)}) for r in R for i in interfaces[r] if i.startswith(('Ethernet','Serial'))]
 cases += [frozenset((r,i) for r in R for i,p in interfaces[r].items() if p==net) for net in ['192.168.123.0/24','192.168.35.0/24','192.168.45.0/24']]
 total=0
 for down in cases:
  n,it,rib=run(down); total+=n
  print('PASS',','.join(r+':'+i for r,i in down) or 'all links up',n,'reachable pairs',it,'iterations')
 print('TOTAL',total,'forwarding checks;',len(cases),'scenarios. Abstract analysis only, not live IOS validation.')
