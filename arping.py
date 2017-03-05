import os,subprocess,re
from glob import glob
ifcfglist=[]
iplist=[]
ifcfglist=glob("/etc/sysconfig/network-scripts/ifcfg-eth*")
ip=re.compile(r'.*IPADDR0=(?P<ip>\S+).*')

for i in ifcfglist:
    file=open(i,"r")
    str=file.read()
    iplist.append(ip.findall(str))

for i in iplist:
    if i:
        subprocess.call('arping -c 1 -I eth0 -s %d 192.168.0.1' %int(i), shell=True)

