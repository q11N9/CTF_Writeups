                                         
DSEG SEGMENT
tenfile dw 'E:\emu8086\emu8068_loca\emu8086\MyBuild\'
;chuoi db 100 dup(?),0 
chuoi dw 0
kq dw 0

;tenfile = tenfile1 + tenfile2;
thefile dw ?

DSEG ENDS
CSEG SEGMENT
ASSUME cs:cseg, ds:dseg
begin: mov ax, dseg
mov ds, ax 

;lea si, tenfile 
mov si,0
LAP: 
    MOV AH, 8 ; nhap ky tu
    INT 21H
    CMP AL,0Dh ;check dau enter
    JE STOP
    mov ah,0
    MOV chuoi[SI], Ax
    INC SI
JMP LAP
;get array chuoi[SI] connect vao String tenfile

STOP:   
mov chuoi[si], 24h 
mov cx, chuoi


mov bx, tenfile
add bx, cx

mov tenfile, bx

mov ah, 09h ; In cau thong bao ra man hinh
mov dx,0
lea dx, tenfile 
int 21h 
 

mov ah, 3ch ; tao tap tin moi
lea dx, tenfile
mov cx, 0 ; thuoc tinh tap tin
int 21h
mov thefile, ax ; cat the file
mov ah, 3eh ; dong tap tin
mov bx, thefile
int 21h
 
mov ah, 4ch ; thoat ve Dos
int 21h
CSEG ENDS
END begin

