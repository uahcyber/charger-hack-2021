from pwn import *

#p = process(["python3","app.py"])
p = remote("127.0.0.1",15867)

p.recvuntil('you only have 20 seconds!\n\n')
counter = 0
while True:
    data = p.recv().decode().split("=")[0].strip()
    if "flag" in data:
        print(data)
        exit(-1)
    ans = eval(data)
    p.sendline(str(ans))
    p.recvline()