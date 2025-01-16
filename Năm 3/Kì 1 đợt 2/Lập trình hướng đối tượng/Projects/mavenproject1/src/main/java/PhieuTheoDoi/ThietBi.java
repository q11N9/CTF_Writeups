/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package PhieuTheoDoi;

/**
 *
 * @author maima
 */
import java.util.*;

public final class ThietBi{
	private String tenThietBi;
	private String nhaSanXuat;
	private String ngayNhap;
	private int soLuong;
	private String donGia;
	private int thanhTien;
	public ThietBi(String tenThietBi, String nhaSanXuat, String ngayNhap, int soLuong, String donGia){
            this.tenThietBi = tenThietBi;
            this.nhaSanXuat = nhaSanXuat;
            this.ngayNhap = ngayNhap;
            this.soLuong = soLuong;
            this.donGia = donGia;
            this.thanhTien = Integer.parseInt(this.donGia)*soLuong;
	}
	public ThietBi(){
            nhapTTThietBi();
	}
	public void nhapTTThietBi(){
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhap ten thiet bi: ");
		this.tenThietBi = sc.nextLine();
		System.out.print("Nhap ten nha san xuat: ");
		this.nhaSanXuat = sc.nextLine();
		System.out.print("Nhap ngay nhap: ");
		this.ngayNhap = sc.nextLine();
		System.out.print("Nhhap so luong: ");
		this.soLuong = sc.nextInt();
		System.out.print("Nhap don gia: ");
		this.donGia = sc.nextLine();
		this.thanhTien = Integer.parseInt(donGia)*soLuong;
	}
	public void inTTThietBi(){
		System.out.printf("%s   %s   %s   %d   %s   %d\n", tenThietBi, nhaSanXuat, ngayNhap, soLuong, donGia, thanhTien);
	}
}