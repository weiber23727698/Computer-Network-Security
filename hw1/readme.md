# CNS 2023 Spring Hw1
## Simple Crypto
First, I would like to confess that I didn't apply pwn to this problem. Thus, it could be a little troublesome to reproduce my result.
```shell
python code5.py
```
1. Finish the summation and retype on your own
2. Copy the ciphertext of Caesar cipher and find the reasonable solution with your eyes and copy it to the termianl
3. Copy the ciphertext of Rail Fence cipher and find the reasonable solution with your eyes and copy it to the termianl
4. This round requires three strings to be copied. The order is as following: c2, c1, m1. However, if the length of c2 is longer than that of c1, my decryption would fail because of the lake of key. I have tried to view the list of key as circular but in vain.
5. Copy the ciphertext and wait for the result of final rail fence cipher and copy the result to the termianl
6. Copy the encoded flag and you will catch the flag
## ElGamal Cryptosystem
```shell
python code6.py # 6-(a)
python code6.py --problem c # 6-(c)
```
## Bank
```shell
python code6.py # 7-(a)
python code6.py --problem 2 # 7-(b)
```
## Clandestine Operation
```shell
python code8.py # It will print both flags in the end.
```