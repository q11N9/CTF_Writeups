
DSEG SEGMENT
tenfile db "E:\emu8086\emu8068_loca\emu8086\MyBuild\data.txt",0
thefile dw ?
DSEG ENDS
CSEG SEGMENT
ASSUME cs:cseg, ds:dseg
begin: mov ax, dseg
mov ds, ax
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

