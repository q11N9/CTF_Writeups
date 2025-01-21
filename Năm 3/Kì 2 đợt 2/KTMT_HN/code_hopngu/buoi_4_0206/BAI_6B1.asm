inchuoi MACRO chuoi
MOV AH, 9h
LEA DX, chuoi
INT 21h 
ENDM                 


DSEG SEGMENT
msg1 DB "Hay nhap 1 ky tu: $"
msg2 DB 10,13,"Ma ASCII o dang Hex: $"
xdong DB 10, 13, '$'
kytu DB ?

kytu1 DB ?
kytu2 DB ?
thunhat DB "Hay nhap ky tu dau tien: $"
thuhai DB 10,13,"Hay nhap ky tu thu hai: $"

DSEG ENDS
CSEG SEGMENT
ASSUME CS:CSEG, DS:DSEG
begin: MOV AX, DSEG
MOV DS, AX
inchuoi thunhat
MOV AH, 01h
INT 21h
;xac dinh ky tu la so hay chu
MOV BL, AL

CMP BL,3Ah ;xem la dang so hay chu
JB laso
CMP BL,40     
JA lachu
laso:
    SUB BL, 30h
    JMP next
lachu: 
    SUB BL, 38h
    JMP next
next: 
MOV kytu1, BL    

inchuoi thuhai
MOV AH, 01h
INT 21h
MOV BL,AL

CMP BL,3Ah ;xem la dang so hay chu
JB laso1
CMP BL,40     
JA lachu1
laso1:
    SUB BL, 30h
    JMP next1
lachu1: 
    SUB BL, 38h
    JMP next1
next1: 
ADD BL, kytu1

MOV kytu,BL

;ADD kytu2, kytu1
;MOV kytu, AL ; cat ky tu nhan duoc
;inchuoi xdong
inchuoi msg2
MOV BH, kytu ; Ký t? c?n in
CALL hex_out
MOV AH, 02 ; in ra ký t? h sau s? Hex
MOV DL, 'h'
INT 21h
MOV AH, 01
INT 21h
MOV AH, 4Ch ; thoat kh?i chuong trình
INT 21h
hex_out PROC
;MOV CX, 4
MOV CX,2
xuat:PUSH CX
MOV CL, 4
MOV DL, BH
SHR DL, CL
CMP DL, 09h
JA nhan
ADD DL, 30h ; Ð?i thành ký s? ‘0’-‘9’
JMP inra
Nhan: ADD DL, 37h ; Ð?i thành ký t? ‘A-‘F’
inra:MOV AH, 02h ; In ra màn hình ký t? dã d?i
INT 21h
SHL BX, CL ; Quay trái BX 4 bit
POP CX
LOOP xuat
RET
hex_out ENDP
CSEG ENDS
END begin
