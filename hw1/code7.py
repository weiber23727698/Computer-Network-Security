from pwn import *
import requests
import argparse

parser = argparse.ArgumentParser(description="P13 ~ 16")
parser.add_argument("--problem", type=int, default = 1)
args = parser.parse_args()

def main():
    # Preprocess: download file, establish connection
    url1 = 'https://shattered.io/static/shattered-1.pdf?fbclid=IwAR2iQOJXx4HUviJsWms585KMu0Me8WhwkxF7KnMhxQBwASDlgciRQrL2ntk'
    r = requests.get(url1, allow_redirects=True)
    open('shattered-1.pdf', 'wb').write(r.content)
    url2 = 'https://shattered.io/static/shattered-2.pdf?fbclid=IwAR1Xm9Mn4Nz3gPWmDxnB93O-yS3K74rBZYYXo0bSvzBgJJBKtS_RygO06Ys'
    r = requests.get(url2, allow_redirects=True)
    open('shattered-2.pdf', 'wb').write(r.content)
    file1, file2 = open("shattered-1.pdf", "rb"), open("shattered-2.pdf", "rb")
    read1, read2 = file1.read(), file2.read()
    r = remote('cns.csie.org', 44377)
    # Register 1
    r.recvuntil('Your choice: ')
    r.sendline("1")
    r.sendlineafter('Username: ', read1+b"I love CNS")
    r.recvuntil('Here is your passkey, store it in a safe place: ')
    passwd1 = f"{r.recvline()}"[2:-3]
    # Register 2
    r.recvuntil('Your choice: ')
    r.sendline("1")
    r.sendlineafter('Username: ', read2+b"I love CNS")
    r.recvuntil('Here is your passkey, store it in a safe place: ')
    passwd2 = f"{r.recvline()}"[2:-3]
    # Login by user1
    r.recvuntil('Your choice: ')
    r.sendline("2")
    r.sendlineafter('Username: ', read1+b"I love CNS")
    r.sendlineafter('Passkey in Base64: ', passwd1)
    # buy the flag
    r.sendlineafter('Your choice: ', f"{args.problem+1}")
    r.recvuntil(f"Here is your flag {args.problem}: ")
    flag = f"{r.recvline()}"
    # Logout and Quit
    r.sendlineafter('Your choice: ', "1")
    r.sendlineafter('Your choice: ', "3")
    # CNS{ha$h_i5_m15used}
    # CNS{$ha1_15_n0t_c0ll1510n_r3s1st@nt}\n
    print(f"flag: {flag}")

if __name__ == "__main__":
    main()