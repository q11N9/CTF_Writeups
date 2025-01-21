DSEG SEGMENT
   A DB  100 DUP(15)

DSEG ENDS
CSEG SEGMENT
ASSUME CS: CSEG, DS: DSEG
start:
mov ax, DSEG
mov ds, ax
  MOV SI, 0 ; ch? s? m?ng
MOV CX, 10 ; s? l?n l?p
LAP: MOV AH, 1 ; nh?p ký t?
INT 21H
MOV A[SI], AL
INC SI
CMP SI,10
JB LAP

CSEG ENDS
END start
