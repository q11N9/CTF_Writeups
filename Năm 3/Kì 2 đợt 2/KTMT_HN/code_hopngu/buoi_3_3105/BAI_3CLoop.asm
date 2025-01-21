CSEG SEGMENT
ASSUME CS: CSEG
start:
    mov dl, 'Z' ; Dl chua ky tu dau tien 'Z'
mov cx, 26
L1:
mov ah, 02h ; in ky tu trong DL ra man hinh
int 21h
mov bl,dl ;tam luu DL vao BL
mov dl,20h ;khoang trang
int 21h
mov dl,bl ;tra lai DL nhu cu

dec dl ; DL chua ky tu ke can in; DL = DL-1
cmp dl, 'A' ; So sanh voi ky tu 'A'
;jnb nhan ; Neu <= 'A' thi tiep tuc in
loop L1

mov ah, 08h ; Neu > 'A' thi thoat (ngung in)
int 21h
mov ah, 4Ch
int 21h

CSEG ENDS
END start
