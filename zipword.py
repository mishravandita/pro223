import zipfile
import time
  

folderpath =input('Path to the file: ')
zipf = zipfile.ZipFile(folderpath)
global result
result =0
global tried
tried =0
c=0
if not zipf:
    print('The zipped file/folder is not password protected!You can open it!')

else:
    wordlistfile=open('wordlist.txt','r',errors="ignore") 
    body=wordlistfile.read().lower()
    words=body.split('\n')
    for i in range(len(words)):
        word=words[i]
        result=zipfile.decrypt(word)
        if result==1:
            print("the password is"+word)
            break
        elif result==0:
            tried+=1
            print("password not found"+str(tried))       
            continue    
if (result==0):
    print("Sorry,password not found.A total of "+str(c)+"+ possible combination tried in"+str(duration)+'second')
else:
    duration= endtime-starttime
    print('Congratulation!!! Password found after trying '+str(c)+'combination in'+str(duration)+'seconds')  

