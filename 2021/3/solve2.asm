; solve2.asm
; binary boarding solution part 2
section         .data
	;gamma			dw		0x496
	gamma			dw		22
	;epsilon			dw		0xb69
	epsilon			dw		9

section         .bss
    bufStart        resq    1
    indexSize       resq    1
	totSize			resq	1

	bitSize			resq	1
	bitPositions	resd	12
	oxyBuffer		resq	1
	co2Buffer		resq	1

extern atoi
extern strtol
extern malloc
extern free

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

main:			; convert each index to an int and store on the stack
    mov qword [bufStart], rdi
	mov rcx, rsi
	mov qword [totSize], rsi
	mov r12, rdi
l1:
	cmp byte [r12], 0xa
	jne newline
	dec rbx
	mov qword [bitSize], rbx
	mov rbx, 0
	mov byte [r12], 0
	mov rsi, 0
	mov rdx, 2
	push rcx
	call strtol
	pop rcx
	push rax
	inc qword [indexSize]
	mov rdi, r12
	inc rdi

newline:
	inc rbx
	inc r12
	loop l1

setBuffers:				; setup buffers for oxygen and C02.  Each index in the buffer will be 2 bytes
	mov rax, 2
	mul qword [indexSize]
	mov rbx, rax
	mov rdi, rax
	call malloc
	mov qword [oxyBuffer], rax
	mov rdi, rbx
	call malloc
	mov qword [co2Buffer], rax

fillBuffers:			; fill in the buffers for oxygen and C02
	mov rcx, qword [indexSize]
	mov r13, 0
l2:
	pop rax
	mov rbx, [oxyBuffer]
	mov word [rbx + r13*2], ax
	mov rbx, [co2Buffer]
	mov word [rbx + r13*2], ax
	inc r13
	loop l2

findOxygen:				; find the oxygen value
	mov r13, qword [bitSize]
l3:						; loop through each bit
	cmp r13, 0
	je doneOxygen
	mov rdi, [oxyBuffer]
	mov rsi, qword [indexSize]
	mov rdx, r13
	call oxy
	cmp rax, 0
	jne foundOxygen
	dec r13
	jmp l3

foundOxygen:
	mov r15, rax

doneOxygen:
	mov rdi, qword [oxyBuffer]
	call free
	
findCo2:				; find the C02 value
	mov r13, qword [bitSize]
l4:						; loop through each bit
	cmp r13, 0
	je doneCo2
	mov rdi, [co2Buffer]
	mov rsi, qword [indexSize]
	mov rdx, r13
	call co2
	cmp rax, 0
	jne foundCo2
	dec r13
	jmp l4

foundCo2:
	mul r15
	mov r15, rax

doneCo2:
	mov rdi, qword [co2Buffer]
	call free

done:
	mov rax, r15

fin:
    mov rsp, rbp
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	pop rbp
    ret


	;3430428
	;3431602

; oxy(oxyBuffer, bufSize, bit)
; rdi - buffer containing index values
; rsi - size of the buffer
; rdx - bit we are currently checking
oxy:
	push rbp
	push rbx
	push r15
	push r14
	push r13
	push r12
    mov rbp, rsp

oxymain:
	mov r12, rdi			; buffer start
	mov r14, 0				; number of found values
	mov r15, 0				; number of 1 bits
	mov rbx, 1
	mov rcx, rdx
	shl rbx, cl
	mov rcx, 0
	shr rbx, 1				; mask to check

oxyl1:						; go through and count how many have the check bit set
	cmp word [rdi + rcx*2], 0
	je oxybackl1
	mov ax, word [rdi + rcx*2]
	and ax, bx
	cmp ax, 0
	je oxynobitl1
	inc r15

oxynobitl1:
	inc r14

oxybackl1:
	inc rcx
	cmp rcx, rsi
	je oxycheck
	jmp oxyl1

oxycheck:					; if we have more bits set than no bits, we need to filter the array to only bits set
	sub r14, r15
	cmp r15, r14
	jge oxysetbit
	jmp oxynosetbit

oxysetbit:					; filter the array to only bits set
	mov rcx, 0
	mov r14, 0				; keep track of new values
