import random
import string

characters = ''.join(map(chr, range(0x20, 0x7f)))
print(characters)

mapping = '''D&E!Y"'%T^)-w>L#l*Gu,50RH2Jk38;CO]rQh<f=v.djs{gcio (|\A~F9B$ISPVaz/m:Z`@_Mxt[Xp1Uy764NW?e}+Kbqn'''
key = '''fs]=#Ql*:DpuWu7D/l4_u7u:DXuDOp}?O}K'''

T = str.maketrans(mapping, characters)

print( key.translate(T) )
