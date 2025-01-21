DSEG SEGMENT   
   chuoi DB  100 DUP(0) 
   inthuong DB 100 DUP(0)
   inhoa DB 100 DUP (0)
   kq DB 10,13,'Ket qua: $'
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
CMP AL,20h ;check dau space
JE dau_trang
CMP AL, 'Z'
JBE chu_hoa;chu hoa
JA chu_thuong;chu thuong
next:
MOV chuoi[SI], AL
INC SI
JMP LAP

dau_trang:
;nem vao string hoa
mov inhoa[SI],AL
;nem vao string thuong
mov inthuong[SI],AL
jmp next


chu_hoa: 
;nem vao string hoa
mov inhoa[SI],AL
;day la chu hoa, convert thanh chu thuong
ADD AL, 20h
;nem vao string thuong
mov inthuong[SI],AL
jmp next

chu_thuong: 
;nem vao string thuong
mov inthuong[SI],AL
;day la chu thuong, convert thanh chu hoa
SUB AL, 20h
;nem vao string hoa
mov inhoa[SI],AL

jmp next


STOP: ;co duoc chuoi
mov ah, 09h ; In cau thong bao ra man hinh
lea dx, kq
int 21h

mov BX,SI ;cat tam
;in chuoi thuong

mov CX,SI
INC CX
mov SI,0
mov ah,02h
L1:
    mov DL,inthuong[SI]
    int 21h
    inc SI
loop L1

;in chuoi hoa
mov SI,BX
mov CX,SI
INC CX
mov SI,0
mov ah,02h
L2:
    mov DL,inhoa[SI]
    int 21h
    inc SI
loop L2
  
mov ah,08h
int 21h
mov ah, 4Ch ; tro ve he dieu hanh
int 21h
CSEG ENDS
END start
