/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package QuanLyNhanVien;

/**
 *
 * @author maima
 */
import java.util.*;
import java.io.*;

public class Test_DSNV{
	public static void main(String arg[])
		throws IOException, FileNotFoundException, ClassNotFoundException
	{
		ArrayList<NhanVien> dsNV = new ArrayList<NhanVien>();
		String s1 = "Nguyen Thi Ha$13/04/1990$Thanh Xuan-Ha Noi$Nu$Khoa CNTT$2.7$10$180000";
		String s2 = "Pham Van Son$10/11/1983$Dong Da-Ha Noi$Nam$Khoa CNTT$4.5$15$180000";
		String s3 = "Dao Van Huy$20/07/1973$Hoang Mai-Ha Noi$Nam$Khoa CNTT$5.5$10$180000";
		String s4 = "Nguyen Van Quan$10/03/1993$Ha Dong-Ha Noi$Nam$Khoa CNTT$3.2$7$180000";
		String s5 = "Luong Sy Binh$21/12/2001$Chau Giang-Ha Nam$Nam$Khoa CNTT$4.4$9$180000";
		String s6 = "Nguyen Hai Minh$14/04/1995$Thanh Xuan-Ha Noi$Nam$Khoa CNTT$6.2$5$180000";
		NhanVien nv1 = new NhanVien(s1);
		NhanVien nv2 = new NhanVien(s2);
		NhanVien nv3 = new NhanVien(s3);
		NhanVien nv4 = new NhanVien(s4);
		NhanVien nv5 = new NhanVien(s5);
		NhanVien nv6 = new NhanVien(s6);
		dsNV.add(nv1);
		dsNV.add(nv2);
		dsNV.add(nv3);
		dsNV.add(nv4);
		dsNV.add(nv5);
		dsNV.add(nv6);
		System.out.print("\n\n DSNV");
		for(NhanVien nv : dsNV)
			nv.hienThi();
		System.out.print("\n---------------------------------\n");
		XuLyFile_DSNV_DataObject.luuFileDSNV(dsNV);
		System.out.print("\n---------------------------------\nLUU FILE XONG\n\n");
		ArrayList<NhanVien> readNV = XuLyFile_DSNV_DataObject.docFileDSNV();
		System.out.print("\nDSNV doc tu File: "); 
		for (NhanVien nv : readNV)
			nv.hienThi();
		System.out.print("\n---------------------------------\n");
		readNV.sort(Comparator.comparingDouble(NhanVien::tinhLuong));
		System.out.print("\n---------------------------------\nDSNV Sap Xep Theo luongThucLinh Tang Dan:");
        for (NhanVien nv : readNV)
            nv.hienThi();
        String targetName = "Nguyen Thi Ha";
        float newHeSoLuong = 3.5f;
        modifyHeSoLuong(dsNV, targetName, newHeSoLuong);

        
        System.out.print("\nDSNV After Modifying heSoLuong:");
        for (NhanVien nv : dsNV)
            nv.hienThi();
        System.out.print("\n---------------------------------\n");
	}
	public static void modifyHeSoLuong(ArrayList<NhanVien> dsNV, String hoTen, float newHeSoLuong) {
        for (NhanVien nv : dsNV) {
            if (nv.layHoTen().equalsIgnoreCase(hoTen)) {
                nv.chinhHeSoLuong(newHeSoLuong);
                System.out.println("\nChinh sua heSoLuong cua " + hoTen + " thanh " + newHeSoLuong);
                return;
            }
        }
        System.out.println("\nNhan vien " + hoTen + " not found.");
    }
}
