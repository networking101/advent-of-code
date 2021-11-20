; solve2.asm
; password philosophy solution part 2
section         .data

section         .bss
    bufStart        resq    1
    indexSize       resq    1

    count           resq    1

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

main:
    mov [bufStart], rdi     ; original buffer start
    xor r9, r9
    mov [indexSize], r9     ; number of values

    ; change newlines to nulls    
    mov rcx, rsi
l1:
    mov rax, [rdi]
    cmp al, 0xa
    jne end1

    mov byte [rdi], 0
    mov r9, [indexSize]
    inc r9
    mov [indexSize], r9
end1:
    inc rdi
    loop l1


    ; loop through each index.  call valid(first_position, second_position, character, password)
    mov r12, [bufStart]
    xor r14, r14                ; keep track of index
lIndex:     ; loop through each index
    sub rsp, 0x18               ; character
                                ; second position
                                ; first position
    mov r13, r12
l2: ; save first position
    inc r13
    cmp byte [r13], 0x2d
    jne l2
    mov byte [r13], 0x0
    mov rdi, r12
    call atoi
    mov [rsp], rax
    inc r13
    mov r12, r13
l3: ; save second position
    inc r13
    cmp byte [r13], 0x20
    jne l3
    mov byte [r13], 0x0
    mov rdi, r12
    call atoi
    mov [rsp + 8], rax
    inc r13
    mov r12, r13
l4: ; save character
    mov byte [r13 + 1], 0x0
    xor rdi, rdi
    mov dil, [r13]
    mov [rsp + 0x10], rdi
    add r12, 3
l5: ; call valid
    mov rdi, [rsp]
    mov rsi, [rsp + 0x8]
    mov rdx, [rsp + 0x10]
    mov r10, r12
    call valid
    ; check if password is valid
    cmp rax, 1
    jne l6
    inc qword [count]                     ; increase valid count if password is valid

l6: ; move to next index
    inc r12
    cmp byte [r12], 0x0
    jne l6

    inc r14                         ; increase current index
    inc r12
    add rsp, 0x18
    cmp r14, [indexSize]
    jne lIndex

done:
    mov rax, [count]

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


; Function valid(first position, second position, character, password)
; Arguments:
; rdi = first position
; rsi = second position
; rdx = character
; r10 = password
valid:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 0x8            ; number of times found
    mov qword [rsp], 0x0

check1:
    cmp byte [r10 + rdi - 1], dl
    jne check2
    inc byte [rsp]

check2:
    cmp byte [r10 + rsi - 1], dl
    jne res
    inc byte [rsp]

res:
    mov rax, [rsp]
    and al, 0x1

finValid:
	add rsp, 0x8
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    ret