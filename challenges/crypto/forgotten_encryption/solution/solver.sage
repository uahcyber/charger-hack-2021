#!/usr/bin/env sage

p = 2
F = GF(p)
P.<x> = PolynomialRing(F)

from sage.coding.information_set_decoder import LeeBrickellISDAlgorithm


class Cipher:
  def __init__(self, size, params):
    self.size = size
    self.params = params

  def sequence(self, key):
    while True:
      key = key * self.params[0]
      yield key + self.params[1]

  def encrypt(self, key, data, strength, linear=False):
    for value, pbit in zip(self.sequence(key), data):
      xbit = sum(value[i] for i in range(0, strength, 2))
      ybit = mul(value[i] for i in range(1, strength, 2))

      if linear:
        yield int(pbit) ^^ int(xbit)
      else:
        yield int(pbit) ^^ int(xbit) ^^ int(ybit)


def ISD_attack(size, stream, params, strength, error):
  M = []
  clean = [0] * len(stream)
  cipher = Cipher(size, params)

  for i in range(size):
    row = list(cipher.encrypt(x^(size - 1 - i), clean, strength, linear=True))
    M.append(row)

  G = matrix(F, M)
  v = vector(F, stream)

  C = codes.LinearCode(G)
  A = LeeBrickellISDAlgorithm(C, error)
  A.calibrate()

  print(A)
  print(A.time_estimate())

  r = A.decode(v)
  e = v - r

  key = G.solve_left(r)
  return P(list(key)[::-1])


def main():
  size = 256
  length = 1024
  strength = 10
  error = (15, 25)

  q = P.irreducible_element(size, 'minimal_weight')
  R.<z> = P.quo(q)

  a = R(z^255 + z^253 + z^252 + z^251 + z^250 + z^249 + z^248 + z^247 + z^246 + z^245 + z^243 + z^242 + z^241 + z^239 + z^238 + z^237 + z^235 + z^233 + z^231 + z^228 + z^227 + z^226 + z^225 + z^224 + z^223 + z^222 + z^220 + z^218 + z^213 + z^212 + z^210 + z^209 + z^208 + z^207 + z^203 + z^202 + z^190 + z^189 + z^188 + z^187 + z^186 + z^182 + z^180 + z^179 + z^178 + z^177 + z^176 + z^175 + z^174 + z^172 + z^165 + z^164 + z^162 + z^160 + z^159 + z^158 + z^157 + z^150 + z^149 + z^148 + z^147 + z^146 + z^143 + z^140 + z^139 + z^137 + z^136 + z^135 + z^134 + z^132 + z^130 + z^125 + z^120 + z^118 + z^117 + z^115 + z^111 + z^109 + z^105 + z^104 + z^101 + z^99 + z^95 + z^94 + z^92 + z^90 + z^87 + z^84 + z^83 + z^82 + z^79 + z^78 + z^77 + z^74 + z^70 + z^68 + z^66 + z^65 + z^64 + z^63 + z^62 + z^59 + z^55 + z^54 + z^51 + z^50 + z^48 + z^47 + z^46 + z^45 + z^44 + z^42 + z^41 + z^39 + z^36 + z^35 + z^33 + z^30 + z^28 + z^27 + z^26 + z^25 + z^23 + z^21 + z^19 + z^18 + z^16 + z^14 + z^13 + z^5 + z^2 + z + 1)
  b = R(z^255 + z^253 + z^249 + z^248 + z^244 + z^243 + z^242 + z^241 + z^240 + z^239 + z^238 + z^236 + z^234 + z^233 + z^231 + z^228 + z^227 + z^226 + z^225 + z^223 + z^222 + z^221 + z^219 + z^217 + z^216 + z^215 + z^213 + z^211 + z^209 + z^206 + z^205 + z^203 + z^196 + z^194 + z^192 + z^190 + z^189 + z^188 + z^187 + z^186 + z^185 + z^182 + z^181 + z^180 + z^179 + z^178 + z^176 + z^175 + z^170 + z^168 + z^167 + z^166 + z^156 + z^155 + z^154 + z^153 + z^152 + z^150 + z^149 + z^148 + z^145 + z^143 + z^141 + z^140 + z^139 + z^137 + z^136 + z^135 + z^134 + z^131 + z^130 + z^129 + z^127 + z^126 + z^125 + z^123 + z^122 + z^120 + z^119 + z^116 + z^115 + z^114 + z^112 + z^111 + z^110 + z^109 + z^107 + z^106 + z^105 + z^104 + z^102 + z^100 + z^99 + z^98 + z^96 + z^95 + z^93 + z^92 + z^91 + z^90 + z^86 + z^83 + z^82 + z^81 + z^80 + z^79 + z^78 + z^74 + z^70 + z^69 + z^63 + z^60 + z^59 + z^58 + z^55 + z^53 + z^52 + z^51 + z^48 + z^47 + z^46 + z^45 + z^38 + z^36 + z^34 + z^28 + z^27 + z^23 + z^20 + z^17 + z^16 + z^15 + z^14 + z^13 + z^9 + z^8 + z^6 + z^5 + z^4 + 1)

  message = 128535117555304255782843316448837583985741779214504437594523327946810963738669689579300532332358869182408731798628388025029658108177854492705135756861443091281720475936859475215124008611362122913096360417320335972295252303921800027384280415761008049614592175812848846851183403400535921426238076451103515205250
  ciphertext = list(map(int, bin(message)[2:]))

  key = ISD_attack(size, ciphertext[:-size], [a, b], strength, error)

  cipher = Cipher(size, [a, b])
  plaintext = cipher.encrypt(key, ciphertext, strength)
  result = int(''.join(str(bin) for bin in plaintext), 2)

  print(result.to_bytes(length, 'big').strip(b'\x00'))

if __name__ == '__main__':
  main()
