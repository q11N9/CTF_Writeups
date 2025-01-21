dseg segment
;tenfile db "D:\date.txt",0
tenfile db 100 dup(0)
thefile dw ?
buffer db 251 dup ('$')
result db 100 dup(0)
inthuong DB 100 DUP(0)
inhoa DB 100 DUP (0)

dseg ends
cseg segment
assume cs:cseg, ds:dseg
begin: mov ax, dseg
mov ds, ax

;nhap ten file:
MOV SI, 0 ; chi so mang
MOV CX, 100 ; do dai mang max

LAP: 
    MOV AH, 1 ; nhap ky tu
    INT 21H
    CMP AL,0Dh ;check dau enter
    JE STOP1
    MOV tenfile[SI], AL
    INC SI
JMP LAP

stop1:
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

mov cx,250
mov si,0 
mov bh,0
convert:
    mov AL, buffer[si]  
    CMP AL,20h ;check dau space
    JE dau_trang
    CMP AL, '$'
    JE STOP
    CMP AL, 'Z'
    JBE chu_hoa;chu hoa
    JA chu_thuong;chu thuong
    next:
    ;MOV result[SI], AL
    INC SI  
    inc bh
    cmp cx,1
    je stop
JMP convert

dau_trang:
;nem vao string thuong
mov inthuong[SI],AL
jmp next


chu_hoa: 
;nem vao string hoa
mov inhoa[SI],AL
;day la chu hoa, convert thanh chu thuong
ADD AL, 20h
;nem vao string thuong
mov inthuong[SI],AL
jmp next

chu_thuong: 
;nem vao string thuong
mov inthuong[SI],AL
;day la chu thuong, convert thanh chu hoa
SUB AL, 20h
;nem vao string hoa
mov inhoa[SI],AL

jmp next


STOP: ;co duoc chuoi
mov bl,bh
mov bh,0
mov cx,bx
mov SI,0
mov ah,02h
L2:
    mov DL,inthuong[SI]
    int 21h
    inc SI
loop L2

mov ah, 3ch ; tao tap tin moi
lea dx, tenfile
mov cx, 0 ; tap tin co thuoc tinh binh thuong
int 21h
mov cx, bx
mov thefile, ax ; cat the file
mov ah, 40h ; ghi file
mov bx, thefile


GHI_FILE:
    ;xor cx, cx
    ;mov cl, len
    mov dh,0
    mov dl, inthuong[SI]
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
