dseg segment
;tenfile db "D:\data.txt",0
tenfile db 100 dup(0)
dseg ends
cseg segment
assume cs:cseg, ds:dseg
begin: mov ax, dseg
mov ds, ax
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
mov ah,41h ; xoa tap tin da co
lea dx, tenfile
int 21h
mov ah, 4ch ; thoat ve Dos
int 21h
cseg ends
end begin
