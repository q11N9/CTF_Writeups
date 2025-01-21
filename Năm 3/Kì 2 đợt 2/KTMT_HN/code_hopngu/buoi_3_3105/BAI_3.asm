DSEG SEGMENT
    tbao DB 'Hay go vao 1 chu cai viet thuong: $' 
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
mov ah, 08h 
int 21h ; goi ngat thuc hien ham
mov dl, al ;luu sang DL

nhan:
mov ah, 02h ; in ky tu trong DL ra man hinh
int 21h
;tao khoang trang
mov bl,dl ;tam luu DL vao BL
mov dl,20h ;khoang trang
int 21h
mov dl,bl ;tra lai DL nhu cu

inc dl ; DL chua ky tu ke can in; DL = DL+1
cmp dl, 'z' ; So sanh voi ky tu 'Z'
jna nhan ; Neu <= 'z' thi tiep tuc in

mov ah, 08h ; Neu > 'z' thi thoat (ngung in)
int 21h
mov ah, 4Ch
int 21h

CSEG ENDS
END start
