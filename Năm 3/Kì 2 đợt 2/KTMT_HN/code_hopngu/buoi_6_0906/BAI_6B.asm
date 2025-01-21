dseg segment
string1 db "Khong co gi quy hon doc lap tu do"
string2 db "Hom nay la mot ngay hop ly de ngu va chay deadline$";40 dup('$')
dseg ends
cseg segment
assume cs:cseg, ds:dseg, es: dseg
begin: mov ax, dseg
mov ds, ax
mov es, ax
cld ; chon chieu xu ly chuoi

mov cx, 33 ; so ky tu/so byte can di chuyen
lea si, string1 ; (DS:SI)--> dia chi cua chuoi nguon
lea di, string2 ; (ES:DI)--> dia chi cua chuoi dich
rep movsb ; di chuyen tung byte
mov ah, 09h
lea dx, string2
int 21h
mov ah,08h ; dung man hinh de xem ket qua
int 21h
mov ah, 4ch ; thoat ve Dos
int 21h
cseg ends
end begin