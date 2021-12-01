; solve2.asm
; binary boarding solution part 2
section         .data

section         .bss
    bufStart        resq    1
    indexSize       resq    1

	seats			resb	900
	foundseats		resb	1

extern atoi

section         .text
global solve2
solve2:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 0x8

main:               ; format input (replace '\n' with nulls)
    mov [bufStart], rdi
    mov rcx, rsi
    mov qword [indexSize], 0
l1:
    cmp byte [rdi], 0xa
    jne next
    inc qword [indexSize]
    mov byte [rdi], 0

next:
    inc rdi
    loop l1

startCheck:         ; loop through each index and calculate size
    mov rcx, qword [indexSize]
    mov rdi, [bufStart]
    mov r12, 0      ; curr index value
    mov r15, 0      ; max value
l2:                 ; The 3rd bit for 'F' and 'L' are set.  The 3rd bit for 'B' and 'R' are not.  We can use this to check if we need to
    movzx rax, byte [rdi]
    xor rax, 0xff
    and rax, 0x4
    shr rax, 2
    add r12, rax
    inc rdi
    cmp byte [rdi], 0
    je saveIndex
    shl r12, 1
    jmp l2

saveIndex:		; mark the seats array with the found ticket
    mov byte [seats + r12], 1
    cmp r12, r15
    jle notgreater
    mov r15, r12

notgreater:
    inc rdi
    mov r12, 0
    loop l2


findSeat:		; now we need to find our seat.  Skip through the first few indexs that we don't have tickets for.  Once we find the first ticket.  Look for ours.
	mov rcx, 0
	mov byte [foundseats], 0

l3:
	cmp byte [seats + rcx], 0
	je seat0
	mov byte [foundseats], 1
	jmp cont

seat0:
	cmp byte [foundseats], 0
	je cont
	mov rax, rcx
	jmp fin

cont:
	inc rcx
	jmp l3

fin:
	add rsp, 0x8
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    ret