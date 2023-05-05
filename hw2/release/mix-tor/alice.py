from pwn import *
import socks
from lib import *
from Crypto.Util.number import bytes_to_long, long_to_bytes

# context.log_level = 'debug'

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
target = f"{r.recvline()}"[3: -28]
target = list(map(int, target.split(",")))
target.reverse()

## padding(?), make the packet and call add_next_hop
correct_data = Packet.create(message, 3, public_key[3])
packet = Packet(correct_data)
for i in range(1, len(target)):
    packet.add_next_hop(target[i], public_key[target[i]])


## send packet
r.sendlineafter("> ", packet.data.hex())

print(packet)
r.interactive()
