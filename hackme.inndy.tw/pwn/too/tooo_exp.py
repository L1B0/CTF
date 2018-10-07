from pwn import *

io = remote( "hackme.inndy.tw", 7702 )

io.interactive()
