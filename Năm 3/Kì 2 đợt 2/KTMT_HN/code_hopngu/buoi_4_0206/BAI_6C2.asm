                     DSEG SEGMENT   
   S1 DW 0 
   S2 DW 0
   S3 DW 0
   inputS1 DW 10,13,'S1: $'
   inputS2 DW 10,13,'S2: $'
   kq DW 10,13,'Hien tai: $'
DSEG ENDS  
CSEG SEGMENT
ASSUME CS: CSEG, DS: DSEG
start:
mov ax, DSEG
mov ds, ax
MOV SI, 0 ; chi so mang
MOV CX, 100 ; do dai mang max


mov ah, 09h ; In cau thong bao ra man hinh
lea dx, inputS1
int 21h
L1: 
MOV AH, 1 ; nhap ky tu
INT 21H
CMP AL,0Dh ;check dau enter
JE INPUT_S2
SUB AL, 30h
MOV AH, 0
MOV CX, AX   ;luu tam sang CX
MOV AX, S1   
MOV BX, 10
MUL BX ;AX = AX*BX
ADD AX,CX
MOV S1, AX
JMP L1

INPUT_S2:
mov ah, 09h ; In cau thong bao ra man hinh
lea dx, inputS2
int 21h
L2: 
MOV AH, 1 ; nhap ky tu
INT 21H
CMP AL,0Dh ;check dau enter
JE NEXT
SUB AL, 30h
MOV AH, 0
MOV CX, AX   ;luu tam sang CX
MOV AX, S2   
MOV BX, 10
MUL BX ;AX = AX*BX
ADD AX,CX
MOV S2, AX
JMP L2

NEXT: ;xu ly tu mang thanh so 
MOV AX, S1
MOV BX, S2
ADD S3, AX
ADD S3, BX
mov ah, 09h ; In cau thong bao ra man hinh
lea dx, kq
int 21h
mov ah, 2h
mov dx, s3 ;hien tai S3 dang giu gia tri dec ket qua
int 21h
  
mov ah,08h
int 21h
mov ah, 4Ch ; tro ve he dieu hanh
int 21h
CSEG ENDS
END start
