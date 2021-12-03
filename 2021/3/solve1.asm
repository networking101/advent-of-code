; solve1.asm
; binary boarding solution part 1
section         .data

section         .bss
    bufStart        resq    1
    indexSize       resq    1

	bitSize			resq	1
	bitPositions	resd	12

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
	mov rcx, rsi
	mov r12, rdi
l1:
	cmp byte [rdi], 0xa
	jne newline
	dec rbx
	mov qword [bitSize], rbx
	mov rbx, 0
	mov byte [rdi], 0
	push r12
	inc qword [indexSize]
	mov r12, rdi
	inc r12

newline:
	inc rbx
	inc rdi
	loop l1

solve:					; for each index add the bit into the bitPositions array
	mov rcx, 0
	pop rdi
l2:
	cmp rcx, qword [bitSize]
	je next
	movzx rax, byte [rdi + rcx]
	sub rax, 0x30
	add dword [bitPositions + rcx * 4], eax
	inc rcx
	jmp l2

next:
	mov rcx, 0
	pop rdi
	cmp rbp, rsp
	je findGamma
	jmp l2

findGamma:				; calculate the gama value.  Store in r15
	mov r15, 0
	mov rcx, 0
	mov r14, qword [indexSize]
	shr r14, 1			; find the mid point of the index size.  We will use r14 to decide if we set the bit or not
l3:
	cmp rcx, qword [bitSize]
	je findEpsilon
	shl r15, 1
	cmp dword [bitPositions + rcx * 4], r14d
	jl back
	inc r15
back:
	inc rcx
	jmp l3

findEpsilon:
	mov rax, r15
	not rax
	mov rbx, 0
	mov rcx, qword [bitSize]
lmask:
	shl rbx, 1
	inc rbx
	loop lmask

	and rax, rbx
	mul r15

fin:
    mov rsp, rbp
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	pop rbp
    ret