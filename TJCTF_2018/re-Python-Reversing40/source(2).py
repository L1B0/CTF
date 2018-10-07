import numpy as np

flag = 'redacted'

np.random.seed(12345)
arr = np.array([ord(c) for c in flag])
other = np.random.randint(1,5,(len(flag)))
arr = np.multiply(arr,other)

b = [x for x in arr]
lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]
c = [b[i]^lmao[i] for i,j in enumerate(b)]
print(''.join(bin(x)[2:].zfill(8) for x in c))

# original_output was 1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101