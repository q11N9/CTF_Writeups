DSEG SEGMENT
tbao DB 'Hay go vao 1 chu cai: $' 
tbao_hoa DB 10,13,'Ky tu HOA $'
tbao_thuong DB 10,13, 'Ky tu thuong $'
DSEG ENDS
CSEG SEGMENT
ASSUME CS: CSEG, DS: DSEG
start:
mov ax, DSEG
mov ds, ax
mov ah, 09h ; In cau thong bao ra man hinh
lea dx, tbao
int 21h

; Ham 1, nhan ky tu tu ban phim
mov ah, 01h 
int 21h ; goi ngat thuc hien ham
mov bl, al ;luu tam sang BL

;thuc hien so sanh BL voi 'Z'
;mov cl, 'Z'
CMP bl, 'Z'
;chu thuong khi >Z aka CF & ZF = 0
;chu hoa khi <=Z aka CF = 1 or ZF = 1
JBE chu_hoa;chu hoa
JA chu_thuong;chu thuong

chu_hoa:
mov ah, 09h ; In cau thong bao ra man hinh
lea dx,tbao_hoa
int 21h
jmp stop

chu_thuong:
mov ah, 09h ; In cau thong bao ra man hinh
lea dx, tbao_thuong
int 21h
jmp stop


stop:
mov ah, 4Ch ; tro ve he dieu hanh
int 21h
CSEG ENDS
END start
