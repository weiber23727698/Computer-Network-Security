from cipher import StreamCipher, PublicKeyCipher
from lib import *

plaintext = b'\x00\x01\x02\x03'

# cipher = StreamCipher.encrypt(10, plaintext)
# print(cipher)
# decoded = StreamCipher.decrypt(10, cipher)
# print(decoded)


pk, sk = PublicKeyCipher.gen_key()
pk2, sk2 = PublicKeyCipher.gen_key()

packet = Packet.create(b"hello bob", 1, pk)
print(packet.decrypt_client(sk))

packet.add_next_hop(1, pk)
packet.add_next_hop(2, pk2)

x1 = packet.decrypt_server(sk2)
print(x1[0])
x2 = x1[1].decrypt_server(sk)
print(x2[0])
x3 = x2[1].decrypt_client(sk)
print(x3)