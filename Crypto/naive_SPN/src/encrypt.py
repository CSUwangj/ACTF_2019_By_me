import os

from secret import flag, key

SZ = 8

# random.shuffle(range(256))
sbox = [87, 197, 234, 101, 164, 232, 32, 86, 212, 39, 77, 141, 255, 52, 198, 240, 103, 249, 13, 7, 71, 239, 216, 41, 119, 110, 148, 252, 21, 145, 222, 204, 73, 136, 38, 56, 229, 19, 49, 135, 36, 74, 120, 109, 12, 99, 160, 169, 217, 130, 98, 65, 100, 76, 115, 147, 158, 253, 191, 244, 213, 231, 140, 82, 117, 9, 54, 186, 178, 79, 61, 163, 200, 177, 126, 194, 248, 89, 97, 14, 25, 184, 208, 121, 187, 93, 16, 111, 170, 48, 230, 201, 153, 28, 254, 137, 46, 146, 193, 218, 70, 228, 245, 224, 241, 180, 171, 168, 4, 220, 189, 209, 106, 45, 196, 236, 242, 132, 215, 156, 66, 50, 84, 72, 90, 53, 42, 43, 127, 176, 185, 37, 17, 133, 6, 3, 102, 78, 179, 26, 123, 243, 173, 11, 1, 104, 44, 174, 207, 142, 15, 108, 31, 210, 85, 226, 143, 118, 91, 149, 35, 205, 22, 182, 150, 237, 165, 134, 18, 195, 172, 246, 95, 192, 116, 47, 60, 30, 227, 20, 202, 175, 80, 8, 29, 166, 24, 69, 0, 55, 159, 128, 68, 223, 219, 225, 92, 151, 105, 94, 63, 5, 10, 67, 129, 64, 33, 214, 40, 157, 83, 59, 122, 152, 154, 58, 203, 188, 139, 235, 124, 250, 51, 114, 144, 34, 190, 238, 183, 27, 107, 138, 211, 247, 96, 131, 113, 57, 206, 162, 2, 81, 75, 161, 125, 233, 112, 88, 181, 62, 23, 167, 199, 155, 251, 221]

def doxor(l1,l2):
    return [x[0]^x[1] for x in zip(l1,l2)]

def trans(blk):
    res = []
    for k in range(0, SZ, 8):
        bits = [bin(x)[2:].rjust(8,'0') for x in blk[k:k+8]]
        for i in range(8):
            res.append(int(''.join([x[i] for x in bits]),2))
    return res

def encrypt_block(pt, ks):
    cur = doxor(pt, ks[:SZ])
    cur = [sbox[x] for x in pt]
    cur = trans(cur)
    cur = [sbox[x] for x in pt]
    return cur

def encrypt(pt, k):
    x = SZ-len(pt)%SZ
    pt += chr(x)*x
    print(pt,len(pt))
    ct = ''
    for i in range(0, len(pt), SZ):
        res = encrypt_block([ord(x) for x in pt[i:i+SZ]], k)
        ct += doout(res)
    return ct

def doout(x):
    tmp = ''.join([hex(xx)[2:] for xx in x])
    if len(tmp) % 16:
        tmp = (16 - len(tmp) % 16) * "0" + tmp
    return tmp

# gen your own key for test
def genkeys():
    return map(ord, os.urandom(2*SZ))

if __name__ == "__main__":
    f = open("ciphertext", "w")
    ct = encrypt(flag, key)
    f.write(ct+"\n")
    # To save your time, I'll omit the interactive step and give you plain-cipher pairs directly
    # Hope you don't hit shift+enter
    for i in range(65536):
        pt = list(os.urandom(SZ))
        ct = encrypt_block(pt, key)
        f.write(doout(pt)+" "+doout(ct)+"\n")
    f.close()
