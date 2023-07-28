; 5/30/2023
; failed attempt

section .data
; consts
TRUE		equ	1
FALSE		equ	0

SUCCESS		equ	0
NOSUCCESS	equ	1

STDIN		equ	0
STDOUT		equ	1
STDERR		equ	2

SYS_read	equ	0
SYS_write	equ	1
SYS_open	equ	2
SYS_close	equ	3
SYS_fork	equ	57
SYS_exit	equ	60
SYS_creat	equ	85
SYS_time	equ	201

LF		equ	10
SPACE		equ	" "
NULL		equ	0
ESC		equ	27

; vars
A dd 0.0
B dd 0.0
i dd 0.0
j dd 0.0
k dd 0

c dd 0.0
d dd 0.0
e dd 0.0
f dd 0.0
g dd 0.0
h dd 0.0
D dd 0.0
l dd 0.0
m dd 0.0
n dd 0.0
t dd 0.0

x dd 0
y dd 0
o dd 0
N dd 0

incA dd 0.00004
incB dd 0.00002
incJ dd 0.014
incI dd 0.004
fltTwoPi dd 6.28

fltOne dd 1.0
fltTwo dd 2.0
fltFive dd 5.0

clearTerminal   db 0x1b, "[2J", LF, NULL
moveCursor		db 0x1b, "[H", LF, NULL
points			db ".,-~:;=!*#$@", NULL

section .bss
zee	resb 7040
bee resb 1760

putcharString resb 1

section .text

extern cos, sin

; void donut()
global donut
donut:
; clear terminal
    mov rdi, clearTerminal
    call printString

