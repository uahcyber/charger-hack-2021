from pwn import *

password = 'z3R0-c00!B1U3'

p = remote('127.0.0.1',15727)

p.recvuntil('Enter the password: ')
p.sendline(password)
p.interactive()