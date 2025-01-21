DSEG SEGMENT
    tbao DB 'Hay go vao 1 chu cai: $'
    tbao_sang DB 10,13, 'Good morning! $'
    tbao_chieu DB 10,13, 'Good afternoon! $'
    tbao_toi DB 10,13, 'Good evening! $'
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

;thuc hien so sanh
; = S or s -> sang
CMP BL,'S'
JE sang
CMP BL,'s' 
JE sang
; T or t -> chieu
CMP BL,'T' 
JE chieu
CMP BL,'t' 
JE chieu
; C or c -> toi
CMP BL,'C' 
JE toi
CMP BL,'c' 
JE toi

sang:
mov ah, 09h ; In cau thong bao ra man hinh
lea dx,tbao_sang
int 21h
jmp stop

chieu:
mov ah, 09h ; In cau thong bao ra man hinh
lea dx, tbao_chieu
int 21h
jmp stop

toi:
mov ah, 09h ; In cau thong bao ra man hinh
lea dx, tbao_toi
int 21h
jmp stop

stop:
mov ah, 4Ch ; tro ve he dieu hanh
int 21h
CSEG ENDS
END start
