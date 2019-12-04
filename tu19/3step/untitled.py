from pwn import*
context(os='linux')
context.log_level = 'DEBUG'
e =ELF("./3step")
io = process(e.path)
io.recvuntil("0x")
buf1_addr = int(io.recv(8),16)
io.recvuntil("0x")
buf_addr = int(io.recv(8),16)
print hex(buf_addr)
print hex(buf1_addr)
payload = ""
#io.sendline(payload)
io.interactive()