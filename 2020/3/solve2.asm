; solve2.asm
; toboggan trajectory solution part 2
section         .data

    x_array         dq      3, 1, 5, 7, 1
    y_array         dq      1, 1, 1, 1, 2

section         .bss
    bufStart        resq    1
    indexSize       resq    1
    rowSize         resq    1

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
    mov [indexSize], r9     ; number of rows
    xor r10, r10            ; number of columns

    ; change newlines to nulls and store each index on the stack
    mov rcx, rsi
    push rdi
l1:
    mov rax, [rdi]
    cmp al, 0xa
    jne end1

    mov byte [rdi], 0
    inc qword [indexSize]
    mov rbx, rdi
    inc rbx
    push rbx
    cmp qword [indexSize], 1
    jne end1
    mov qword [rowSize], r10

end1:
    inc rdi
    inc r10
    loop l1

execute:        ; call slope(terrain_array, x, y)
    mov r12, 0
    mov r13, 1
l3:
    mov rdi, rsp
    mov rsi, [x_array + r12 * 8]
    mov rdx, [y_array + r12 * 8]
    call slope
    mul r13
    mov r13, rax
    cmp r12, 4
    je done
    inc r12
    jmp l3
    

done:   ; fix stack and set return value to rax
    mov rax, 8
    mov rbx, [indexSize]
    mul rbx
    add rsp, rax

    mov rax, r13

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


; slope(terrain_array, x, y)
; rdi = terrain_array
; rsi = x
; rdx = y
slope:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 0x8

    ; set arguments
    mov r9, rdi                 ; terrain array start
    mov r10, rsi                ; x value
    mov r11, rdx                ; y value

    ; loop through each index, check for '#'
    mov r12, 0
    mov r13, 0
    mov r15, 0
l2:
    add r12, r11
    add r13, r10
    cmp r12, qword [indexSize]
    jge doneSlope
    mov rax, r13
    mov rdx, 0
    div qword [rowSize]         ; use div to recycle through row
    mov r8, rdx

    ; get position value
    mov rbx, [indexSize]
    sub rbx, r12
    mov rax, 8
    mul rbx
    mov rax, [r9 + rax]      ; move row to rax
    mov rax, [rax + r8]            ; move char to rax

    ; check if we hit a tree
    cmp al, 0x23
    jne n1
    inc r15

n1:
    jmp l2

doneSlope:
    mov rax, r15

finSlope:
	add rsp, 0x8
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    ret