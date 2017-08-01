#!/usr/bin/python
import MySQLdb
import subprocess
import string
import random
import multiprocessing


num=8
def id_generator (size=39, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))

def df():
    kurwa = subprocess.Popen("df -h|grep mysql|awk '{print $5}'", stdout=subprocess.PIPE, stderr=None, shell=True)
    kurwa1 = kurwa.communicate()
    return int(kurwa1[0].split("%")[0])


def insert(num):
 db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="123",  # your password
                     db="test")        # name of the data base#

 num=num+1
 cur = db.cursor()
 cur.execute("insert into kurwa (num, data1, data2) values (%d, '%s', '%s');"  %(num,id_generator(),id_generator()))
 db.commit()
 print("Commit")
 #cur.close()

# Use all the SQL you like
i=4
key=100000
for num in range(4):
    multiprocessing.Process(target=insert, args=(key)).start()
    key=key*2