oxyl2:
	cmp word [rdi + rcx*2], 0
	je oxybackl2
	mov ax, word [rdi + rcx*2]
	and ax, bx
	cmp ax, 0
	jne oxyfoundbs
	mov word [rdi + rcx*2], 0
	jmp oxybackl2

oxyfoundbs:
	inc r14

oxybackl2:
	inc rcx
	cmp rcx, rsi
	je oxydone
	jmp oxyl2

oxynosetbit:				; filter the array to only no bits set
	mov rcx, 0
	mov r14, 0				; keep track of new values
oxyl3:
	cmp word [rdi + rcx*2], 0
	je oxybackl3
	mov ax, word [rdi + rcx*2]
	and ax, bx
	cmp ax, 0
	je oxyfoundnbs
	mov word [rdi + rcx*2], 0
	jmp oxybackl3

oxyfoundnbs:
	inc r14

oxybackl3:
	inc rcx
	cmp rcx, rsi
	je oxydone
	jmp oxyl3

oxydone:
	cmp r14, 1
	je oxyfindresult
	mov rax, 0
	jmp oxyfin

oxyfindresult:
	mov rcx, 0
oxyl4:
	cmp word [rdi + rcx*2], 0
	je oxybackl4
	movzx rax, word [rdi + rcx*2]
	jmp oxyfin
oxybackl4:
	inc rcx
	jmp oxyl4


oxyfin:
    mov rsp, rbp
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	pop rbp
    ret


; co2(oxyBuffer, bufSize, bit)
; rdi - buffer containing index values
; rsi - size of the buffer
; rdx - bit we are currently checking
co2:
	push rbp
	push rbx
	push r15
	push r14
	push r13
	push r12
    mov rbp, rsp

co2main:
	mov r12, rdi			; buffer start
	mov r14, 0				; number of found values
	mov r15, 0				; number of 1 bits
	mov rbx, 1
	mov rcx, rdx
	shl rbx, cl
	mov rcx, 0
	shr rbx, 1				; mask to check

co2l1:						; go through and count how many have the check bit set
	cmp word [rdi + rcx*2], 0
	je co2backl1
	mov ax, word [rdi + rcx*2]
	and ax, bx
	cmp ax, 0
	je co2nobitl1
	inc r15

co2nobitl1:
	inc r14

co2backl1:
	inc rcx
	cmp rcx, rsi
	je co2check
	jmp co2l1

co2check:					; if we have more bits set than no bits, we need to filter the array to only bits set
	sub r14, r15
	cmp r15, r14
	jl co2setbit
	jmp co2nosetbit

co2setbit:					; filter the array to only bits set
	mov rcx, 0
	mov r14, 0				; keep track of new values
co2l2:
	cmp word [rdi + rcx*2], 0
	je co2backl2
	mov ax, word [rdi + rcx*2]
	and ax, bx
	cmp ax, 0
	jne co2foundbs
	mov word [rdi + rcx*2], 0
	jmp co2backl2

co2foundbs:
	inc r14

co2backl2:
	inc rcx
	cmp rcx, rsi
	je co2done
	jmp co2l2

co2nosetbit:				; filter the array to only no bits set
	mov rcx, 0
	mov r14, 0				; keep track of new values
co2l3:
	cmp word [rdi + rcx*2], 0
	je co2backl3
	mov ax, word [rdi + rcx*2]
	and ax, bx
	cmp ax, 0
	je co2foundnbs
	mov word [rdi + rcx*2], 0
	jmp co2backl3

co2foundnbs:
	inc r14

co2backl3:
	inc rcx
	cmp rcx, rsi
	je co2done
	jmp co2l3

co2done:
	cmp r14, 1
	je co2findresult
	mov rax, 0
	jmp co2fin

co2findresult:
	mov rcx, 0
co2l4:
	cmp word [rdi + rcx*2], 0
	je co2backl4
	movzx rax, word [rdi + rcx*2]
	jmp co2fin
co2backl4:
	inc rcx
	jmp co2l4


co2fin:
    mov rsp, rbp
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	pop rbp
    ret