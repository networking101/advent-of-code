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

main:			; replace all newlines with nulls
	mov qword [bufStart], rdi
	mov rcx, rsi
l1:
	cmp byte [rdi], 0xa
	jne cont
	mov byte [rdi], 0
	inc qword [indexSize]
cont:
	inc rdi
	loop l1

count:
	mov rdi, qword [bufStart]
	mov r15, 0
	mov r14, 0
	mov r12, rdi
	call atoi
	mov r14, rax
	mov rdi, r12

l2:				; skip to the next null
	inc rdi
	cmp byte [rdi], 0
	jne l2
	
skip:			; check if the new index is higher than the last
	inc rdi
	mov r12, rdi
	call atoi
	mov rdi, r12
	cmp rax, r14
	jle noIncrease
	inc r15

noIncrease:		; reset and loop
	mov r14, rax
	dec qword [indexSize]
	cmp qword [indexSize], 0
	jne l2

done:
	mov rax, r15

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