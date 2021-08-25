# take block of data in .data section of binary, then 
# subtract 18 from each value and XOR it with len(password)-current_position

# data from disassembling executable
# binary ninja: copy as 32-bit element C-array (little endian)
data = [0x0000008f, 0x00000078, 0x00000080, 0x00000070,
	0x0000005e, 0x00000029, 0x00000062, 0x00000057,
	0x00000055, 0x00000041, 0x0000008c, 0x00000040,
	0x0000008a, 0x00000056, 0x0000005c, 0x0000008a,
	0x0000005d, 0x00000076, 0x00000073, 0x00000037,
	0x00000078, 0x00000089, 0x00000039, 0x00000060,
	0x00000083, 0x0000006f, 0x0000007d, 0x00000064,
	0x00000074, 0x0000004d, 0x00000070, 0x00000068,
	0x0000008e, 0x00000081, 0x00000047, 0x0000006c,
	0x0000007b, 0x00000045, 0x00000086, 0x0000008e]

flag = ""
for i, c in enumerate(data): # enumerate() gives index, value
    flag += chr((c - 18) ^ (len(data) - i))
print(f"flag: {flag}")
