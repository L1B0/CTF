import os
from pwn import *

flag = ''
while 1:
    
    for i in range(32,128):
        
        temp_flag = flag+chr(i)
        f = open('a','w')
        f.write(temp_flag+'\n')
        f.close()

        os.system("gdb ./esrever-mv -x gdb.py < a")

        check = open('./check','r').read(1)
        if check == 'T':
            flag = temp_flag
            break
        
    pause()
    if flag[-1] == '}':
        break

os.system("echo %s > flag"%flag)
