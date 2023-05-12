from pwn import *
from Crypto.Util.number import long_to_bytes
from argparse import ArgumentParser

pk1 = {
    'p': 17273778075625677522481857001649048000254516373658641714706007905653799726491757288361568764249751425534604050731784256579722319314863497542342290134691959,
    'g': 2,
    'y': 9543574173467011822951693855239450750241211186088167468828571708954182706909453376410774593060587800089977883674087684271747587260177674591358373106628646
}

def flag1():
    alice = remote('cns.csie.org', 12346)
    bob = remote('cns.csie.org', 12347)
    alice.sendlineafter("Interactive mode (y/n)? ", "y")
    bob.sendlineafter("Interactive mode (y/n)? ", "y")

    alice.recvuntil("a = ")
    a = f"{alice.recvline()}"[2:-3]
    bob.sendlineafter("a = ", a)

    bob.recvuntil("c = ")
    c = f"{bob.recvline()}"[2:-3]
    alice.sendlineafter("c = ", c)

    alice.recvuntil("w = ")
    w = f"{alice.recvline()}"[2:-3]
    bob.sendlineafter("w = ", w)

    print(bob.recvline())
    
def flag2():
    r = remote('cns.csie.org', 12346)
    r.sendlineafter("Interactive mode (y/n)? ", "y")
    r.sendlineafter("c = ", "0")
    r.recvuntil("w = ")
    w0 = int(f"{r.recvline()}"[2:-3])
    r.close() # stop the connection

    r = remote('cns.csie.org', 12346)
    r.sendlineafter("Interactive mode (y/n)? ", "y")
    r.sendlineafter("c = ", "1")
    r.recvuntil("w = ")
    w1 = int(f"{r.recvline()}"[2:-3])
    r.close() # stop the connections
    
    print("=======================================================")
    print(f"flag2: {long_to_bytes(w1-w0)}")
    print("=======================================================")

def flag3():
    # reference: https://shrek.unideb.hu/~tengely/crypto/section-6.html#p-204-part9
    w = 1995135457311837329338013220674023065119097253499626394183669323611116768755869053
    print("=======================================================")
    print(f"flag3: {long_to_bytes(w)}")
    print("=======================================================")

def main():
    parser = ArgumentParser(description='P5 for CNS hw2')
    parser.add_argument("--problem", type = int, default=1) # E_in or E_out
    args = parser.parse_args()

    if args.problem == 1:
        flag1()
    elif args.problem == 2:
        flag2()
    elif args.problem == 3:
        flag3()

if __name__ == "__main__":
    main()