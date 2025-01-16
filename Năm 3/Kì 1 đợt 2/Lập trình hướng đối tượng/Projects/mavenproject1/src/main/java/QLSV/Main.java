/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package QLSV;

/**
 *
 * @author maima
 */
import java.util.*;
import java.io.IOException;

public class Main{
	public static void main(String[] args) {
		DSSinhVien ds = new DSSinhVien();
		try{
			ds.nhapDanhSach();
			ds.inDanhSach();
			ds.luuSinhVien("sinhvien.dat");
			ds.luuTheoLoai();

			while(true){
				System.out.println("1. Thoat");
				System.out.println("2. Sua sinh vien");
				Scanner sc = new Scanner(System.in);
				int choice = sc.nextInt();
				if (choice != 2) break;
				else{
					String maSinhVien = sc.nextLine();
					ds.suaThongTin(maSinhVien);

					ds.inDanhSach();
				}
				
			}
			
		}catch (IOException e){
			System.out.println("Loi khi xu ly file: " + e.getMessage());
		}
	}
}