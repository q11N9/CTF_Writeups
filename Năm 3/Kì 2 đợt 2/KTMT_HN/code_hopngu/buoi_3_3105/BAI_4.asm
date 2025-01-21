DSEG SEGMENT
   
   chuoi DB  100 DUP(0)
   length DB 10,13,'Do dai chuoi: $'
DSEG ENDS
CSEG SEGMENT
ASSUME CS: CSEG, DS: DSEG
start:
mov ax, DSEG
mov ds, ax
MOV SI, 0 ; chi so mang
MOV CX, 100 ; do dai mang max
LAP: MOV AH, 1 ; nhap ky tu
INT 21H
CMP AL,0Dh ;check dau enter
JE STOP
MOV chuoi[SI], AL
INC SI
JMP LAP

STOP:
mov ah, 09h ; In cau thong bao ra man hinh
lea dx, length
int 21h
;in KQ so dem
mov ah, 02h;
mov DX, SI ;hien tai dang bi in thanh ASCII
add DX,30h
int 21h
mov ah,08h
int 21h
mov ah, 4Ch ; tro ve he dieu hanh
int 21h
CSEG ENDS
END start
