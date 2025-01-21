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
chuoi db 100 dup(10) 
enter db 10,13,'Kq: $'
dseg ends
cseg segment
assume cs:cseg, ds:dseg, es: dseg
begin: mov ax, dseg
mov ds, ax
mov es, ax

mov cx, 10 ; so ky tu/so byte can so sanh
mov si,0
L1: 
MOV AH, 8 ; nhap ky tu
INT 21H
CMP AL,1Bh ;check dau esc
JE STOP
MOV chuoi[si], AL
INC SI

MOV AH,2
MOV DL, '*'
INT 21H
LOOP L1

STOP:
mov ah,9
lea dx,enter 
int 21h
mov dx,0

MOV CX,SI
ADD CX,1
mov si,0
Print:
    MOV Ah,2
    MOV DL, chuoi[si]
    inc si
    int 21h
loop print    
mov ah, 4ch
int 21h
cseg ends
end begin
