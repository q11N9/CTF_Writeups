
dseg segment
chuoi Db  100 DUP(0)
len db $ - string1
tenfile db "E:\emu8086\emu8068_loca\emu8086\MyBuild\data.txt",0
thefile dw ?
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
    MOV chuoi[SI], AL
    INC SI
JMP LAP


STOP: 
mov ah, 3ch ; tao tap tin moi
lea dx, tenfile
mov cx, 0 ; tap tin co thuoc tinh binh thuong
int 21h
mov cx, si
mov thefile, ax ; cat the file
mov ah, 40h ; ghi file
mov bx, thefile


GHI_FILE:
    ;xor cx, cx
    ;mov cl, len
    mov dh,0
    mov dl, chuoi[SI]
    ;lea dx, string1
    int 21h
LOOP GHI_FILE
    mov ah, 3eh ; dong tap tin
    mov bx, thefile
int 21h
mov ah, 4ch ; thoat ve Dos
int 21h
cseg ends
end begin
