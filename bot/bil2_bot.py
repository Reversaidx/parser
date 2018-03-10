import requests
from bot import  conf
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
       "username":conf.user,
       'password':conf.passw
       }
 url="https://cp.mrhost.biz/admin/supportcenter.php"
 headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
 session = requests.Session()
 r=session.post('https://cp.mrhost.biz/admin/dologin.php', auth=HTTPBasicAuth(conf.httpuser,conf.httppass), data=param,headers=headers)
 r=session.get(url,auth=HTTPBasicAuth(conf.httpuser,conf.httppass),  cookies=r.cookies,headers=headers)
 #print(r.text)
 return r

#функция парсинга нужных значений
def pars(r):

 soup=BeautifulSoup(r.text,"html.parser")
 link =soup.findAll('div', 'stat',text="")
 print(link)
 reg=re.compile(r'<.*>(?P<num>\d+)<.*')
 new=reg.findall(str(link[0]))
 rep=reg.findall(str(link[1]))
 return int(new[0]),int(rep[0])

new_old,rep_old=pars(auth())
while True:

 new_tmp,rep_tmp=pars(auth())
#если количество тикетов стало больше нужно реагировать
 if new_tmp>new_old or rep_tmp>rep_old:
      print(new_tmp,rep_tmp)
      bot.send_message(conf.chatid, "BILLING 2 NEW TICKET")
      new_old=new_tmp
      rep_old=rep_tmp
#если количество тикетов и ответов стало меньше нужно сбросить значения, е
 if new_old<new_tmp or rep_old<rep_old:
      new_old=new_tmp
      rep_old=rep_tmp
      print(new_old,rep_old)
 time.sleep(60)
