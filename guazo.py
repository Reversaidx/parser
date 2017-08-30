import random
import multiprocessing
import urllib3
def genstr():
    str1=[]
    strrange=range(ord('a'),ord('z')+1)
    for i in strrange:
        str1.append(chr(i))
    for i in range(0,10):
        str1.append(i)
    return ''.join(map(str,str1))

genst=genstr()
def parse():
 rd=random.sample(genst,k=32)
 string=''.join(rd)
 http=urllib3.PoolManager()
 r=http.request('GET','https://gyazo.com/%s' %string)
 while r.status!=200:
  rd = random.sample(genst, k=32)
  string = ''.join(rd)
  r=http.request('GET','https://gyazo.com/%s' %string)
  print('https://gyazo.com/%s' %string)
  print (r.status)
 print ("KURWA")
 exit(1)

for num in range(100):
    multiprocessing.Process(target=parse).start()