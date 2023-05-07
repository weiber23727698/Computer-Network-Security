from pwn import *
import socks
from lib import *
from Crypto.Util.number import bytes_to_long, long_to_bytes

public_key, sk = {}, {}
public_key[0], sk[0] = PublicKeyCipher.gen_key() # server0
public_key[1], sk[1] = PublicKeyCipher.gen_key() # server1
public_key[2], sk[2] = PublicKeyCipher.gen_key() # server2
public_key[3], sk[3] = PublicKeyCipher.gen_key() # Bob

route = [random.choice([0, 1, 2])]
while len(route) < 5:
    route.append(random.choice([i for i in range(3) if i != route[-1]]))
route.append(3)
route.reverse()
message = b'Give me flag, now!'
## padding(?), make the packet and call add_next_hop
packet = Packet.create(message, route[1], public_key[3])
print(route)
for i in range(1, len(route)):
    packet.add_next_hop(route[i-1], public_key[route[i]])
route.reverse()


try:
    for i in range(len(route) - 1):
        next_hop, next_packet = packet.decrypt_server(sk[route[i]])
        print(f"i: {i}, next: {next_hop}")
        assert next_hop == route[i+1]
        packet = next_packet
    message = packet.decrypt_client(sk[3])
    print(message)
    assert message == b'Give me flag, now!'
except Exception as e:
    print(e)
    print(f'Bob: I cannot hear you!')
    exit()

exit()

## send packet
r.sendlineafter("> ", packet.data.hex())

r.interactive()
