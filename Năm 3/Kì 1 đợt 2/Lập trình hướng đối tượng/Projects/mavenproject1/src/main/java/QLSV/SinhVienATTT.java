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
public class SinhVienATTT extends SinhVien{
	double hocPhi;
	public SinhVienATTT(){
		super();
		this.hocPhi = 0;
	}
	public SinhVienATTT(String maSinhVien, String hoTen, String ngaySinh, String gioiTinh, double diemTrungBinh, double hocPhi){
		super(maSinhVien, hoTen, ngaySinh, gioiTinh, diemTrungBinh);
		this.hocPhi = hocPhi;
	}
        @Override
	public void nhap(){
		Scanner sc = new Scanner(System.in);
		super.nhap();
		System.out.print("Nhap hoc phi: ");
		hocPhi = sc.nextDouble();
	}
        @Override
	public void hienThi(){
		super.hienThi();
		System.out.printf("|%5.2f", hocPhi);
	}
}