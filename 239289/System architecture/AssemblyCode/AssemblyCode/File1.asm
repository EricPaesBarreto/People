INCLUDE Irvine32.inc
.386
.data
	arrayB BYTE 3h, 1h, 4h, 1h, 5h	; Create array (PI)
.code
main PROC
	mov ECX, SIZEOF arrayB		; Store in ECX array length
	mov ESI, OFFSET arrayB		; Store 0 (index) in ESI
	mov CL, 0h

	beginning:					; While ECX > 0
		mov BL, arrayB[ESI];	; Store the value of arrayB at position ESI in BX reg
		add CL, BL				; Add current value (BL reg) to sum (CL reg)
		inc ESI					; Increment ESI
	LOOP beginning				; GOTO beginning of loop, decrement ECX

	call DumpRegs
main ENDP
END main
