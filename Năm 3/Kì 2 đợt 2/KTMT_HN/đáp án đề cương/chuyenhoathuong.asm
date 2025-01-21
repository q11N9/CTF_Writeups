.model small
.stack 100h
.data 
   str db 256 dup('$')
   tb1 db 10,13, 'chuoi thuong: $'
   tb2 db 10, 13, 'chuoi hoa: $' 
.code 
main proc 
    mov ax,@data
    mov ds, ax
     
    lea dx,str 
    mov ah,10
    int 21h
    
    mov ah,9
    lea dx,tb1
    int 21h
    call inthuong
    
    mov ah,9
    lea dx,tb2
    int 21h
    call inhoa     
    
    mov ah,4ch
    int 21h
main endp

inthuong proc
    lea si ,str+2 
    
    lap1:
    mov dl,[si]
    cmp dl,'A'
    jl in1
    cmp dl,'Z'
    jg in1
    add dl,32
    
    in1:
    mov ah,2
    int 21h
    inc si
    cmp [si],'$'
    jne lap1
 ret
inthuong endp                                                                

inhoa proc
    lea si ,str+2 
    
    lap2:
    mov dl,[si]
    cmp dl,'a'
    jl in2
    cmp dl,'z'
    jg in2
    sub dl,32
    
    in2:
    mov ah,2
    int 21h
    inc si
    cmp [si],'$'
    jne lap2
 ret
inhoa endp      

end