.model small
.data
   filecu db 100 dup('$')
   filemoi db 100 dup('$')
   thefile dw ?
   msg_filecu db 'nhap ten file cu: $'
   msg_filemoi db 10,13,'nhap ten file moi: $'
   msg_tc db 10,13,'Da doi ten file thanh cong!$'
   msg_tb db 10,13, 'Doi ten file that bai!'
   
 .code
 main proc
    mov ax,@data
    mov ds,ax
    mov es,ax
    
    mov ah,9
    lea dx,[msg_filecu]
    int 21h
    
    mov ah,10
    lea dx,[filecu]
    int 21h
    
    lea si,[filecu+2]
    mov cx,0
    mov cl,[filecu+1]
    add si,cx
    mov [si],0
    
    mov ah,9
    lea dx,[msg_filemoi]
    int 21h
    
    mov ah,10
    lea dx,[filemoi]
    int 21h
           
    lea si,[filemoi+2]
    mov cx,0
    mov cl,[filemoi+1]
    add si,cx
    mov [si],0
           
    mov ah,56h
    lea dx,[filecu+2]
    lea di,[filemoi+2]
    int 21h
    
    jc error
    
    mov ah,9
    lea dx,msg_tc
    int 21h
    jmp endf
error:
     mov ah,9
    lea dx,msg_tb
    int 21h
    jmp endf
    
endf:        
    mov ah,4ch
    int 21h
    main endp
 end
    
    