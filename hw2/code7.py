from pwn import *
import random
from tqdm import tqdm
from lib import *
from argparse import ArgumentParser


def flag1():
    context.log_level = 'debug'
    r = remote('cns.csie.org', 12804)
    public_key = [None for i in range(4)]
    r.recvuntil("The public key of server0 is ")
    pk0 = f"{r.recvline()}"[3:-4]
    public_key[0] = list(map(int, pk0.split(",")))
    r.recvuntil("The public key of server1 is ")
    pk1 = f"{r.recvline()}"[3:-4]
    public_key[1] = list(map(int, pk1.split(",")))
    r.recvuntil("The public key of server2 is ")
    pk2 = f"{r.recvline()}"[3:-4]
    public_key[2] = list(map(int, pk2.split(",")))
    r.recvuntil("The public key of Bob is ")
    pk_bob = f"{r.recvline()}"[3:-4]
    public_key[3] = list(map(int, pk_bob.split(",")))

    r.recvuntil("Your public key is ")
    pk = f"{r.recvline()}"[3:-4]
    pk = list(map(int, pk.split(",")))

    r.recvuntil("Your private key is ")
    sk = f"{r.recvline()}"[3:-4]
    sk = list(map(int, sk.split(",")))

    ## store incoming packets
    packets = []

    progress = tqdm(total=int(101))
    r.recvuntil("Wait for 3 seconds to start ...")
    while len(packets) < 101:
        p = r.recvline()
        if len(p) > 5:
            p = p.decode()
            message = bytes.fromhex(p)
            if len(message) != 400:
                continue
            new_packet = Packet(message)
            content = new_packet.decrypt_server(sk)
            packets.append((content[0], content[1].data.hex()))
            progress.update(1)
    random.shuffle(packets)

    ## send
    for i, packet in enumerate(packets):
        r.sendline(f"({packet[0]}, {packet[1]})")

    r.interactive()

def flag2():
    r = remote('cns.csie.org', 12805)

    public_key = [None for i in range(4)]
    r.recvuntil("The public key of server0 is ")
    pk0 = f"{r.recvline()}"[3:-4]
    public_key[0] = list(map(int, pk0.split(",")))
    r.recvuntil("The public key of server1 is ")
    pk1 = f"{r.recvline()}"[3:-4]
    public_key[1] = list(map(int, pk1.split(",")))
    r.recvuntil("The public key of server2 is ")
    pk2 = f"{r.recvline()}"[3:-4]
    public_key[2] = list(map(int, pk2.split(",")))
    r.recvuntil("The public key of Bob is ")
    pk_bob = f"{r.recvline()}"[3:-4]
    public_key[3] = list(map(int, pk_bob.split(",")))

    r.recvuntil("Send the message ")
    message = r.recvline()[1:-9]

    r.recvuntil("The route of the packet should be ")
    route = f"{r.recvline()}"[3: -28]
    route = list(map(int, route.split(",")))
    route.reverse()

    packet = Packet.create(message, route[1], public_key[3])
    for i in range(1, len(route)):
        packet.add_next_hop(route[i-1], public_key[route[i]])

    r.sendlineafter("> ", packet.data.hex())
    r.recvuntil("Bob: ")
    print(r.recvline())


def main():
    parser = ArgumentParser(description='P7 for CNS hw2')
    parser.add_argument("--problem", type = int, default=1)
    args = parser.parse_args()

    if args.problem == 1:
        flag1()
    elif args.problem == 2:
        flag2()

if __name__ == "__main__":
    main()