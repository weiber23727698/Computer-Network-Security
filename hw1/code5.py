from base64 import *

def Caesar(message):
    Letters = "abcdefghijklmnopqrstuvwxyz"
    Letters2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for key in range(len(Letters)):
        translated = ''
        for ch in message:
            if ch in Letters:
                num = Letters.find(ch)
                num = num - key
                if num < 0:
                    num = num + len(Letters)
                translated = translated + Letters[num]
            elif ch in Letters2:
                num = Letters2.find(ch)
                num = num - key
                if num < 0:
                    num = num + len(Letters2)
                translated = translated + Letters2[num]
            else:
                translated = translated + ch
        print('Hacking key is %s: %s' % (key, translated))

def decryptRailFence(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]
     
    # find the direction
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
         
        rail[row][col] = '*'
        col += 1
         
        if dir_down:
            row += 1
        else:
            row -= 1
             
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
            (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
         
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

def getkey(cipher, plaintext):
    tmp = b64decode(cipher)
    key = []
    for i in range(len(tmp)):
        key.append(tmp[i] ^ ord(plaintext[i]))
    return key

def getRes(cipher, key):
    res = ""
    if len(cipher) > len(key):
        print("out of bound")
    for i in range(len(cipher)):
        res += chr(cipher[i] ^ key[i%len(key)])
    return res

lookup = {"aaaaa": "A", "aaaab": "B", "aaaba": "C", "aaabb": "D", "aabaa": "E",
          "aabab": "F","aabba": "G", "aabbb": "H", "abaaa": "I", "abaab": "J",
          "ababa": "K","ababb": "L", "abbaa": "M", "abbab": "N", "abbba": "O",
          "abbbb": "P","baaaa": "Q", "baaab": "R", "baaba": "S", "baabb": "T",
          "babaa": "U","babab": "V", "babba": "W", "babbb": "X", "bbaaa": "Y", "bbaab": "Z"}

def decrypt(plaintext):
    decipher = ""
    i = 0
    while True:
        if i < len(plaintext)-4:
            substr = plaintext[i:i + 5]
            decipher += lookup[substr]
            i += 5
        else:
            break
 
    return decipher

def preprocess(message):
    plaintext = ""
    for letters in message:
        if letters<="Z" and letters>="A":
            plaintext += "B"
        elif letters>="a" and letters<="z":
            plaintext += "A"
    return plaintext

# Classical crypto is super easy!
## Caesar
round1 = input("round1: ")
Caesar(round1)
## Fences
round2 = input("round2: ")
fences = []
for i in range(2, 101):
    c = decryptRailFence(round2, i)
    if len(fences)!=0 and c == fences[-1]:
        break
    fences.append(c)
    print("key %d: %s" %(i, c))
## round3
round3_target = input("round3 target c2: ")
round3_c1 = input("round3 c1: ")
round3_m1 = input("round3 m1: ")
goal_c = b64decode(round3_target)
key = getkey(round3_c1, round3_m1)
res = getRes(goal_c, key)
print(res)
## round4
message = input("message: ")
plaintext = preprocess(message)
result = decrypt(plaintext.lower())
print(result)
fences2 = []
for i in range(2, 101):
    c = decryptRailFence(round2, i)
    if len(fences2)!=0 and c == fences2[-1]:
        break
    fences2.append(c)
    print("key %d: %s" %(i, c))
## Final
flag = input("flag: ")
real = b64decode(flag)
print(real)