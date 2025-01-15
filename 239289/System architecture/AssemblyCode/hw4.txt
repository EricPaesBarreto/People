INCLUDE	Irvine32.inc

ifndef X64
.686p ;Pentium Pro class of CPUs full instruction set
.XMM ;makes math calc faster, additional registers for vector ops
.model flat, C ; flat memory addressing, function conv agrees with C
endif

.data
; Define strings, using BYTE character arrays using '0' as abreak condition (when the final byte is empty [null]) --> null terminated string
PromptMsgA	BYTE	"Enter a ", 0
PromptMsgB	BYTE	"Enter b ", 0
PromptMsgC	BYTE	"Enter c ", 0
PromptMsgX	BYTE	"Enter x ", 0
ResultMsg	BYTE 	"The answer is ", 0

; Define uninitializsed values [?], which will be used to store inputs. SDWORD --> signed double word (2's compliment)
a	SDWORD	?
b	SDWORD	?
cc	SDWORD	?
x	SDWORD	?

.code
main	proc
	; protected mode
	; Read a

	; move the address of Prompt message A into the register edx, which is used in the Irvine library to store output strings
	mov	edx, OFFSET PromptMsgA

	; outputs the value in the edx register to the terminal (console)
	call	WriteString

	; moves the value form the console, inputted by the user, into the register eax, reads signed integers
	call	ReadInt

	; moves the value from the eax register into the variable 'a' (which is in memory)
	mov	a, eax
	
	; Read b
	mov	edx, OFFSET PromptMsgB
	call	WriteString
	call	ReadInt
	mov	b, eax

	; Read cc
	mov	edx, OFFSET PromptMsgC
	call	WriteString
	call	ReadInt
	mov	cc, eax

	; Read x
	mov	edx, OFFSET PromptMsgX
	call	WriteString
	call	ReadInt
	mov	x, eax


	; here's where the maths starts :sunglasses:
	mov	eax, x		; 
	imul	x		; multiply value in eax by specified value (value stored in [x]) stores the result back in eax
	imul	a		; multiply value in eax by the value stored in variable [a] and store the result in the eax register
	mov	ebx, eax	; move the result in the eax register into the ebx register

	mov	eax, x		; move the value from variable x into the eax reg
	imul	b		; multiply eax [x] by [b] store in eax
	mov	ecx, eax	; move [x] * [b] into ecx

	mov	eax, cc		; move variable cc into the eax reg
	add	eax, ecx	; add the value from the ecx register (x * b) into the eax register [cc]
	add	eax, ebx	; add the value from the ebx register (x * x * a) into the eax register [cc + (x * b)]
					; now  the final value in the eax register should be a*x^2 + cc + x * b = x(a*x + b) + cc --> ax2 + bx + c

	mov	edx, OFFSET ResultMsg	; store the result after the final string in edx
	call	WriteString			; write the result string
	call	WriteInt			; write the result
	call	CrLf				; write a new line
	exit						; ends the program
main 	endp					; endpoint of (main) procedure
	end	main					; end program (main)
