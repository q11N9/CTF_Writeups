inchuoi MACRO chuoi
        MOV AH, 9h
        LEA DX, chuoi
        INT 21h
        ENDM
DSEG SEGMENT
    msg1 DW "Hay nhap ky tu vao ban phim: $"
    msg2 DW 10,13,"Ma ASCII  nhi phan cua ky tu: $"
    sobin DW 100 DUP(0) ; luu tru so nhi phan nhan duoc
    number DW 0
DSEG ENDS
CSEG SEGMENT
    ASSUME CS:CSEG, DS:DSEG
start: MOV AX, DSEG
       MOV DS, AX
       inchuoi msg1
nhap:
    MOV AH, 01h
    INT 21h
    cmp al, 13
    je prechia
    
    mov ah,0
    mov cx,ax
    mov bx,10
    ;mov ax,so
    ;mul bx
    add ax,cx
    mov number,ax 
    jmp nhap  
prechia:
    inchuoi msg2
    
    mov cx,0
    mov bx,2
    mov ax,number
    
chia:
    mov dx,0
    div bx
    add dx,30h
    push dx
    ;mov sobin[si], dx
    ;inc si
    inc cx
    cmp ax,0
    je preinso
jmp chia        

preinso: 
    dec cx       
inso:
    pop dx
    mov ah,2
    int 21h
loop inso       
       
  
mov ah,08h
int 21h
mov ah, 4Ch ; tro ve he dieu hanh
int 21h
CSEG ENDS
END start