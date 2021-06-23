import string

data = [0x77, 0xAD, 0x07, 0x02, 0xA5, 0x00, 0x29, 0x99, 0x28, 0x29, 
  0x24, 0x5E, 0x2E, 0x2A, 0x2B, 0x3F, 0x5B, 0x5D, 0x7C, 0x5C, 
  0x2D, 0x7B, 0x7D, 0x2C, 0x3A, 0x3D, 0x21, 0x0A, 0x0D, 0x08]

str_map = string.ascii_uppercase + string.digits
print(str_map)

def rol(a,n):

    a = (bin(a)[2:]).rjust(8,'0')
    a = eval('0b'+a[n:]+a[:n])

    return a
    

for j in str_map:
    a = ord(j)
    b = ord(j)
    a = a&0xf
    a = a&0x7
    #print(b,a)
    b = rol(b,a)
    #print(b)

    for i in range(8):
        a = data[i]
        #print(b)
        c = b^a
        #print(c,i)
        if chr(c) in str_map:
            print(i,j,chr(c))
        
