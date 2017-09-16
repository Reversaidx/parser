#!/usr/bin/python
import subprocess
from glob import glob
import time,os,shutil
date=time.strftime("%d.%m.%Y")
subprocess.call('mysqldump -uroot -p{} wiki>/tmp/wiki%s.sql'%date,shell=True)

if os.path.exists('/tmp/wiki%s.sql' %date):
    print("dump success ")
else:
    print ("krivo")
    exit(1)

os.chdir("/tmp")
subprocess.call('tar cvfz strace.tar.gz%s /var/www/strace.pw' %date, shell=True)

if os.path.exists('/tmp/strace.tar.gz%s' %date):
    print("Tar success")
else:
    exit(1)
oldb=glob("/yadisk/backup/wiki*")
for i in oldb:
 if len(oldb)>3:
     os.remove(i)
shutil.copy('/tmp/wiki%s.sql' %date,'/yadisk/backup/' )
subprocess.call('rsync -av /yadisk/backup root@176.215.239.16:~/' ,shell=True)


oldb=glob("/yadisk/backup/strace.tar.gz**")
for i in oldb:
 if len(oldb)>3:
     os.remove(i)
subprocess.call('rsync -av /yadisk/backup root@176.215.239.16:~/' ,shell=True)