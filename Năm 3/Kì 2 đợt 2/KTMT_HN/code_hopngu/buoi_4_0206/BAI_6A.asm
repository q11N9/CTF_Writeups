inchuoi MACRO chuoi
        MOV AH, 9h
        LEA DX, chuoi
        INT 21h
        ENDM
DSEG SEGMENT
    msg1 DB "Hay nhap so nhi phan 8 bit: $"
    msg2 DB "So nhi phan da nhap la: $"
    xdong DB 10, 13, '$'
    sobin DB ? ; luu tru so nhi phan nhan duoc
DSEG ENDS
CSEG SEGMENT
    ASSUME CS:CSEG, DS:DSEG
begin: MOV AX, DSEG
       MOV DS, AX
            inchuoi msg1
       CALL bin_in
       MOV sobin, BL
            inchuoi xdong
            inchuoi msg2
       MOV BL, sobin
       CALL bin_out
       MOV AH, 01
       INT 21h
       MOV AH, 4Ch ; thoat khoi chuong trinh 
       INT 21h
bin_in  PROC
        MOV BL, 0 ; Xoa BL
        MOV CX, 8 ; nhap du 8 bit thi dung

   nhap:MOV AH, 01h ; ham nhap ky tu
        INT 21h
        CMP AL, 0Dh ;neu la phim  Enter thi thoi nhap
        JZ exit ; k phai Enter thi doi sang bit
        SHL BL, 1 ; Dic tri BL 1 bit
        SUB AL, 30h ; Ky so - 30h = so
        ADD BL, AL ; Chuyen bit tu AL sang BL luu tru
        LOOP nhap
   exit:RET
bin_in ENDP
bin_out PROC
        MOV CX, 8 ; xuat 8 bit trong BL ra M.Hinh
   xuat:MOV DL, 0
        SHL BL, 1 ; CF chua MSB, xuat ra man hinh
        RCL DL, 1 ; dua CF vao LSB cua DL
        ADD DL, 30h ; So + 30h = Ky so
        MOV AH, 02h ; In ra man hinh
        INT 21h
        LOOP xuat
        RET
bin_out ENDP
CSEG ENDS
    END begin
