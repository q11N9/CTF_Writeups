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
public class SinhVienMatMa extends SinhVien{
	String donVi;
	double luong;
	public SinhVienMatMa(){
		super();
		this.luong = 0;
	}
	public SinhVienMatMa(String maSinhVien, String hoTen, String ngaySinh, 
						String gioiTinh, double diemTrungBinh, String donVi, double luong){
		super(maSinhVien, hoTen, ngaySinh, gioiTinh, diemTrungBinh);
		this.donVi = donVi;
		this.luong = luong;
	}
        @Override
	public void nhap(){
		Scanner sc = new Scanner(System.in);
		super.nhap();
		System.out.print("Nhap ten don vi: ");
		donVi = sc.nextLine();
		System.out.print("Nhap luong: ");
		luong = sc.nextDouble();

	}
        @Override
	public void hienThi(){
		super.hienThi();
		System.out.printf("|%20s", donVi);
		System.out.printf("|%5.2s", luong);
	}
}