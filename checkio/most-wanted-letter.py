import string
def parse(text):
   characterdict={}
   for i in str.lower(text):
     if i in string.ascii_lowercase:
       if i in characterdict:
           characterdict[i]=characterdict[i]+1
       else:
           characterdict[i]=1
   max=sorted(characterdict.values())[-1]
   for i in string.ascii_lowercase:
       try:
        if characterdict[i]==max:
         return i
       except:
           pass

if __name__ == '__main__':
    print (parse("One"))