#!/usr/bin/env python3
import textwrap
import requests
'''
两个相同的数异或为0，那么在相应的位置就不可能出现和flag相等的数
'''
record = [[False for __ in range(256)] for _ in range(50)]
print(record[0])

while True:
    r = requests.get("https://hackme.inndy.tw/otp/?issue_otp=flag.php")
    enc = r.text.strip('\n').split('\n')
    #print(enc)
    for e in enc:
        print(e)
        for i, v in enumerate(textwrap.wrap(e, 2)):
            record[i][int(v, 16)] = True
    if all(map(lambda x: x.count(True) == 255, record)):
        with open('flag.txt','w') as a:
            a.write(str(record))
        break

ans = ''.join(map(lambda x: chr(x.index(False)), record))

print(ans)
