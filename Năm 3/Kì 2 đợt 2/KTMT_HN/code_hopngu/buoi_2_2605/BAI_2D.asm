DSEG SEGMENT
    max DB 30
    len DB 0
    chuoi DB 30 dup(?)
    tbao DB 'Hay go vao 1 chuoi: $'
DSEG ENDS
CSEG SEGMENT
    ASSUME CS: CSEG, DS: DSEG
start: mov ax, DSEG
    mov ds, ax
    mov ah, 09h ; In cau thong bao ra man hinh
    lea dx, tbao
    int 21h
    mov ah, 0Ah ; Ham 0Ah, nhap chuoi ky tu tu ban phim
    lea dx, MAX ; dx chua dia chi vung dem ban phim
    int 21h ; goi ngat thuc hien ham
    mov ah, 4Ch ; tro ve he dieu hanh
    int 21h
CSEG ENDS
END start
