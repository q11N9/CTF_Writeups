inchuoi MACRO chuoi
MOV AH, 9h
LEA DX, chuoi
INT 21h
ENDM
DSEG SEGMENT
msg1 DB "Hay nhap 1 ky tu: $"
msg2 DB "Ma ASCII o dang Dec: $"
xdong DB 10, 13, �$�
kytu DB ?
DSEG ENDS
CSEG SEGMENT
ASSUME CS:CSEG, DS:DSEG
begin: MOV AX, DSEG
MOV DS, AX
inchuoi msg1
MOV AH, 01h
INT 21h
MOV kytu, AL ; c?t k� t? nh?n du?c
inchuoi xdong
inchuoi msg2
XOR AX, AX
MOV AL, kytu ; K� t? c?n in
CALL dec_out
MOV AH, 01
INT 21h
MOV AH, 4Ch ; thoat kh?i chuong tr�nh
INT 21h
dec_out PROC
XOR CX,CX ; CX d?m s? ch? s? th?p ph�n
MOV BX,10
chia10: XOR DX,DX
DIV BX ; DX:AX�BX => AX: Thuong, DX: s? du
PUSH DX ; C?t s? du v�o stack
INC CX
CMP AX, 0
JNZ chia10 ; n?u AX>0 th� chia ti?p cho 10
inra: MOV AH,2 ; in ra m�n h�nh
POP DX ; l?y ch? s? th?p ph�n
ADD DL,30h ; d?i th�nh k� s?
INT 21h
LOOP inra
RET
dec_out ENDP
CSEG ENDS
END begin

