import os,subprocess
from glob import glob
ifcfglist=[]
iplist=[]
os.chdir("/etc/sysconfig/network-scripts/")
ifcfglist=glob("ifcfg-eth*")
for i in ifcfglist:
    int=i.split("-")
    subprocess.call("ifup %s" %int[1], shell=True)