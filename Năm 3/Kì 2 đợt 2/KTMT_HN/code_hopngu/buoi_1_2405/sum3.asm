.MODEL Small
.STACK 100
.DATA  
      A1 DW 15h
      A2 DW 250
      B1 DW 16
      B2 DW 0AF1h
      C1 DW 300
      C2 DW 400  
      D1 DW 1000
      D2 DW 100
      E1 DW 1000
      E2 DW 100h
      F1 DD 3AB45Eh
      F2 DW 0A1h
.CODE 
   MAIN PROC 
    ; kh?i d?u cho DS
				MOV AX, @data
				MOV DS, AX
 
    ;15h*250
    ;mov AX,A1
    ;mov BX,A2
    ;;mul BX  
    
    ;16*0AF1h
    ;mov AX,B1
    ;mov BX,B2
    ;mul BX  
    
    ;300*400
    ;mov AX,C1
    ;mov BX,C2
    ;mul BX  
    
    ;1000/100     
    ;mov AX,D1
    ;mov BX,D2
    ;div BX   
    
    ;1000/100h
    ;mov AX,E1
    ;mov BX,E2
    ;div BX  
    
    ;3AB45Eh/0A1h
    mov AX,0B45Eh
    mov DX,3Ah      
    div F2 
    
    mov AH,4ch
    int 21h
   MAIN ENDP
END MAIN




