; solve1.asm
; binary boarding solution part 1
section         .data

section         .bss
    bufStart        resq    1
    indexSize       resq    1

	forward			resq	1
	depth			resq	1

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

main:
    mov qword [bufStart], rdi
	mov r12, rdi
	mov rcx, rsi
l1:
	cmp byte [rdi], 0xa
	jne nonewline
	mov byte [rdi], 0
	push r12
	mov r12, rdi
	inc r12
	inc qword [indexSize]

nonewline:
	inc rdi
	loop l1

position:			; calculate position
	mov qword [forward], 0
	mov qword [depth], 0
	mov r14, 0
	mov r13, 1
l2:					; loop through each index and check if the command is "forward", "down", or "up"
	mov r12, rbp
	mov rax, 8
	mul r13
	sub r12, rax
	mov r14, r12
	mov r12, qword [r12]
	cmp dword [r12], 0x77726f66				; forward
	je fwd
	cmp dword [r12], 0x6e776f64				; down
	je down
	cmp word [r12], 0x7075					; up
	je up

fwd:
	add r12, 8
	mov rdi, r12
	call atoi
	add qword [forward], rax
	jmp next

down:
	add r12, 5
	mov rdi, r12
	call atoi
	add qword [depth], rax
	jmp next

up:
	add r12, 3
	mov rdi, r12
	call atoi
	sub qword [depth], rax
	jmp next

next:			; move to next index
	inc r13
	cmp r14, rsp
	jne l2

done:			; multiply forward position by depth and move into return value
	mov rax, qword [forward]
	mov rbx, qword [depth]
	mul rbx

fin:
    mov rsp, rbp
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	pop rbp
    ret