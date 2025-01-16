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
import java.io.Serializable;
public class SinhVien implements Serializable{
	private String maSinhVien, hoTen, ngaySinh, gioiTinh;
	private double diemTrungBinh;
	public SinhVien(){this.diemTrungBinh = 0;}
	public SinhVien(String maSinhVien, String hoTen, String ngaySinh, String gioiTinh, double diemTrungBinh){
		this.maSinhVien = maSinhVien;
		this.hoTen = hoTen;
		this.ngaySinh = ngaySinh;
		this.gioiTinh = gioiTinh;
		this.diemTrungBinh = diemTrungBinh;
	}
	public void nhap(){
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhap ma sinh vien : ");
		maSinhVien = sc.nextLine();
		System.out.print("Nhap ho ten : ");
		hoTen = sc.nextLine();
		System.out.print("Nhap ngay sinh : ");
		ngaySinh = sc.nextLine();
		System.out.print("Nhap gioi tinh : ");
		gioiTinh = sc.nextLine();
		System.out.print("Nhap diem trung binh : ");
		diemTrungBinh = sc.nextDouble();
	}
	public void hienThi(){
		System.out.printf("\n|%10s", maSinhVien);
		System.out.printf("|%30s", hoTen);
		System.out.printf("|%11s", ngaySinh);
		System.out.printf("|%5s", gioiTinh);
		System.out.printf("|%5.2f", diemTrungBinh);
	}
	public String getMaSinhVien(){
		return maSinhVien;
	}
	public void setHoTen(String hoTen){
		this.hoTen = hoTen;
	}
	public void setNgaySinh(String ngaySinh){
		this.ngaySinh = ngaySinh;
	}
}