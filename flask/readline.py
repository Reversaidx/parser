import subprocess
def readsl(start,end):
    file=open('tmp.txt','wt')
    file.write(subprocess.getoutput("sed -n '%s,%sp' testfile " %(start,end)))
    file.close()
if __name__ == '__main__':
    test=readsl(2,4)
    print (type(test))
