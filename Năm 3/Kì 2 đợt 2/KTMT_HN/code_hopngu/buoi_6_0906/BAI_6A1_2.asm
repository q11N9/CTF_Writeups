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
tbao db 10,13,'$'
oldpass db "0123456789"
newpass db   100 dup(10) 
pass db 10,13,"Ban da nhap dung $"
fail db 10,13,"Ban da nhap sai roi va vui long nhap lai $"
dseg ends
cseg segment
assume cs:cseg, ds:dseg, es: dseg
begin: mov ax, dseg
mov ds, ax
mov es, ax
again:
mov si,0
mov cx,10
L1: 
MOV AH, 8 ; nhap ky tu
INT 21H
CMP AL,1Bh ;check dau esc
JE stop
MOV newpass[si], AL
INC SI

MOV AH,2
MOV DL, '*'
INT 21H
LOOP L1
stop:  


cld ; chonchieu xu ly chuoi
mov cx, 10 ; so ky tu/so byte can so sanh
lea si, oldpass; (DS:SI)--> dia chi cua chuoi nguon
lea di, newpass; (ES:DI)--> dia chi cua chuoi dich
repe cmpsb ; so sanh tung ky tu/byte
je jmpass
jne jmfail        

jmpass:
    writeln pass
    jmp thoat    

jmfail:
    writeln fail
    ;writeln tbao
    jmp again     

    thoat:
mov ah,08h
int 21h
mov ah, 4ch
int 21h
cseg ends
end begin
