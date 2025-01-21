.model small
.stack 100
.data    
    tb1 db 10,13, 'chuoi da nhap la: $'
    str db 100 dup('$')
.code 
main proc
    mov ax,@data
    mov ds, ax 
    
    mov ah,10
    lea dx, str   
    int 21h
    
    mov ah,9
    lea dx,tb1
    int 21h
     
    mov ah,9
    lea dx,str +2
    int 21h      
    
    mov ah,4ch
    int 21h
    main endp
end