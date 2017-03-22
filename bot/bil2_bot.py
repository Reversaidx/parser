import requests
from requests.auth import HTTPBasicAuth
import re
import time
from bs4 import BeautifulSoup
import telebot

token = '335134502:AAEFvsBH_icdljXBfimaG3h0_zT2cYtGZ6U'
bot = telebot.TeleBot(token)
#функция авторизации
def auth():
 param={'language':"",
        'redirect':"",
       "username":'Rab',
       'password':"123"
       }
 url="https://5.61.34.118/test/admin/supportcenter.php"
 headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
 session = requests.Session()
 r=session.post('https://5.61.34.118/test/admin/dologin.php', auth=HTTPBasicAuth('rever','123'), data=param,headers=headers,verify=False)
 r=session.get(url,auth=HTTPBasicAuth('rever','123'),  cookies=r.cookies,headers=headers,verify=False)
 return r

#функция парсинга нужных значений
def pars(r):

 soup=BeautifulSoup(r.text,"html.parser")
 link =soup.findAll('div', 'stat',text="")
 reg=re.compile(r'<.*>(?P<num>\d+)<.*')
 new=reg.findall(str(link[0]))
 rep=reg.findall(str(link[1]))
 return int(new[0]),int(rep[0])

new_old,rep_old=pars(auth())
while True:

 new_tmp,rep_tmp=pars(auth())
 if new_tmp>new_old or rep_tmp>rep_old:
      print(new_tmp,rep_tmp)
      bot.send_message(321732078, "BILLING 2 NEW TICKET")
      new_old=new_tmp
      rep_old=rep_tmp
 if new_old<new_tmp or rep_old<rep_old:
      new_old=new_tmp
      rep_old=rep_tmp
 time.sleep(60)

