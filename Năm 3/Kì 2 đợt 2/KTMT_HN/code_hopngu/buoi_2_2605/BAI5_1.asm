.model small  
.stack 50
.data
    tbao DB 'Hay go vao 1 phim: $' 
    tbao2 DB 10,13,'Ky tu nhan duoc la: $'
    kytu db ?

.code 
main proc                         
mov ax,@data
mov ds, ax  

mov ah, 09h ; In cau thong bao ra man hinh
lea dx, tbao
int 21h   

mov ah, 01h ; Ham 1, nhan ky tu tu ban phim
int 21h ; goi ngat thuc hien ham
mov kytu, al

mov ah, 09h ; In cau thong bao ra man hinh
lea dx, tbao2
int 21h 

mov ah, 2
mov dl, kytu
int 21h

mov ah, 4Ch ; tro ve he dieu hanh
int 21h 

main ENDP
END
