import re, paramiko, os
str1='5.255.251.2 - - [01/Mar/2017:05:38:16 +0300] "GET /e-store/xml_catalog/38/262/ HTTP/1.0" 200 6867 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"'
str2='5.255.251.2 - - [01/Mar/2017:05:38:20 +0300] "GET /e-store/xml_catalog/22/261/ HTTP/1.0" 200 6954 "-" "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)"'
str3='153.36.233.35 - - [01/Mar/2017:11:52:28 +0300] "GET / HTTP/1.0" 301 305 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"'
str4='91.121.146.47 - - [01/Mar/2017:14:20:40 +0300] "GET /w00tw00t.at.ISC.SANS.DFind:) HTTP/1.1" 400 184 "-" "-"'
str5='''127.0.0.1 - frank [10/Oct/2000:13:55:36 0700] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I;Nav)"'''
str6='''127.0.0.1 - frank [10/Oct/2000:13:55:36 0700] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I;Nav)"'''
list=[str1,str2,str3,str4,str5,str6]
#регулярное выражение по которому выполняется поиск
log_line_re = re.compile(r'''(?P<ip>\S+) #IP ADDRESS
\s+ #whitespace
#.*
\S+ #remote logname
\s+ #whitespace
\S+ #remote user
\s+ #whitespace
#(?P<time>\[[^\[\]]+\]) #time

\[[^\[\]]*\]
\s+ #whitespace
"
(?P<request>[^"]+)" #first line of request
\s+ #whitespace
(?P<status>\d+)
\s+ #whitespace
(?P<bytes_sent>-|\d+)
\s* #whitespace
''', re.VERBOSE)
a=[]
#поиск и группировка по регулярному выражению
def dictify_logline(line):
    m = log_line_re.match(line)
    if m:
        groupdict = m.groupdict()
        if groupdict['bytes_sent'] == '0':
            groupdict['bytes_sent'] = '0'
        return groupdict
    else:
            return {'remote_host': None,
                    'status': None,
                    'bytes_sent': "0",
                                    }
#класс, где хранятся все запросы
class ip():
    def __init__(self,ip):
        self.ip=ip
        self.request=[]
        self.status=[]
        self.count=0

    def add(self,requst,status):
        self.status.append(status)
        self.count+=1
        self.request.append(requst)

ip_list=[]#список объектов
#функция которая записывает в переменную list последние 1000 строк логов
def down(ip,passw,logname):
    s=paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname="5.61.34.118",port=22,username="root",password="ipoPA4nDEg")
    #kurwa=s.exec_command("ifconfig")
    stdin, stdout, stderr = s.exec_command('tail -n 1000 /var/www/httpd-logs/kurwakurwa228.tk.access.log')
    global list
    list=stdout.readlines()
    s.close()

down(1,1,1)
#функция выпонляет сравнение, присуствует ли такой IP, если нет то создаётся новый объект
for line in list:
    m=dictify_logline(line)
    l=0
    for kal in ip_list:
        if kal.ip==m['ip']:
            l=1
            break
    if l==0:
        temp=ip(m['ip'])
        temp.add(m['request'],m['status'])
        ip_list.append(temp)
    if l==1:
        kal.add(m['request'],m['status'])

#проверка работы
for i in ip_list:
    print(i.ip, i.request, i.status)

#test


jkvgcxsfgsxcfgsxdf