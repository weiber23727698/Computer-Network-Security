from pwn import *
from accumulator import *
from challenge2 import Division_Intractable_RSA_Accumulator

# context.log_level = 'debug'

# r = remote('cns.csie.org', 4002)
# r.recvuntil("N = ")
# N = int(r.recvline().decode(), 16)
# r.recvuntil("g = ")
# g = int(r.recvline().decode(), 16)

acc = Division_Intractable_RSA_Accumulator(1024)

message = ""
m = acc.HashToPrime(message.encode())
print(m)
acc.add(message.encode())

