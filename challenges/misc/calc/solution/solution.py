from pwn import *

#p = process(["python3","app.py"])
p = remote("127.0.0.1",15867)

p.recvuntil('you only have 20 seconds!\n\n')
while True:
    data = p.recv().decode().split("=")[0].strip() # get equation
    if "flag" in data:
        print(data)
        break
    ans = eval(data) # solve equation (ik eval is bad, i'm just lazy)
    p.sendline(str(ans))
    p.recvline()