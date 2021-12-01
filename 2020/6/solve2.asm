; solve2.asm
; binary boarding solution part 2
section         .data

section         .bss
    bufStart        resq    1
    indexSize       resq    1

    alphabetarray   resb    26

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

main:
    mov qword [bufStart], rdi
    mov r12, rdi
    mov rcx, rsi
    mov r15, 0
l1:
    cmp byte [rdi], 0xa
    jne next
    cmp byte [rdi + 1], 0xa
    jne next

newIndex:
    mov word [rdi], 0x0
    push r12
    add rdi, 2
    dec rcx
    mov r12, rdi
    inc qword [indexSize]
    loop l1
    jmp continue

next:
    inc rdi
    loop l1

continue:
    mov byte [rdi - 1], 0
    push r12
    inc qword [indexSize]

findUnique:         ; go through all letters in an index and check for unique entries
    cmp qword [indexSize], 0
    je done
    pop rdx
    mov rbx, 1
l2:
    cmp byte [rdx], 0
    je nextIndex
    cmp byte [rdx], 0xa
    je newline
    movzx rax, byte [rdx]
    sub rax, 0x61
    inc byte [alphabetarray + rax]
    inc rdx
    jmp l2

newline:
    inc rbx
    inc rdx
    jmp l2

nextIndex:          ; loop through all alphabetarray. check if every answer on a question was correct. reset array to zero
    mov rax, 0
    mov rcx, 26
l3:
    cmp byte [alphabetarray + rcx - 1], bl
    jne notfound
    inc r15
notfound:
    mov byte [alphabetarray + rcx - 1], 0
    loop l3

    dec qword [indexSize]
    jmp findUnique

done:
    pop rax
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