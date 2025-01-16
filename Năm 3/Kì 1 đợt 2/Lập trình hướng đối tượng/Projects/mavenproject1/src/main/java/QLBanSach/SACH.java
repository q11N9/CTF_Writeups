/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package QLBanSach;

/**
 *
 * @author maima
 */
import java.util.*;

public class SACH{
	private String maSach;
	private String tenSach;
	private int soLuongMua;
	private float donGia;
	public void nhapSach(){
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhap ma sach: ");
		this.maSach = sc.nextLine();
		System.out.print("Nhap ten sach: ");
		this.tenSach = sc.nextLine();
		System.out.print("Nhap so luong mua: ");
		this.soLuongMua = sc.nextInt();
		System.out.print("Nhap don gia: ");
		this.donGia = sc.nextFloat();

	}
	public void inSach(){
		System.out.print("Ma sach: " + this.maSach);
		System.out.print("\nTen sach: " + this.tenSach);
		System.out.print("\nSo luong mua: " + this.soLuongMua);
		System.out.print("\nDon gia: " + this.donGia);
		System.out.print("\nThanh tien: " + this.thanhTien());
	}
	public float thanhTien(){
		return this.soLuongMua*donGia;
	}
}