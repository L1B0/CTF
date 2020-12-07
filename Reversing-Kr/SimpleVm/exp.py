opcode = [
    0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x45, 
  0x45, 0xC4, 0xC4, 0x04, 0x04, 0x65, 0x44, 0xE4, 0x08, 0xC4, 
  0x04, 0xE4, 0x44, 0xE4, 0x25, 0xE4, 0x04, 0xE4, 0x25, 0x44, 
  0x44, 0xE4, 0xC8, 0xC4, 0x24, 0xE4, 0x44, 0xE4, 0x44, 0xE4, 
  0x24, 0xE4, 0x25, 0x44, 0x44, 0xE4, 0xA6, 0xC4, 0x44, 0xE4, 
  0x44, 0xE4, 0xC0, 0xE4, 0x44, 0xE4, 0x25, 0x44, 0x44, 0xE4, 
  0xE4, 0xC4, 0x64, 0xE4, 0x44, 0xE4, 0xA1, 0xE4, 0x64, 0xE4, 
  0x25, 0x44, 0x44, 0xE4, 0x8D, 0xC4, 0x84, 0xE4, 0x44, 0xE4, 
  0x40, 0xE4, 0x84, 0xE4, 0x25, 0x44, 0x44, 0xE4, 0x68, 0xC4, 
  0xA4, 0xE4, 0x44, 0xE4, 0xE4, 0xE4, 0xA4, 0xE4, 0x25, 0x44, 
  0x44, 0xE4, 0x0B, 0xC4, 0xC4, 0xE4, 0x44, 0xE4, 0x06, 0xE4, 
  0xC4, 0xE4, 0x25, 0x44, 0x44, 0x04, 0x24, 0x65, 0x04, 0x04, 
  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 
  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 
  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 
  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 
  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 
  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 
  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 
  0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04
    ]
dword_804B18c, dword_804B190, dword_804B194, dword_804B198, dword_804B19c = 0,0,0,0,0

def string_decode(a):
    #a = [0x40,0x61,0x60,0x61,0x76,0x75,0x27,0x4C,0x6C,0x64,0x62,0x69,0x69,0x0440,0x61,0x60,0x61,0x76,0x75,0x27,0x4C,0x6C,0x64,0x62,0x69,0x69,0x04]
    a = [ (i+1)^a[i] for i in range(len(a))]
    #print(a)
    a = ''.join(map(chr,a))
    print(a)

def opcode_init(input):

    global opcode

    # sub_80489AA 
    opcode = [ (((i<<3)&0xff)|(i>>5)) for i in opcode ]
    #print(opcode)

    opcode = [ i^0x20 for i in opcode]
    opcode[:8] = input
    #opcode = [ i for i in opcode]
    print(opcode)

def sub_8048a48():

    global opcode, dword_804B190
    
    # opcode[9] is the index
    # dword_804B190 is the opcode[index] and then index ++
    dword_804B190 = opcode[(opcode[9])]
    opcode[9] = ((opcode[9])+1)
    
def vm():

    global opcode, dword_804B18c, dword_804B190, dword_804B194, dword_804B198, dword_804B19c
    
    while 1:
        sub_8048a48()
        print("dword_804B190 = %d"%dword_804B190)
        #print("opcode[9] = %d"%opcode[9])
        #print(opcode)
        if dword_804B190 == 2:
            # i = opcode[9]
            # opcode[opcode[i]] = opcode[i+1]
            sub_8048a48()
            dword_804B198 = dword_804B190
            sub_8048a48()
            dword_804B194 = dword_804B190

            opcode[dword_804B198] = dword_804B194
            print("opcode[%d] = %d"%(dword_804B190,dword_804B198))
            
        elif dword_804B190 == 6:
            # i = opcode[9]
            # opcode[opcode[i]] = opcode[opcode[i]]^opcode[opcode[i+1]]
          
            sub_8048a48()
            dword_804B18c = dword_804B190

            sub_8048a48()
            #dword_804B194 = opcode[dword_804B190] # 0-'a' 7
            #dword_804B190 = opcode[dword_804B18c]

            dword_804B198 = opcode[dword_804B18c]^opcode[dword_804B190]
            print("opcode[%d]^opcode[%d]=%d^%d=%d"%(dword_804B18c,dword_804B190,opcode[dword_804B18c],opcode[dword_804B190],dword_804B198))
            #dword_804B190 = dword_804B18c

            opcode[dword_804B18c] = dword_804B198
            #print("opcode[%d] = %d"%(dword_804B18c,dword_804B190))
            
        elif dword_804B190 == 7:
            # i = opcode[9]
            # opcode[opcode[i]] ?== opcode[opcode[i+1]]
            sub_8048a48()
            dword_804B190 = opcode[dword_804B190]
            print("opcode[%d] = %d"%(7, opcode[7]))
            dword_804B198 = dword_804B190

            sub_8048a48()
            print(dword_804B190)
            dword_804B190 = opcode[dword_804B190]
            dword_804B194 = dword_804B190

            print(" %d == %d?"%(dword_804B194,dword_804B198))
            if dword_804B194 == dword_804B198:
                dword_804B198 = 1
            else:
                dword_804B198 = 1 # patch, make it continue.

            opcode[8] = dword_804B198 # check_flag
            
            
        elif dword_804B190 == 9:

            sub_8048a48()

            if opcode[8] == 0: # not equal, next step is break
                opcode[9] = (opcode[0xa]+dword_804B190)
            
        elif dword_804B190 == 10:

            sub_8048a48()
            opcode[9] = (opcode[0xa] + dword_804B190)
            print("opcode[%d] = %d"%(9,opcode[9]))
            
        elif dword_804B190 == 11:
            
            #dword_804B190 = 0
            #dword_804B190 = opcode[0]
            #dword_804B198 = dword_804B190

            #dword_804B190 = 1
            #dword_804B190 = opcode[1]
            #dword_804B194 = dword_804B190

            #dword_804B190 = dword_804B198
            #dword_804B198 = dword_804B194
            print("nothing.")
        else:
            break
        
input = 'abcdefgh'

opcode_init([ord(i) for i in input])
vm()
