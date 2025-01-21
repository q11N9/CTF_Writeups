DSEG SEGMENT
tbao DB 'Hay go vao 1 phim: $' 
tbao2 DB 10,13,'Ky tu ke truoc la: $'  
tbao3 DB 10,13,'Ky tu ke sau la: $'
DSEG ENDS
CSEG SEGMENT
ASSUME CS: CSEG, DS: DSEG
start:mov ax, DSEG
mov ds, ax
mov ah, 09h ; In cau thong bao ra man hinh
lea dx, tbao
int 21h
mov ah, 01h ; Ham 1, nhan ky tu tu ban phim
int 21h ; goi ngat thuc hien ham
mov bl, al ;luu tam gia tri vao BL

;ky tu trc
mov ah, 09h ; In cau thong bao ra man hinh
lea dx, tbao2
int 21h
mov dl,bl
dec dl
mov ah,2
int 21h

;ky tu sau
mov ah, 09h ; In cau thong bao ra man hinh
lea dx, tbao3
int 21h
mov dl,bl
inc dl
mov ah,2
int 21h

mov ah, 4Ch ; tro ve he dieu hanh
int 21h
CSEG ENDS
END start
