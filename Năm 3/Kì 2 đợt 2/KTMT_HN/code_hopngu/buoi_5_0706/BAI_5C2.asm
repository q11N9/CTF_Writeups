dseg segment
tenfile db "D:\solieu.txt",0
tenfile2 db "D:\dati.txt",0
thefile dw ?
buffer db 251 dup ('$')
len db $ - buffer
dseg ends
cseg segment
assume cs:cseg, ds:dseg
begin: mov ax, dseg
mov ds, ax 

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
