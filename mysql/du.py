import string
import random
import MySQLdb
import subprocess
import string
import random

def id_generator(size=39, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="123",  # your password
                     db="test")        # name of the data base


cur = db.cursor()
cur.execute("insert into kurwa (num, data1, data2) values (2, %s, %s)" %(id_generator(),id_generator()))

