
# Generating Info

p = 17459102747413984477
a = 2
b = 3
E = EllipticCurve(GF(p), [a, b])
G = E(15579091807671783999, 4313814846862507155)


key = 'blu3_3eC'
key = int(''.join([bytes(char, 'utf-8').hex() for char in 'blu3_3cC']), 16)

Q = key*G
print(Q)


# Solve the discrete log problem

solve = G.discrete_log(Q)
solve = bytes(int(solve).to_bytes(10, 'big'))
print(solve)
