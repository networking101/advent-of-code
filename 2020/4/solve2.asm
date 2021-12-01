; solve2.asm
; passport processing solution part 2
section         .data
    eyecolors       dq      ":amb", ":blu", ":brn", ":gry", ":grn", ":hzl", ":oth"

section         .bss
    bufStart        resq    1
    indexSize       resq    1

extern atoi
extern strtol

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
    mov [bufStart], rdi
    inc qword [indexSize]

    ; organize data.  Replace all ' ' with '\n' and  '\n\n' with '\0\0'. Push each index onto the stack
    mov r8, rdi
    mov rcx, rsi
l1:
    cmp byte [r8], 0xa
    je firstnewline
    cmp byte [r8], 0x20
    je addNull
    jmp end1

firstnewline:
    cmp byte [r8 + 1], 0xa
    je secondnewline

addNull:
    mov byte [r8], 0
    ;mov byte [r8], 0x20
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

lbyr:       ; loop byr
    cmp dword [rdi], 0x3a727962
    je foundbyr
    inc rdi
fcbyr:      ; first check byr
    cmp byte [rdi + 2], 0
    jne lbyr
scbyr:      ; second check byr
    cmp byte [rdi + 3], 0
    jne lbyr

notfoundbyr:
    mov rax, 0          ; we didn't find the string
    jmp finbyr

foundbyr:
    add rdi, 4
    call atoi
    cmp rax, 1920
    jl notfoundbyr
    cmp rax, 2002
    jg notfoundbyr

    mov rax, 1

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

liyr:       ; loop iyr
    cmp dword [rdi], 0x3a727969
    je foundiyr
    inc rdi
fciyr:      ; first check iyr
    cmp byte [rdi + 2], 0
    jne liyr
sciyr:      ; second check iyr
    cmp byte [rdi + 3], 0
    jne liyr

notfoundiyr:
    mov rax, 0          ; we didn't find the string
    jmp finiyr

foundiyr:
    add rdi, 4
    call atoi
    cmp rax, 2010
    jl notfoundiyr
    cmp rax, 2020
    jg notfoundiyr

    mov rax, 1

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

leyr:       ; loop eyr
    cmp dword [rdi], 0x3a727965
    je foundeyr
    inc rdi
fceyr:      ; first check eyr
    cmp byte [rdi + 2], 0
    jne leyr
sceyr:      ; second check eyr
    cmp byte [rdi + 3], 0
    jne leyr

notfoundeyr:
    mov rax, 0          ; we didn't find the string
    jmp fineyr

foundeyr:
    add rdi, 4
    call atoi
    cmp rax, 2020
    jl notfoundeyr
    cmp rax, 2030
    jg notfoundeyr

    mov rax, 1

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

lhgt:       ; loop hgt
    cmp dword [rdi], 0x3a746768
    je testhgt
    inc rdi
fchgt:      ; first check hgt
    cmp byte [rdi + 2], 0
    jne lhgt
schgt:      ; second check hgt
    cmp byte [rdi + 3], 0
    jne lhgt

notfoundhgt:
    mov rax, 0
    jmp finhgt

testhgt:
    add rdi, 4
    cmp word [rdi + 2], 0x6e69
    je foundin
    cmp word [rdi + 3], 0x6d63
    je foundcm
    jmp notfoundhgt

foundin:
    call atoi
    cmp rax, 59
    jl notfoundhgt
    cmp rax, 76
    jg notfoundhgt
    mov rax, 1
    jmp finhgt

foundcm:
    call atoi
    cmp rax, 150
    jl notfoundhgt
    cmp rax, 193
    jg notfoundhgt
    mov rax, 1
    jmp finhgt

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

lhcl:       ; loop hcl
    cmp dword [rdi], 0x3a6c6368
    je validhcl
    inc rdi
fchcl:      ; first check hcl
    cmp byte [rdi + 2], 0
    jne lhcl
schcl:      ; second check hcl
    cmp byte [rdi + 3], 0
    jne lhcl

notfoundhcl:
    mov rax, 0
    jmp finhcl

validhcl:       ; run strtol() to check if hex value is valid.  Use endptr to make sure we got 6 hex characters.
    mov r12, rdi
    add rdi, 4
    cmp byte [rdi], 0x23
    jne notfoundhcl
    cmp byte [rdi + 7], 0x20
    jg notfoundhcl
    inc rdi
    push rax
    mov rsi, rsp
    mov rdx, 16
    call strtol
    mov rdi, [rsp]
    pop rdx             ; need to fix the stack
    sub rdi, r12
    cmp rdi, 0xb
    jne notfoundhcl

foundhcl:
    mov rax, 1

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

lecl:       ; loop ecl
    cmp dword [rdi], 0x3a6c6365
    je validateecl
    inc rdi
fcecl:      ; first check ecl
    cmp byte [rdi + 2], 0
    jne lecl
scecl:      ; second check ecl
    cmp byte [rdi + 3], 0
    jne lecl

notfoundecl
    mov rax, 0
    jmp finecl

foundecl:
    cmp byte [rdi + 4], 0x20
    jg notfoundecl
    mov rax, 1
    jmp finecl

validateecl:
    mov rcx, 7
    add rdi, 3
lecl2:
    mov rbx, [eyecolors + rcx * 8 - 8]
    cmp ebx, dword [rdi]
    je foundecl
    loop lecl2

    jmp notfoundecl

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

lpid:       ; loop pid
    cmp dword [rdi], 0x3a646970
    je validatepid
    inc rdi
fcpid:      ; first check pid
    cmp byte [rdi + 2], 0
    jne lpid
scpid:      ; second check pid
    cmp byte [rdi + 3], 0
    jne lpid

notfoundpid:
    mov rax, 0
    jmp finpid

validatepid:
    add rdi, 4
    mov rcx, 9
lpid2:
    cmp byte [rdi], 0x30
    jl notfoundpid
    cmp byte [rdi], 0x39
    jg notfoundpid
    inc rdi
    loop lpid2

    ;make sure we don't have more than 9 values
    cmp byte [rdi], 0x20
    jg notfoundpid

    mov rax, 1

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