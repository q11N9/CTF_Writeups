
dseg segment
string1 db "Hello World"
len db $ - string1
tenfile db "E:\emu8086\emu8068_loca\emu8086\MyBuild\data.txt",0
thefile dw ?
dseg ends
cseg segment
assume cs:cseg, ds:dseg
begin: mov ax, dseg
mov ds, ax
mov ah, 3ch ; tao tap tin moi
lea dx, tenfile
mov cx, 0 ; tap tin co thuoc tinh binh thuong
int 21h
mov thefile, ax ; cat the file
mov ah, 40h ; ghi file
mov bx, thefile
xor cx, cx
mov cl, len
lea dx, string1
int 21h
mov ah, 3eh ; dong tap tin
mov bx, thefile
int 21h
mov ah, 4ch ; thoat ve Dos
int 21h
cseg ends
end begin
