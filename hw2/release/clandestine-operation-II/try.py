from template import *
from pwn import *
from binascii import *

# context.log_level = 'debug'

user = {
        "Azar": "d429c61d71e719d4f94eadfff13ebb23", 
        "Cyno": "c63aec25923b1f7c7d3d5a78257ae4bc", 
        "Alhaitham": "eea7e9e67c472ab48ee412861e7d8a48", 
        "Tighnari": "9ed636edea6d6de4d94b51e54aa6d1cc", 
        "Lisa": "90efdf511fbcdce25e836eb26458acaa", 
        "Faruzan": "3b9c1218d527fa1de09ee3355f11547b"
    }

# password = unhexlify(user['Azar'].encode())

r = remote('cns.csie.org', 44397)
r.sendlineafter(">>> ", "1")
r.sendlineafter("Username: ", "Azar")
type1 = gen_type1_msg()
r.sendline(type1)

type2 = r.recvline()
print(f"type2: {type2.hex()}")
# only challenge will be different
target_name_buf, flag, challenge, context, target_info_buf = parse_type2_msg(type2.hex())

type3 = header_signature() + header_type(3)