#!/usr/bin/env python2.7
from pwn import *
from collections import Counter

HOST = "127.0.0.1"
PORT = 9999


initial_permutation = "abcdefghijklmnopqrstuvwxy"
current_permutation = ""
flag = ""
for j in range(0, 25):
    r = remote(HOST, PORT)
    result = ""
    current_permutation = list(initial_permutation)
    current_permutation[1] = current_permutation[j]
    current_permutation[j] = "b"
    for i in range(6000):
        r.recv()
        r.sendline(''.join(current_permutation))
        letter = r.recvline().strip().decode("hex")[1]
        result += letter
        print("%d--%s" % (i, letter))
    char, occur = Counter(result).most_common(1)[0]
    log.success("Current flag : %s" % (flag+char))
    flag += char
    r.close()
    sleep(3)
log.success(flag)
