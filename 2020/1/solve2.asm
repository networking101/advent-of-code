; solve2.asm
;report repair solution part 2
section         .data

section         .bss
    bufStart        resq    1
    indexSize       resq    1

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
	sub rsp, 0x48   ; curr big loop index
                    ; curr med loop index
                    ; curr little loop index
                    ; big loop value
                    ; big loop value address
                    ; med loop value
                    ; med loop value address
                    ; little loop value
                    ; little loop value address


main:
    mov [bufStart], rdi     ; original buffer start
    xor r9, r9
    mov [indexSize], r9     ; number of values

    ; change newlines to nulls    
    mov rcx, rsi
loop1:
    mov rax, [rdi]
    cmp al, 0xa
    jne end1

    mov byte [rdi], 0
    mov r9, [indexSize]
    inc r9
    mov [indexSize], r9
end1:
    inc rdi
    loop loop1


    ; loop through each number (outer loop)
    mov qword [rsp + 0x40], 0             ; set curr big loop
    mov rcx, [indexSize]            ; set big loop condition
    mov r15, [bufStart]
bigloop:
    mov [rsp + 0x20], r15           ; set big loop address
    mov rdi, r15
    call atoi
    mov [rsp + 0x28], rax           ; set big loop value

    ; move to next value
loop2:
    inc r15
    cmp byte[r15], 0x0
    jne loop2

    inc r15
    mov rbx, [rsp + 0x40]           ; set curr med loop
    inc rbx
    mov [rsp + 0x38], rbx 

medloop:
    mov [rsp + 0x10], r15           ; set med loop address
    mov rdi, r15
    call atoi
    mov [rsp + 0x18], rax           ; set med loop value

    ; move to next value
loop5:
    inc r15
    cmp byte[r15], 0x0
    jne loop5

    inc r15
    mov rbx, [rsp + 0x38]           ; set curr little loop
    inc rbx
    mov [rsp + 0x30], rbx 

    ; loop through each number (inner loop)
littleloop:
    mov [rsp], r15                  ; set little loop address
    mov rdi, r15
    call atoi
    mov [rsp + 0x8], rax            ; set little loop value

    ; check if sum of big value and little value equals 2020
    mov rbx, [rsp + 0x8]
    add rbx, [rsp + 0x18]
    add rbx, [rsp + 0x28]
    cmp rbx, 2020
    je found

    ; not found, check if we are at the last index
    mov rbx, [rsp + 0x30]
    cmp rbx, [indexSize]
    je backmedloop

loop3:
    inc r15
    cmp byte [r15], 0x0
    jne loop3

    inc r15
    inc qword [rsp + 0x30]                ; set curr little loop
    jmp littleloop

backmedloop:
    ; check if we are at the last index
    mov rbx, [rsp + 0x38]
    mov r11, [indexSize]                    ; we need to subtract indexSize by 1 
    dec r11
    cmp rbx, r11
    je backbigloop

    mov r15, [rsp + 0x10]
loop6:
    inc r15
    cmp byte [r15], 0x0
    jne loop6

    inc r15
    inc qword [rsp + 0x38]
    jmp medloop

backbigloop:
    mov r15, [rsp + 0x20]
loop4:
    inc r15
    cmp byte [r15], 0x0
    jne loop4

    inc r15
    inc qword [rsp + 0x40]
    jmp bigloop                    ; jump to big loop if done with little loop


found:
    mov rax, [rsp + 0x8]
    mov rbx, [rsp + 0x28]
    mul rbx
    mov rbx, [rsp + 0x18]
    mul rbx


fin:
	add rsp, 0x48
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    ret

