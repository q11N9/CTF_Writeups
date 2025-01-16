/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ViduMinhHoa;

import static ViduMinhHoa.XuLyFile_DSNV.docDSNVFile;
import java.util.ArrayList;
import static ViduMinhHoa.XuLyFile_DSNV.luuDSNVFile;
/**
 *
 * @author maima
 */
public class TaoMoi_DSNV {
    public static void main(String[] args) {
        ArrayList<NhanVien> dsNV = new ArrayList<NhanVien>();
        String s1 = "Nguyen Thi Ha$13/04/1989$Thanh Xuan - Ha Noi$Nu$Khoa CNTT$2.3$10$1800000";
        String s2 = "Ha Ngoc Minh$12/01/1980$Ha Dong - Ha Noi$Nam$Khoa CNTT$4.5$12$1800000";
        String s3 = "Nguyen Cong Vu Ha$20/09/2000$Thanh Tri - Ha Noi$Nu$Khoa CNTT$3.5$8$1800000";
        NhanVien nv1 = new NhanVien(s1);
        NhanVien nv2 = new NhanVien(s2); 
        NhanVien nv3 = new NhanVien(s3);
        dsNV.add(nv1);
        dsNV.add(nv2);
        dsNV.add(nv3);
        System.out.print("\n\n DSNV tu tao: ");
        for (NhanVien x : dsNV) x.hienThi();
        System.out.print("\n=============================\n");
        luuDSNVFile(dsNV);
        System.out.print("\n===================\nLUU FILE XONG\n\n");
        
        dsNV = docDSNVFile();
        System.out.print("\n====================\n DSNV doc tu File: \n");
        for (NhanVien nv : dsNV) nv.hienThi();
        System.out.print("\n\n");
    }
    
}
