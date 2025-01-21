dseg segment
;tenfile db "D:\solieu.txt",0
;tenfile2 db "D:\dati.txt",0
filedich db 10,13,'Ten file dich: $'
filenguon db 10,13,'Ten file nguon: $'
tenfile db 100 dup(0)
tenfile2 db 100 dup(0)

thefile dw ?
buffer db 251 dup ('$')
len db $ - buffer
dseg ends
cseg segment
assume cs:cseg, ds:dseg
begin: mov ax, dseg
mov ds, ax 
mov ah,9
lea dx,filenguon
int 21h
MOV SI, 0 ; chi so mang
MOV CX, 100 ; do dai mang max

LAP: 
    MOV AH, 1 ; nhap ky tu
    INT 21H
    CMP AL,0Dh ;check dau enter
    JE STOP
    MOV tenfile[SI], AL
    INC SI
JMP LAP

stop:
mov ah,9
lea dx,filedich
int 21h

MOV SI, 0 ; chi so mang
MOV CX, 100 ; do dai mang max

LAP2: 
    MOV AH, 1 ; nhap ky tu
    INT 21H
    CMP AL,0Dh ;check dau enter
    JE STOP2
    MOV tenfile2[SI], AL
    INC SI
JMP LAP2

stop2:


mov ah, 3dh ; mo tap tin da co
lea dx, tenfile
mov al, 2 ; thuoc tinh tap tin
int 21h
mov thefile, ax ; cat the file
mov ah, 3fh ; doc noi dung file vao vung dem
mov bx, thefile
lea dx, buffer
mov cx, 250 ; so byte can doc tu file da mo
int 21h

mov ah, 3eh ; dong tap tin
mov bx, thefile
int 21h

mov ah, 3ch ; tao tap tin moi
lea dx, tenfile2
mov cx, 0 ; tap tin co thuoc tinh binh thuong
int 21h
mov thefile, ax ; cat the file
mov ah, 40h ; ghi file
mov bx, thefile
xor cx, cx
mov cl, len
lea dx, buffer
int 21h
mov ah, 3eh ; dong tap tin
mov bx, thefile
int 21h
mov ah, 4ch ; thoat ve Dos
int 21h
cseg ends
end begin
