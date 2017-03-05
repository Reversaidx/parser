import os,subprocess
from glob import glob
ifcfglist=[]
os.chdir('/etc/sysconfig/network-scripts')
ifcfglist=glob("ifcfg-eth*")
print (ifcfglist)
