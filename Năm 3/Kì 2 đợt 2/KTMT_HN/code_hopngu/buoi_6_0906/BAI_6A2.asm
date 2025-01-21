writeln macro bien1
    ;LOCAL bien1
    mov ah,09
    lea dx, bien1
    int 21h
    mov ah,02h
    mov dl, 0ah
    int 21h
    mov dl, 0dh
    int 21h
endm
dseg segment
tbao db "Chuong tring so sanh oldpass va newpass$"

tbao1 db "Haichuoi giong nhau $"
tbao2 db "Haichuoi khong giong nhau $"
x1:
oldpass dw "0123456789"
newpass dw "0123456789"     
size = ($ - x1) / 4
dseg ends
cseg segment
assume cs:cseg, ds:dseg, es: dseg
begin:
mov ax, dseg 

mov ds, ax
mov es, ax

;writeln tbao

cld ; chonchieu xu ly chuoi 

lea si, oldpass; (DS:SI)--> dia chi cua chuoi nguon
lea di, newpass; (ES:DI)--> dia chi cua chuoi dich
mov cx, size ; so ky tu/so byte can so sanh
repe cmpsw ; so sanh tung ky tu/byte
jnz khongbang  

;truong hop bang:
    writeln tbao1
    jmp thoat
    
khongbang:
    writeln tbao2
    jmp thoat
thoat:
mov ah,08h
int 21h
mov ah, 4ch
int 21h
cseg ends
end begin
