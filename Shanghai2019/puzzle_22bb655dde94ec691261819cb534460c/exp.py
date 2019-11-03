import os
'''
>>> a = [6, 1, 4, 9, 5, 0, 7, 2]
>>> b = [0x7C,0xAB,0x2D,0x91,0x2F,0x98,0xED,0xA9]
>>> c = [a[i]^b[i] for i in range(8)]
>>> c
[122, 170, 41, 152, 42, 152, 234, 171]
>>> map(hex,c)
['0x7a', '0xaa', '0x29', '0x98', '0x2a', '0x98', '0xea', '0xab']
flag{5cb92582-66a8-e5b7-d3bf-3b99df8ac7f0}
'''
xor = [0x7C,0xAB,0x2D,0x91,0x2F,0x98,0xED,0xA9]
#dd = [0x8A,0x01A1,0x012A,0x0269,0x209,0x68,0x039F,0x02C8]
correct_d = [0xFFFFFC49,104,16,0xFFFFCC30,14961,14456,231,0xFFFFFF11]
v = [[5,8],[1,6],[0,1,9],[0,4,9],[2,3,8],[4,6,7],[5,7],[2,3]]
num = 10**8

for aa in range(9,-1,-1):
    for bb in range(10):
        for cc in range(10):
            for dd in range(10):
                for ee in range(10):
                    for ff in range(10):
                        for gg in range(10):
                            for hh in range(10):
                                num -=1
                                #if num < 11104096:
                                #    continue
                                f = [aa,bb,cc,dd,ee,ff,gg,hh]
                                d = [0x8A,0x01A1,0x012A,0x0269,0x209,0x68,0x039F,0x02C8]

                                for vi in f:

                                    if vi == 0:
                                        d[2] &= d[6]
                                        d[3] *= d[2]
                                        d[2] = d[2] & 0xffffffff
                                        d[3] = d[3] & 0xffffffff
                                    elif vi == 1:
                                        if d[3] == 0:
                                            print ("Wrong!")
                                            break

                                        d[2] = d[2] // d[3]
                                        d[2] = d[2] & 0xffffffff
                                        d[1] += d[5]
                                        d[1] = d[1] & 0xffffffff
                                    
                                    elif vi == 2:
                                        d[4] ^= d[5]
                                        d[4] = d[4] & 0xffffffff

                                        d[7] += d[0]
                                        d[7] = d[7] & 0xffffffff
                                    
                                    elif vi == 3:
                                        d[7] -= d[4]
                                        d[7] = d[7] & 0xffffffff

                                        d[4] &= d[1]
                                        d[4] = d[4] & 0xffffffff
                                    
                                    elif vi == 4:
                                        d[5] *= d[0]
                                        d[5] = d[5] & 0xffffffff
                                        d[3] -= d[6]
                                        d[3] = d[3] & 0xffffffff
                                    
                                    elif vi == 5:
                                        d[0] ^= d[3]
                                        d[0] = d[0] & 0xffffffff
                                        d[6] -= d[7]
                                        d[6] = d[6] & 0xffffffff
                                    
                                    elif vi == 6:
                                        if d[7] == 0:
                                            break
                                        d[5] = d[5] | (d[1] // d[7])
                                        d[5] = d[5] & 0xffffffff
                                        d[1] = d[1] // d[7]
                                        d[1] = d[1] & 0xffffffff
                                    
                                    elif vi == 7:
                                        d[6] += d[2]
                                        d[6] = d[6] & 0xffffffff
                                        d[5] |= d[1]
                                        d[5] = d[5] & 0xffffffff
                                    
                                    elif vi == 8:
                                        d[0] *= d[3]
                                        d[0] = d[0] & 0xffffffff
                                        d[4] -= d[7]
                                        d[4] = d[4] & 0xffffffff
                                    
                                    elif vi == 9:
                                        d[2] += d[5]
                                        d[2] = d[2] & 0xffffffff
                                        d[3] ^= d[4]
                                        d[3] = d[3] & 0xffffffff

                                
                                print(num)
                                if d[:5] == correct_d[:5]:
                                    print(f)
                                    print([hex(l) for l in d])
                                    os.system("pause")

                                    


      
  

