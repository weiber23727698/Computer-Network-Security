from pwn import *

# context.log_level = 'debug'

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