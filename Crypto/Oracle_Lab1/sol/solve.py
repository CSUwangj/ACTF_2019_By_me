#!/usr/bin/env python2.7
from pwn import *
from collections import Counter
import sys

HOST = "127.0.0.1"
PORT = 9999
if len(sys.argv) > 1 and sys.argv[1] == 'r':
    context.log_level = "debug"
    HOST = "140.82.19.20"
    PORT = 45126

initial_permutation = "abcdefghijklmnopqrstuvwxy"
current_permutation = ""
flag = ""
for j in range(0, 25):
    i = 0
    result = ""
    while i < 6000:
        try:
            r = remote(HOST, PORT)
            current_permutation = list(initial_permutation)
            current_permutation[1] = current_permutation[j]
            current_permutation[j] = "b"
            while i < 6000:
                r.recvuntil("sage!")
                r.recvline()
                r.sendline(''.join(current_permutation))
                letter = r.recvline().strip().decode("hex")[1]
                result += letter
                print("%d--%s" % (i, letter))
                i += 1
            char, occur = Counter(result).most_common(1)[0]
            log.success("Current flag : %s" % (flag + char))
            flag += char
            r.close()
            sleep(3)
        except IndexError as e:
            pass

log.success(flag)
