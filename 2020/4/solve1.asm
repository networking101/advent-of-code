; solve1.asm
; passport processing solution part 1
section         .data

section         .bss
    bufStart        resq    1
    indexSize       resq    1

extern atoi

section         .text
global solve1
solve1:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 0x8

main:
    mov [bufStart], rdi
    inc qword [indexSize]

    ; organize data.  Replace all '\n\n' with '\0\0' and push each index onto the stack
    mov r8, rdi
    mov rcx, rsi
l1:
    cmp byte [r8], 0xa
    je firstnewline
    jmp end1

firstnewline:
    cmp byte [r8 + 1], 0xa
    je secondnewline

addNull:
    mov byte [r8], 0x20
    jmp end1

secondnewline:
    mov byte [r8], 0
    mov byte [r8 + 1], 0
    push rdi
    inc r8
    dec rcx
    inc qword [indexSize]
    mov rdi, r8
    inc rdi

end1:
    inc r8
    loop l1
    push rdi

    mov r12, 0          ; index tracker
    mov r15, 0          ; result tracker
l2:
    ; check if passport is valid. valid(index address)
    mov rax, 8
    mul r12
    add rax, rsp
    mov rdi, [rax]
    call valid
    and rax, 1
    add r15, rax

end2:
    inc r12
    cmp qword [indexSize], r12
    je done
    jmp l2

    
done:   ; fix stack, move result to rax
    mov rax, [indexSize]
    mov rbx, 8
    mul rbx
    add rsp, rax

    mov rax, r15

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

; valid(index address)
; rdi = index address
valid:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 0x8

    mov r12, rdi
    mov r15, 0

    ; check birth year
    mov rdi, r12
    call chkbyr
    add r15, rax

    ; check issue year
    mov rdi, r12
    call chkiyr
    add r15, rax

    ; check expiration year
    mov rdi, r12
    call chkeyr
    add r15, rax

    ; check height
    mov rdi, r12
    call chkhgt
    add r15, rax

    ; check hair color
    mov rdi, r12
    call chkhcl
    add r15, rax

    ; check eye color
    mov rdi, r12
    call chkecl
    add r15, rax

    ; check passport id
    mov rdi, r12
    call chkpid
    add r15, rax

    mov rax, 1
    mov rcx, 3
donevalid:
    and rax, r15
    shr r15, 1
    loop donevalid

finvalid:
	add rsp, 0x8
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    ret

; chkbyr(index address)
; rdi = index address
chkbyr:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 0x8
    
    mov rax, 1

lbyr:       ; loop byr
    cmp dword [rdi], 0x3a727962
    je finbyr
    inc rdi
fcbyr:      ; first check byr
    cmp byte [rdi + 2], 0
    jne lbyr
scbyr:      ; second check byr
    cmp byte [rdi + 3], 0
    jne lbyr

    mov rax, 0          ; we didn't find the string

finbyr:
	add rsp, 0x8
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    ret

; chkiyr(index address)
; rdi = index address
chkiyr:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 0x8
    
    mov rax, 1

liyr:       ; loop iyr
    cmp dword [rdi], 0x3a727969
    je finiyr
    inc rdi
fciyr:      ; first check iyr
    cmp byte [rdi + 2], 0
    jne liyr
sciyr:      ; second check iyr
    cmp byte [rdi + 3], 0
    jne liyr

    mov rax, 0          ; we didn't find the string

finiyr:
	add rsp, 0x8
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    ret

; chkeyr(index address)
; rdi = index address
chkeyr:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 0x8
    
    mov rax, 1

leyr:       ; loop eyr
    cmp dword [rdi], 0x3a727965
    je fineyr
    inc rdi
fceyr:      ; first check eyr
    cmp byte [rdi + 2], 0
    jne leyr
sceyr:      ; second check eyr
    cmp byte [rdi + 3], 0
    jne leyr

    mov rax, 0          ; we didn't find the string

fineyr:
	add rsp, 0x8
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    ret

; chkhgt(index address)
; rdi = index address
chkhgt:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 0x8
    
    mov rax, 1

lhgt:       ; loop hgt
    cmp dword [rdi], 0x3a746768
    je finhgt
    inc rdi
fchgt:      ; first check hgt
    cmp byte [rdi + 2], 0
    jne lhgt
schgt:      ; second check hgt
    cmp byte [rdi + 3], 0
    jne lhgt

    mov rax, 0          ; we didn't find the string

finhgt:
	add rsp, 0x8
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    ret

; chkhcl(index address)
; rdi = index address
chkhcl:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 0x8
    
    mov rax, 1

lhcl:       ; loop hcl
    cmp dword [rdi], 0x3a6c6368
    je finhcl
    inc rdi
fchcl:      ; first check hcl
    cmp byte [rdi + 2], 0
    jne lhcl
schcl:      ; second check hcl
    cmp byte [rdi + 3], 0
    jne lhcl

    mov rax, 0          ; we didn't find the string

finhcl:
	add rsp, 0x8
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    ret

; chkecl(index address)
; rdi = index address
chkecl:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 0x8
    
    mov rax, 1

lecl:       ; loop ecl
    cmp dword [rdi], 0x3a6c6365
    je finecl
    inc rdi
fcecl:      ; first check ecl
    cmp byte [rdi + 2], 0
    jne lecl
scecl:      ; second check ecl
    cmp byte [rdi + 3], 0
    jne lecl

    mov rax, 0          ; we didn't find the string

finecl:
	add rsp, 0x8
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    ret

; chkpid(index address)
; rdi = index address
chkpid:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 0x8
    
    mov rax, 1

lpid:       ; loop pid
    cmp dword [rdi], 0x3a646970
    je finpid
    inc rdi
fcpid:      ; first check pid
    cmp byte [rdi + 2], 0
    jne lpid
scpid:      ; second check pid
    cmp byte [rdi + 3], 0
    jne lpid

    mov rax, 0          ; we didn't find the string

finpid:
	add rsp, 0x8
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    ret