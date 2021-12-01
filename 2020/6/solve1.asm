; solve1.asm
; binary boarding solution part 1
section         .data

section         .bss
    bufStart        resq    1
    indexSize       resq    1

    alphabetarray   resb    26

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
    push r12
    inc qword [indexSize]

findUnique:         ; go through all letters in an index and check for unique entries
    cmp qword [indexSize], 0
    je done
    pop rdx
l2:
    cmp byte [rdx], 0
    je nextIndex
    cmp byte [rdx], 0xa
    je found
    movzx rax, byte [rdx]
    sub rax, 0x61
    cmp byte [alphabetarray + rax], 0
    jne found
    inc r15
    inc byte [alphabetarray + rax]
found:
    inc rdx
    jmp l2

nextIndex:          ; loop through all alphabetarray and reset to 0
    mov rax, 0
    mov rcx, 26
l3:
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