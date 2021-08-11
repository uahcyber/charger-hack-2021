flag = 'UAH{h4rdc0d3d_PaSsw0rd5_aRe_n0T_th3_m0v}'.encode()

encoded = []
for i,c in enumerate(flag):
    encoded.append((c^(len(flag)-i))+18)
print(encoded)
print(len(encoded))