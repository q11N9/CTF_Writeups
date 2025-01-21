.MODEL SMALL 
.STACK 100
.DATA
    ;3AB45Eh: 3Ah va 0B45Eh
    A DW 0B45Eh
    B DW 3Ah
    C DW 0A1h 
.CODE 
MAIN PROC 
    MOV AX, @data
	MOV DS, AX
 
    MOV AX, A 
    MOV DX, B 
    DIV C ;ket qua o AX = 5D58h
MAIN ENDP
END MAIN
