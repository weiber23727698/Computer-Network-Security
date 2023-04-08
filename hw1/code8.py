from pwn import *

BLOCK_SIZE = 16

def transform_to_10(s):
    a, b = None, None
    if ord(s[0]) >= ord('a'):
        a = ord(s[0]) - ord('a') + 10
    else:
        a = int(s[0])
    if ord(s[1]) >= ord('a'):
        b = ord(s[1]) - ord('a') + 10
    else:
        b = int(s[1])
    return a*16 + b

def transform_to_16(s: int):
    val = hex(s)[2:]
    if len(val) == 1:
        val = "0" + val
    return val

## Collect ID
r = remote('cns.csie.org', 44399)
r.recvuntil('| ID: ')
ID = f"{r.recvline()}"[2:-5]
for i in range(3):
    r.recvuntil('| ')
    ID += f"{r.recvline()}"[2:-5]
## Enter Akademiya
block_id = len(ID)//(BLOCK_SIZE*2) - 2
r.sendlineafter("Your choice: ", "2")
plaintext = ""
while block_id >= 0:
    print(f"block_id: {block_id}")
    curr = ID[block_id*BLOCK_SIZE*2 : (block_id+1)*BLOCK_SIZE*2]
    block_txt = ""
    for i in range(16):
        prev = ""
        for j in range(i-1, -1, -1):
            prev += transform_to_16(transform_to_10(curr[30-2*j:30-2*j+2]) ^ transform_to_10(block_txt[2*j:2*j+2][::-1]) ^ (i+1))
        ## guess plaintext
        for guess in range(256):
            if i==0 and guess==1:
                continue
            b = transform_to_10(curr[30-2*i:30-2*i+2]) ^ guess ^ (i+1)
            bb = transform_to_16(b)
            ## new modified cipher to oracle
            res = ID[:block_id*BLOCK_SIZE*2+(30-i*2)] + bb + prev + ID[(block_id+1)*BLOCK_SIZE*2:(block_id+2)*BLOCK_SIZE*2]
            r.sendlineafter("Your choice: ", "1")
            r.sendlineafter('Please give me the ID (hex encoded): ', res)
            oracle = f"{r.recvline()}"   
            if "It seems feasible..." in oracle or "Not a valid ID..." in oracle:
                block_txt += transform_to_16(guess)[::-1]
                break
    plaintext += block_txt
    block_id -= 1
plaintext = plaintext[::-1]
flag1 = b''
idx = 0
while idx < len(plaintext):
    val = transform_to_10(plaintext[idx:idx+2])
    flag1 += bytes([val])
    idx += 2
print(f"flag1: {flag1}")
r.sendlineafter("Your choice: ", "3")
r.sendlineafter("Your choice: ", "1")
r.sendlineafter("Please speak out the secret word: ", flag1[45:-6])
## Enter Sanctuary of Surasthana
def xor(a, b):
    idx = 0
    block = ""
    while idx < BLOCK_SIZE*2:
        val = transform_to_10(a[idx:idx+2]) ^ transform_to_10(b[idx:idx+2])
        block = block + transform_to_16(val)
        idx = idx + 2
    return block

encoded = "6a6f62207469746c653a4772616e64204469736369706c696e617279204f6666696365727c7c6e616d653a43796e6f7c7c73656372657420776f72643a434e537b416b615f4249545f6631697070314e395f61745461436b217d060606060606"
plaintext, ciphertext = [], []
r.sendlineafter("Your choice: ", "2")
idx = 0
while idx < len(encoded):
    plaintext.append(encoded[idx : idx+BLOCK_SIZE*2])
    ciphertext.append(ID[idx : idx+BLOCK_SIZE*2])
    idx += BLOCK_SIZE*2
new_plain = plaintext[2][:-10] + "417a61727c"
d2 = xor(plaintext[2], ciphertext[1])
new_cipher = xor(d2, new_plain)
res = None
sign = 0
for i in range(43, 256):
    first = transform_to_16(i)
    print(f"i: {i}")
    for j in range(256):
        new_cipher = first + transform_to_16(j) + new_cipher[4:]
        ciphertext[1] = new_cipher
        res = ""
        for x in ciphertext:
            res = res + x
        r.sendlineafter("Your choice: ", "1")
        r.sendlineafter('Please give me the ID (hex encoded): ', res)
        oracle = f"{r.recvline()}"
        if "It seems feasible..." in oracle:
            sign = 1
            break
    if sign == 1:
        break
r.sendlineafter("Your choice: ", "3")
r.sendlineafter("Your choice: ", "1")
r.sendlineafter("Please enter your ID (hex encoded): ", res)
print(r.recvline())
print("\n===============================================================================")
print(f"FLAG1: {flag1[45:-6]}")
print(r.recvline())
print("===============================================================================")






