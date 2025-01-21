 .model small
isngto macro
        xor bx,bx 
        mov bl,2
        xor ah,ah
        mov al, [si]
        lap:  
            cmp ax, 2
            jb bang0
            cmp ax,2
            jz bang1
            xor dx,dx 
            div bx
            cmp dx, 0
            jz bang0
            mov al, [si]
            inc bx 
            cmp bx,ax
            jz bang1 
            jmp lap
        bang1: 
            jmp cong1    
        bang0:
            mov tmp,0 
endm                                
.stack 100h
.data 
    msg1 db "so luong so nguyen to la: $"
    chuoi db 0,1,2,3,4,5,6,7,8,9,10,11
    tmp db 1 
    s db 0 
.code
    MAIN PROC 
        mov ax,@data
        mov ds,ax
        
        mov bx,13
        push bx
        mov ah,9
        lea dx, msg1
        int 21h 
        xor cx,cx
        mov cl, 12
        ktra:
            lea si,chuoi
            tungso:
                isngto
                inc si
                loop tungso
            vao: 
                xor ax,ax
                mov al,s
                inra:
                    mov bx, 10
                    xor dx,dx
                    div bx
                    push dx
                    cmp ax,0
                    jz hienthi
                    jmp inra
                hienthi: 
                    pop dx
                    cmp dx,13
                    jz thoat
                    mov ah,2
                    add dl,30h
                    int 21h
                    jmp hienthi    
                thoat:
                     mov ah,4Ch
                     int 21h 
            cong1:
                add s,1
                inc si 
                loop tungso
                jmp vao 
        main endp
    end main
