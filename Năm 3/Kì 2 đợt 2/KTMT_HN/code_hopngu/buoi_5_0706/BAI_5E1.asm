dseg segment
;oldfile db "D:\date.txt",0
;newfile db "D:\baitap\date2.txt",0
filedich db 10,13,'Ten file moi: $'
filenguon db 10,13,'Ten file cu: $'
tenfile db 100 dup(0)
tenfile2 db 100 dup(0)

dseg ends
cseg segment
assume cs:cseg, ds:dseg, es: dseg
begin: mov ax, dseg
mov ds, ax
mov es, ax
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


mov ah,56h ; rename/remove ten file cu thanh moi
lea dx, tenfile
lea di, tenfile2
int 21h
mov ah, 4ch ; thoat ve Dos
int 21h
cseg ends
end begin
