def header_signature():
    return b'NTLMSSP\x00'

def header_type(message_type):
    return message_type.to_bytes(4, "little")

def header_flags(flags):
    return flags.to_bytes(4, "little")

def write_security_buffer(input_bytes, offset):
    length = len(input_bytes).to_bytes(2, "little")
    allocated_size = length
    offset = offset.to_bytes(4, "little")
    return length + allocated_size + offset

def read_seurity_buffer(input_bytes):
    if isinstance(input_bytes, str):
        input_bytes = input_bytes.encode()

    length = int.from_bytes(input_bytes[:2], "little")
    allocated_size = int.from_bytes(input_bytes[2:4], "little")
    offset = int.from_bytes(input_bytes[4:8], "little")
    return length, allocated_size, offset

def gen_type1_msg():
    msg = header_signature() + header_type(1) + header_flags(0x60080014)
    return msg

def parse_type2_msg(msg):
    # TODO
    target_name_buf = msg[24:40]
    flag = msg[40:48]
    challenge = msg[48:64]
    context = msg[64:80]
    target_info_buf = msg[80:96]
    return target_name_buf, flag, challenge, context, target_info_buf

def gen_type3_msg():
    # TODO
    msg = header_signature() + header_type(3)
    return msg

user = {
        "Azar": "d429c61d71e719d4f94eadfff13ebb23", 
        "Cyno": "c63aec25923b1f7c7d3d5a78257ae4bc", 
        "Alhaitham": "eea7e9e67c472ab48ee412861e7d8a48", 
        "Tighnari": "9ed636edea6d6de4d94b51e54aa6d1cc", 
        "Lisa": "90efdf511fbcdce25e836eb26458acaa", 
        "Faruzan": "3b9c1218d527fa1de09ee3355f11547b"
    }
from pwn import *
from binascii import *

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