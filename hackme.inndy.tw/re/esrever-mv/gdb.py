import os


f = open('a','r').read()
num = len(f)-1

gdb.execute("b *0x400A7B") # eax

def go():
    gdb.execute("continue")
    rax = int(gdb.parse_and_eval("$rax"))
    return rax

gdb.execute("start")

while 1:
        
    rax = go()
    if rax == 0:
        break

for i in range(num):
    rax = go()
    print("rax=: %d"%rax)

if rax == 0:
    os.system("echo T > check")
else:
    os.system("echo F > check")
