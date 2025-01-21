DSEG SEGMENT
tbao DB 10,13,'Xin chao $' 

chuoi DB 100 dup(0)
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


STOP: ;co duoc chuoi
mov ah, 09h ; In cau thong bao ra man hinh
lea dx, tbao
int 21h

mov BX,SI ;cat tam

mov CX,SI
INC CX
mov SI,0
mov ah,02h
L1:
    mov DL,chuoi[SI]
    int 21h
    inc SI
loop L1
  
mov ah,08h
int 21h
mov ah, 4Ch ; tro ve he dieu hanh
int 21h
CSEG ENDS
END start