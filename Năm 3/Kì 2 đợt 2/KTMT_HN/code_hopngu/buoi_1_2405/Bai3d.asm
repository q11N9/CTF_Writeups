.MODEL SMALL 
.STACK 100
.DATA 
    A DW 1000
    B DW 100 
.CODE 
MAIN PROC 
    MOV AX, @data
	MOV DS, AX
 
    MOV AX, A 
    MOV BX, B 
    DIV BX ;ket qua o AX = 0Ah
MAIN ENDP
END MAIN
