; aoc.asm
; Setup program to solve.  Read file and move it to memory.  Then call solve1 and solve2
section         .data
    inputFile       db      "./input", 0

    numfmt          db      "%d", 10, 0

    EXIT_SUCCESS    equ     0
    SYS_exit        equ     60


section         .bss
    stat            resb    144
    fileHandle      resq    1
    bufAddr1        resq    1
    bufAddr2        resq    1

struc STAT
    .st_dev         resq 1
    .st_ino         resq 1
    .st_nlink       resq 1
    .st_mode        resd 1
    .st_uid         resd 1
    .st_gid         resd 1
    .pad0           resb 4
    .st_rdev        resq 1
    .st_size        resq 1
    .st_blksize     resq 1
    .st_blocks      resq 1
    .st_atime       resq 1
    .st_atime_nsec  resq 1
    .st_mtime       resq 1
    .st_mtime_nsec  resq 1
    .st_ctime       resq 1
    .st_ctime_nsec  resq 1
endstruc

extern malloc
extern free
extern printf
extern memcpy

extern solve1
extern solve2


section         .text
global _start
_start:
	push rbp
	mov rbp, rsp
	push rbx
	push r15
	push r14
	push r13
	push r12
	sub rsp, 8

main:
	; get file size
	mov rax, 4
    mov rdi, inputFile
    mov rsi, stat
    syscall

    ; allocate memory for file contents
    mov rdi, qword [stat + STAT.st_size]
    call malloc
    mov [bufAddr1], rax
    mov rdi, qword [stat + STAT.st_size]
    call malloc
    mov [bufAddr2], rax

    ; open file
    mov rax, 2          ; syscall open
    mov rdi, inputFile
    mov rsi, 0          ; O_RDONLY
    syscall
    mov [fileHandle], rax

    ; read from file
    mov rax, 0
    mov rdi, [fileHandle]
    mov rsi, [bufAddr1]
    mov rdx, qword [stat + STAT.st_size]
    syscall

    ; close file
    mov rax, 3
    mov rdi, [fileHandle]
    syscall

    ; copy mem to buffer 2
    mov rdi, [bufAddr2]
    mov rsi, [bufAddr1]
    mov rdx, qword [stat + STAT.st_size]
    call memcpy

    ; run solve1(buffer, buf_size)
    mov rdi, [bufAddr1]
    mov rsi, qword [stat + STAT.st_size]
    call solve1

    ; print answer
    mov rdi, numfmt
    mov rsi, rax
    xor rax, rax
    call printf

    ; run solve2(buffer, buf_size)
    mov rdi, [bufAddr2]
    mov rsi, qword [stat + STAT.st_size]
    call solve2

    ; print answer
    mov rdi, numfmt
    mov rsi, rax
    xor rax, rax
    call printf

    ; free memory
    mov rdi, [bufAddr1]
    call free
    mov rdi, [bufAddr2]
    call free

fin:
	add rsp, 8
	pop r12
	pop r13
	pop r14
	pop r15
	pop rbx
	mov rsp, rbp
	pop rbp
    mov rax, SYS_exit
    mov rdi, EXIT_SUCCESS
    syscall