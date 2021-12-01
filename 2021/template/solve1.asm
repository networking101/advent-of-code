; solve1.asm
; binary boarding solution part 1
section         .data

section         .bss
    bufStart        resq    1
    indexSize       resq    1

extern atoi

section         .text
global solve1
solve1:
	push rbp
	push rbx
	push r15
	push r14
	push r13
	push r12
    mov rbp, rsp
	sub rsp, 0x8

main:
    xor rax, rax

fin:
	add rsp, 0x8
    mov rsp, rbp
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	pop rbp
    ret