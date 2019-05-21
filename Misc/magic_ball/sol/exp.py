from pwn import *
from sets import Set
import sys


def round(io, weight):
    st = Set()
    mp_n2c = {}
    mp_c2n = {}
    cw = 0
    for i in range(3**weight):
        s = num_to_str(i, 3).rjust(weight, "0")
        if clockwise(s):
            st.add(s)
            mp_n2c[cw] = s
            mp_c2n[s] = cw
            cw += 1
    ans = ""
    for i in range(weight):
        log.info("  {} weight...".format(i))
        left = []
        right = []
        for ball in st:
            if ball[i] == "0":
                left.append(mp_c2n[ball])
            elif ball[i] == "2":
                right.append(mp_c2n[ball])
        io.recvuntil("side of the balance?")
        io.recvline()
        io.sendline(str(len(left)))
        io.recvline()
        io.sendline(" ".join(map(str, left)))
        io.recvline()
        io.sendline(str(len(right)))
        io.recvline()
        io.sendline(" ".join(map(str, right)))
        balance = io.recvline()
        if balance[4] == "l":
            ans += "0"
        elif balance[4] == "r":
            ans += "2"
        else:
            ans += "1"
    io.recvline()
    log.success("Clockwise index of ball is " + ans)
    if clockwise(ans):
        io.sendline(str(mp_c2n[ans]))
        io.recvline()
        io.sendline("h")
    else:
        io.sendline(str(mp_c2n[anticlockwise(ans)]))
        io.recvline()
        io.sendline("l")


def num_to_str(n, b, alphabet="0123456789abcdefghijklmnopqrstuvwxyz"):
    if not n:
        return "0"
    else:
        return num_to_str(n // b, b).lstrip("0") + alphabet[n % b]


def clockwise(s):
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            return ((s[i] == "0" and s[i + 1] == "1")
                    or (s[i] == "1" and s[i + 1] == "2")
                    or (s[i] == "2" and s[i + 1] == "0"))
    return False


def anticlockwise(s):
    return s.replace("0", "a").replace("2", "0").replace("a", "2")


io = ""
if len(sys.argv) > 1 and sys.argv[1] == "r":
    io = remote("140.82.19.20", 45128)
    # context.log_level = "debug"
else:
    io = process("./magic_ball.out")
    # context.log_level = "debug"

print io.recvuntil("PWN challenge.")

log.info("Round 0 with 2 weight...")
round(io, 2)
log.info("Round 1 with 3 weight...")
round(io, 3)
log.info("Round 2 with 7 weight...")
round(io, 7)
log.success(io.recvuntil("it~"))