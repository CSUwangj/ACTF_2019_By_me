from Crypto import Random
from Crypto.Util import Counter
from Crypto.Cipher import AES
import binascii
import array

BLOCK_SIZE = 16


def encrypt(message, key):
    aes = AES.new(key, AES.MODE_CTR, counter=Counter.new(128))
    return str(binascii.b2a_hex(aes.encrypt(message)))[2:-1]


if __name__ == "__main__":
    key = Random.new().read(BLOCK_SIZE)
    o = open("cipher", "w")
    i = open("plaintext", "r")
    pt = i.read()
    i.close()
    o.write(encrypt(pt, key)+"\n")
    i = open("flag", "r")
    pt = i.read()
    i.close()
    o.write(encrypt(pt, key))
    o.close()
