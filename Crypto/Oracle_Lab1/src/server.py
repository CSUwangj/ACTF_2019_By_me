#!/usr/bin/env python3
from os import urandom
from itertools import permutations
from flag import message

banner = """
 /$$      /$$           /$$                                                     /$$                    
| $$  /$ | $$          | $$                                                    | $$                    
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$        /$$$$$$    /$$$$$$       
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$      |_  $$_/   /$$__  $$      
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$        | $$    | $$  \ $$      
| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/        | $$ /$$| $$  | $$      
| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$        |  $$$$/|  $$$$$$/      
|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/         \___/   \______/       
                                                                                                       
                                                                                                       
                                                                                                       
  /$$$$$$                               /$$                 /$$                 /$$               /$$  
 /$$__  $$                             | $$                | $$                | $$             /$$$$  
| $$  \ $$  /$$$$$$  /$$$$$$   /$$$$$$$| $$  /$$$$$$       | $$        /$$$$$$ | $$$$$$$       |_  $$  
| $$  | $$ /$$__  $$|____  $$ /$$_____/| $$ /$$__  $$      | $$       |____  $$| $$__  $$        | $$  
| $$  | $$| $$  \__/ /$$$$$$$| $$      | $$| $$$$$$$$      | $$        /$$$$$$$| $$  \ $$        | $$  
| $$  | $$| $$      /$$__  $$| $$      | $$| $$_____/      | $$       /$$__  $$| $$  | $$        | $$  
|  $$$$$$/| $$     |  $$$$$$$|  $$$$$$$| $$|  $$$$$$$      | $$$$$$$$|  $$$$$$$| $$$$$$$/       /$$$$$$
 \______/ |__/      \_______/ \_______/|__/ \_______/      |________/ \_______/|_______/       |______/
                                                                                                       
                                                                                                       
"""


def init_s(key):
    permS = []
    for x in range(256):
        permS.append(x)
    j = 0
    for x in range(256):
        j = (j+permS[x]+key[x % 16]) % 256
        temp = permS[x]
        permS[x] = permS[j]
        permS[j] = temp
    return permS


def encrypt(S, mes):
    x = 0
    y = 0
    mes = bytearray(mes, "utf_8")
    cipher = ""
    stream = bytearray()
    for z in range(len(mes)):
        x = (x+1) % 256
        y = (y+S[x]) % 256
        temp = S[x]
        S[x] = S[y]
        S[y] = temp
        stream.append(S[(S[x]+S[y]) % 256])
        op = str(hex(mes[z] ^ stream[z]))
        if len(op) % 2 != 0:
            cipher += "0"+op[2:]
        else:
            cipher += op[2:]
    return cipher


mask = "abcdefghijklmnopqrstuvwxy"
mestomask = {}
masktomes = {}
for x in range(len(mask)):
    mestomask[message[x]] = mask[x]
    masktomes[mask[x]] = message[x]


def permute(maskmes):
    out = ""
    for x in maskmes:
        out += masktomes[x]
    return out


print(banner)
while True:
    print("Enter a permutation of \"abcdefghijklmnopqrstuvwxy\" and I'll encrypt the corresponding message! ")
    i = input()
    if len(i) == len(mask) and set(i) == set(mask):
        em = permute(i)
        key = urandom(16)
        tS = init_s(key)
        ct = encrypt(tS, em)
        print(ct)
