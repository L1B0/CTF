def addr_trans(addr):
    return hex(addr-0xF7D6B000-0x1000)

print(addr_trans(0xF7E1C4D0))
