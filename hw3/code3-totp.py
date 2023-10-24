from pwn import *
import hmac, base64, struct, hashlib, time, pyotp

def get_totp_token(secret):
    time_number = int(time.time()) // 30
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", time_number)
    h = hmac.new(key, msg, hashlib.sha1).digest()
    offset = h[-1] & 0x0F
    code = str((struct.unpack(">L", h[offset : offset + 4])[0] & 0x7fffffff) % 1000000)
    # adding 0 in the beginning till OTP has 6 digits
    while len(code) != 6:
        code = '0' + code
    return code

r = remote('cns.csie.org', 17504)

for __ in range(128):
    r.recvuntil("Key: ")
    key = r.recvline().decode().strip()
    totp_code = get_totp_token(key)
    r.sendlineafter("> ", f"{totp_code}")

print(r.recvline())