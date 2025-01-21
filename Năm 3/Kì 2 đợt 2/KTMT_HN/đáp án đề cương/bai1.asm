.model small
.stack 100
.data
tb1 db "Nhap MSV: $"
tb2 db "AT170432","$"
tb3 db 13,10,"NGUYEN DUC MANH $"
tb4 db 13,10,"sai msv$"
str1 db 100,0,100 dup('$')
.code
main proc
    mov ax,@data
    mov ds,ax
    
    ;nhap chuoi 1  
        lea dx,tb1  
        mov ah,09h
        int 21h    
        lea dx,str1 
        mov ah,10
        int 21h
        xor cx,cx 
    
    check:
    lea si,str1+2
    mov cl,[str1+1]
    lea dx,tb2
       
    lap:
        xor ax,ax
        mov al,[si]
        cmp al,[di]
        jne notsame
        inc si
        inc di
        loop lap
        lea dx,tb3
        mov ah,9
        int 21h
        jmp Exit
        
        notsame:
            lea dx,tb4
            mov ah,9
            int 21h
            jmp Exit
                   
    Exit:
        mov ah,4ch
        int 21h
main endp
end main
