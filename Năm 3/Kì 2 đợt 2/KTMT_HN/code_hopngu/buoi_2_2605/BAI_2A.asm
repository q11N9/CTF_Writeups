CSEG SEGMENT
ASSUME CS: CSEG
start: 
mov cx,2
mov ah,02h
mov dl, '8'
lap_in:
    int 21h
    inc dl
loop lap_in
mov ah, 08h ; Ham 08h, ngat 21h
int 21h
mov ah, 4Ch ; Thoat khoi ctrinh
int 21h
CSEG ENDS
END start