outerFor:
	; handle buffers
	mov rdi, bee
	mov rsi, 32
	mov rdx, 1760
	call memorySet
	mov rdi, zee
	mov rsi, 0
	mov rdx, 7040
	call memorySet

	; for loops
	forJ:
	movss xmm0, dword[j]
	ucomiss xmm0, dword[fltTwoPi]
	ja endForJ
		forI:
		movss xmm0, dword[i]
		ucomiss xmm0, dword[fltTwoPi]
		ja endForI

		; a ton of math
		; float c = sin(i);
		movss xmm0, dword[i]
		call sin
		movss dword[c], xmm0
		; float d = cos(j);
		movss xmm0, dword[j]
		call cos
		movss dword[d], xmm0
		; float e = sin(A);
		movss xmm0, dword[A]
		call sin
		movss dword[e], xmm0
		; float f = sin(j);
		movss xmm0, dword[j]
		call sin
		movss dword[f], xmm0
		; float g = cos(A);
		movss xmm0, dword[A]
		call cos
		movss dword[g], xmm0
		; float h = d + 2;
		movss xmm0, dword[d]
		addss xmm0, dword[fltTwo]
		movss dword[h], xmm0
		; float D = 1 / (c * h * e + f * g + 5);
		movss xmm0, dword[fltOne]

		movss xmm1, dword[c]
		mulss xmm1, dword[h]
		mulss xmm1, dword[e]
		movss xmm2, dword[f]
		mulss xmm2, dword[g]
		addss xmm1, xmm2
		addss xmm1, dword[fltFive]

		divss xmm0, xmm1
		movss dword[D], xmm0
		; float l = cos(i);
		movss xmm0, dword[i]
		call cos
		movss dword[l], xmm0
		; float m = cos(B);
		movss xmm0, dword[B]
		call cos
		movss dword[m], xmm0
		; float n = sin(B);
		movss xmm0, dword[B]
		call sin
		movss dword[n], xmm0
		; float t = c * h * g - f * e;
		movss xmm0, dword[c]
		mulss xmm0, dword[h]
		mulss xmm0, dword[g]
		movss xmm1, dword[f]
		mulss xmm1, dword[e]
		subss xmm0, xmm1
		movss dword[t], xmm0
		; int x = 40 + 30 * D * (l * h * m - t * n);
		movss xmm0, dword[l]
		mulss xmm0, dword[h]
		mulss xmm0, dword[m]
		movss xmm1, dword[t]
		mulss xmm1, dword[n]
		subss xmm0, xmm1
		mulss xmm0, dword[D]
		cvtss2si eax, xmm0
		mov r10d, 30
		mul r10d
		add eax, 40
		mov dword[x], eax
		mov rax, 0
		mov rdx, 0
		; int y= 12 + 15 * D * (l * h * n + t * m);
		movss xmm0, dword[l]
		mulss xmm0, dword[h]
		mulss xmm0, dword[n]
		movss xmm1, dword[t]
		mulss xmm1, dword[m]
		addss xmm0, xmm1
		mulss xmm0, dword[D]
		cvtss2si eax, xmm0
		mov r10d, 15
		mul r10d
		add eax, 12
		mov dword[y], eax
		mov rax, 0
		mov rdx, 0
		; int o = x + 80 * y;
		mov eax, dword[y]
		mov r10d, 80
		mul r10d
		mov r10d, dword[x]
		add eax, r10d
		mov dword[o], eax
		; int N = 8 * ( (f*e - c*d*g) * m - c*d*e - f*g - l*d*n);
		movss xmm0, dword[f]
		mulss xmm0, dword[e]
		movss xmm1, dword[c]
		mulss xmm1, dword[d]
		mulss xmm1, dword[g]
		subss xmm0, xmm1
		mulss xmm0, dword[m]
		movss xmm1, dword[c]
		mulss xmm1, dword[d]
		mulss xmm1, dword[e]
		subss xmm0, xmm1
		movss xmm1, dword[f]
		mulss xmm1, dword[g]
		subss xmm0, xmm1
		movss xmm1, dword[l]
		mulss xmm1, dword[d]
		mulss xmm1, dword[n]
		subss xmm0, xmm1
		cvtss2si eax, xmm0
		mov r10d, 8
		mul r10d
		mov dword[N], eax
		mov rax, 0
		mov rdx, 0
		; if(22 > y && y > 0 && x > 0 && 80 > x && D > z[o]) {
        ;     z[o] = D;
        ;     b[o] = ".,-~:;=!*#$@"[N > 0 ? N : 0];
        ; }
		mov eax, dword[y]
		cmp eax, 22
		jge notIf
		cmp eax, 0
		jle notIf
		mov eax, dword[x]
		cmp eax, 0
		jle notIf
		cmp eax, 80
		jge notIf
		mov r10, 0
		mov r11, 0
		mov r10d, dword[o]
		mov rbx, zee
		mov eax, dword[D]
		mov r11d, dword[rbx+r10]
		cmp eax, r11d
		jle notIf
		
		mov dword[rbx+r10], eax

		mov eax, dword[N]
		cmp eax, 0
		jg keepN
		mov eax, 0
		keepN:
		mov r10, 0
		mov r11, 0
		mov rcx, points
		mov r10d, eax
		mov al, byte[rcx+r10]
		mov rbx, bee
		mov r11d, dword[o]
		mov byte[rbx+r11], al
		notIf:

		movss xmm0, dword[i]
		addss xmm0, dword[incI]
		movss dword[i], xmm0
		jmp forI
		endForI:
	movss xmm0, dword[j]
	addss xmm0, dword[incJ]
	movss dword[j], xmm0
	jmp forJ
	endForJ:

	; move cursor to top-left
	mov rdi, moveCursor
	call printString
	; for(k = 0; k < 1761; k++) {
	; 	putchar(k % 80 ? b[k] : 10);
	; 	A += 0.00004;
	; 	B += 0.00002;
	; }
	mov ecx, 0
	theKLoop:
	mov eax, ecx
	mov edx, 0
	mov r10d, 80
	div r10d
	cmp edx, 0
	je putZero
	mov rbx, bee
	mov r10d, ecx
	mov al, byte[rbx+r10]
	mov byte[putcharString], al
	jmp notPutZero
	putZero:
	mov byte[putcharString], 10
	notPutZero:
	mov rdi, putcharString
	call printString

	movss xmm0, dword[A]
	addss xmm0, dword[incA]
	movss dword[A], xmm0

	movss xmm0, dword[B]
	addss xmm0, dword[incB]
	movss dword[B], xmm0

	inc ecx
	cmp ecx, 1761
	jb theKLoop

	jmp outerFor
endOuterFor:
donutDone:
    ret

; memset in x86
; rdi - arr addr
; rsi - char
; rdx - count
global memorySet
memorySet:
	mov al, sil
	mov rsi, 0

memSetLoop:
	mov byte[rdi+rsi], al
	inc rsi
	cmp rsi, rdx
	jl memSetLoop

	ret



; Credit to Dolly Jorgensen
global	printString
printString:
	push	rbx

; -----
;  Count characters in string.

	mov	rbx, rdi			; str addr
	mov	rdx, 0
strCountLoop:
	cmp	byte [rbx], NULL
	je	strCountDone
	inc	rbx
	inc	rdx
	jmp	strCountLoop
strCountDone:

	cmp	rdx, 0
	je	prtDone

; -----
;  Call OS to output string.

	mov	rax, SYS_write			; system code for write()
	mov	rsi, rdi			; address of characters to write
	mov	rdi, STDOUT			; file descriptor for standard in
						; EDX=count to write, set above
	syscall					; system call

; -----
;  String printed, return to calling routine.

prtDone:
	pop	rbx
	ret
