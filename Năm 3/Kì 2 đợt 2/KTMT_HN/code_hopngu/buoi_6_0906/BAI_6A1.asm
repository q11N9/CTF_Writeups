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
oldpass db "0123456789"
newpass db "0124456789"
tbao1 db "Haichuoi giong nhau $"
tbao2 db "Haichuoi khong giong nhau $"
dseg ends
cseg segment
assume cs:cseg, ds:dseg, es: dseg
begin: mov ax, dseg
mov ds, ax
mov es, ax

writeln tbao

mov cx,10 ;so ky tu/so byte can so
mov si,0
soTungKyTu:
    mov bl,oldpass[si]
    mov bh,newpass[si]
   CMP bl,bh 
   jne khongkhop 
   inc si
LOOP soTungKyTu
;khong nhay ra 'khongkhop' --> da khop
writeln tbao1
jmp thoat    

khongkhop:
    writeln tbao2
    jmp thoat       
;cld ; chonchieu xu ly chuoi
;mov cx, 10 ; so ky tu/so byte can so sanh
;lea si, oldpass; (DS:SI)--> dia chi cua chuoi nguon
;lea di, newpass; (ES:DI)--> dia chi cua chuoi dich
;repe cmpsb ; so sanh tung ky tu/byte


je intb1 
    writeln tbao2
    jmp thoat

intb1: 
    writeln tbao1

thoat:
mov ah,08h
int 21h
mov ah, 4ch
int 21h
cseg ends
end begin
