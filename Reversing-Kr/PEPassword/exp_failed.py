import string

def ror(a,n):

    a = bin(a)[2:].rjust(32,'0')
    a = eval('0b'+a[-n:]+a[:len(a)-n])

    return a

def sub_4091E0(input):

    print(input)
    passwd = 0xE98F842A
    eax = 0
    edx = 0

    input = [ord(i) for i in input]
    input.append(0)
    
    for i in input:

        eax = (eax^(i<<8))
        while 1:

            eax = (eax^(edx&0xff))
            eax += 0x434f4445
            eax &= 0xffffffff
            
            ecx = (eax&0xff)%32
            eax = ror(eax,ecx)

            eax = (eax^0x55aa5a5a)
            edx -= 1

            print(edx)
            if edx < 0:
                edx += 0x10000
            if edx == 0:
                break
            
    
    print(input,eax==passwd)

str_map = string.ascii_lowercase + string.digits + string.ascii_uppercase

input = ''
for a in str_map:

    sub_4091E0(a)
    for b in str_map:
        sub_4091E0(a+b)
