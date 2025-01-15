INCLUDE	Irvine32.inc

ifndef X64
.686p ;Pentium Pro class of CPUs full instruction set
.XMM ;makes math calc faster, additional registers for vector ops
.model flat, C ; flat memory addressing, function conv agrees with C
endif

.data


.code
main	proc			; protected mode
	MOV eax 20			; store 20
	ADD eax 10			; add 10
	SUB eax 8			; subtract 8
	CALL WriteInt		; print
exit					; ends the program
main 	endp			; endpoint of (main) procedure
	end	main			; end program (main)