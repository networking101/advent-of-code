; solve2.asm
; binary boarding solution part 2
section         .data

section         .bss
    bufStart        resq    1
    indexSize       resq    1

extern atoi

section         .text
global solve2
solve2:
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
	mov r15, 0				; final answer
	mov r14, 0				; last window sum
	mov r13, 0				; curr window sum progress
	mov r12, rdi			; buffer
	call atoi
	mov r13, rax
	mov rdi, r12

l2:					; skip to the next null
	inc rdi
	cmp byte [rdi], 0
	jne l2
	
skip:				; get number and add to r13. Check if we have 3 numbers
	inc rdi
	mov r12, rdi
	call atoi
	push rax
	mov rdi, r12
	add r13, rax
	cmp qword [rsp + 0x10], 0		; don't compare if we haven't gotten to 3 indexes yet
	je l2
	cmp r13, r14
	jle noIncrease
	inc r15
noIncrease:			; reset and loop
	mov r14, r13
	sub r13, qword [rsp + 0x10]
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