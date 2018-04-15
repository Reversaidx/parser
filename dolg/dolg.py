# -*- coding: utf-8 -*-
def dolg():
 import datetime,time
 from time import sleep
 SD=2000
 currenct=2000
 time1 = datetime.datetime.now() - datetime.datetime(2018, 4, 13, 23, 00)
 dolg_count = time1.total_seconds() / 60 / 40

 for i in range(1, int(dolg_count)):
     currenct += currenct * 0.01
 count=int(dolg_count)
# while True:
#  time1 = datetime.datetime.now() - datetime.datetime(2018, 4, 13, 23, 00)
#  dolg_count = time1.total_seconds() / 60 / 40
#  if int(dolg_count)!=count:
#      currenct += currenct * 0.01
#      count=int(dolg_count)
#  print ("Time of delay:")
 print ("Время просрочки: %s\nТекущий долг:%s" %(str(time1),int(currenct)))
dolg()