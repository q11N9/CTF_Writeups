inchuoi MACRO chuoi
 MOV AH, 9h
 LEA DX, chuoi
 INT 21h
 ENDM
DSEG SEGMENT
 msg1 DB "Hay nhap 1 ky tu: $"
 msg2 DB "Ma ASCII o dang Hex: $"       
 xdong DB 10, 13, �$�
 kytu DB ?
DSEG ENDS
CSEG SEGMENT
 ASSUME CS:CSEG, DS:DSEG
begin: MOV AX, DSEG
 MOV DS, AX
 inchuoi msg1
 MOV AH, 01h
 INT 21h
 MOV kytu, AL ; c?t k� t? nh?n du?c
 inchuoi xdong
 inchuoi msg2
 MOV BH, kytu ; K� t? c?n in
 CALL hex_out
 MOV AH, 02 ; in ra k� t? h sau s? Hex
 MOV DL, 'h'
 INT 21h
 MOV AH, 01
 INT 21h
 MOV AH, 4Ch ; thoat kh?i chuong tr�nh
 INT 21h
hex_out PROC
 MOV CX, 4
 xuat:PUSH CX
 MOV CL, 4
 MOV DL, BH
 SHR DL, CL
 CMP DL, 09h
 JA kytu1
 ADD DL, 30h ; �?i th�nh k� s? �0�-�9�
 JMP inra
 kytu1:
    ADD DL, 37h ; �?i th�nh k� t? �A-�F�
 inra:MOV AH, 02h ; In ra m�n h�nh k� t? d� d?i
 INT 21h
 SHL BX, CL ; Quay tr�i BX 4 bit
 POP CX
 LOOP xuat
 RET
hex_out ENDP
CSEG ENDS
 END begin 