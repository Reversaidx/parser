# -*- coding: utf-8 -*-
import datetime,time
from time import sleep
def dolg():
 SD=2000
 currenct=2000
 time = datetime.datetime.now() - datetime.datetime(2018, 4, 13, 23, 00)
 dolg_count = time.total_seconds() / 60 / 40
 for i in range(1, int(dolg_count)):
     currenct += currenct * 0.01
 count=int(dolg_count)
 while True:
  time = datetime.datetime.now() - datetime.datetime(2018, 4, 13, 23, 00)
  dolg_count = time.total_seconds() / 60 / 40
  if int(dolg_count)!=count:
      currenct += currenct * 0.01
      count=int(dolg_count)
  #print("Time of delay:")
  return (time)
  return (currenct)
  sleep(1)