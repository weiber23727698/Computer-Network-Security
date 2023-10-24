from pwn import *
from accumulator import *

# context.log_level = 'debug'

def flag1():
    A = RSA_Accumulator(1024)

    r = remote('cns.csie.org', 4001)
    r.recvuntil("N = ")
    N = int(r.recvline().decode(), 16)
    r.recvuntil("g = ")
    g = int(r.recvline().decode(), 16)
    r.recvuntil("d = ")
    digest = int(r.recvline().decode(), 16)
    p = int("0xfe7fa2d93be7396c7172a7186f4e561949f53e436a7ed65da22786637b7e76081f65b972be84ea612787a07878c1bf9454edf81059f84158efe34b4207f96d71", 16)
    q = int("0xb76082ea921f3d4729e59d765ff014ad745b6421f1bacc359417e0c2a1aaa318bd96ba0f6476e09bd1db72fa4dfc7fa5aa0ee1bef7bc4f268fb42673e539d3b1", 16)
    phiN = (p-1) * (q-1)

    r.sendlineafter("Enter your choice? [0,1,2] ", "0")

    message = "yeah"
    m = A.HashToPrime(message.encode())
    k = pow(m, -1, phiN)
    r.sendlineafter("Give me your message: ", message)
    proof = pow(digest, k, N)
    r.sendlineafter("Give me your membership proof for the message: ", f"{proof}")
    return r.recvline() # cns{ph4k3_m3m83r5H1p!}
    r.close()

def flag2():
    A = RSA_Accumulator(1024)

    r = remote('cns.csie.org', 4001)
    r.recvuntil("N = ")
    N = int(r.recvline().decode(), 16)
    r.recvuntil("g = ")
    g = int(r.recvline().decode(), 16)
    r.recvuntil("d = ")
    digest = int(r.recvline().decode(), 16)
    p = int("0xfe7fa2d93be7396c7172a7186f4e561949f53e436a7ed65da22786637b7e76081f65b972be84ea612787a07878c1bf9454edf81059f84158efe34b4207f96d71", 16)
    q = int("0xb76082ea921f3d4729e59d765ff014ad745b6421f1bacc359417e0c2a1aaa318bd96ba0f6476e09bd1db72fa4dfc7fa5aa0ee1bef7bc4f268fb42673e539d3b1", 16)
    phiN = (p-1) * (q-1)

    r.sendlineafter("Enter your choice? [0,1,2] ", "1")

    message = "Member2"
    r.sendlineafter("Give me your message: ", message)
    m = A.HashToPrime(message.encode())
    a, b = pow(m, -1, phiN), 0
    proof = (pow(g, a, N), b)
    r.sendlineafter('g^a = ', f"{proof[0]}")
    r.sendlineafter('b = ', f"{proof[1]}")
    return r.recvline() # cns{N0N_n0n_m3M83RSh1p!}

def main():
    ans1, ans2 = flag1(), flag2()
    print(ans1)
    print(ans2)
    
if __name__ == "__main__":
    main()