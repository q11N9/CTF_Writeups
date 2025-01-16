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
import java.io.Serializable;

public class NhanVien implements Serializable{
	private String hoTen, ngaySinh, diaChi, gioiTinh, phongBan;
	private float heSoLuong;
	private float thamNien;
	static float luongCoBan = 180000;

	public void NhanVien(){

	}
	public NhanVien(String hoTen, String ngaySinh, String diaChi, String gioiTinh, String phongBan, float heSoLuong, float thamNien){
		this.hoTen = hoTen;
		this.ngaySinh = ngaySinh;
		this.diaChi = diaChi;
		this.gioiTinh = gioiTinh;
		this.phongBan = phongBan;
		this.heSoLuong = heSoLuong;
		this.thamNien = thamNien;
	}
	public NhanVien(String s){
		String[] result = s.split("\\$");
		hoTen = result[0];
		ngaySinh = result[1];
		diaChi = result[2];
		gioiTinh = result[3];
		phongBan = result[4];
		heSoLuong = Float.parseFloat(result[5]);
		thamNien = Float.parseFloat(result[6]);
		luongCoBan = Float.parseFloat(result[7]);
	}
        @Override
	public String toString(){
		return hoTen + "$" + ngaySinh + "$" + diaChi + "$" + gioiTinh + "$" + phongBan + "$" + heSoLuong + "$" + thamNien + "$" + luongCoBan;
	}
	public void chinhHeSoLuong(float heSoLuong){
		this.heSoLuong = heSoLuong;
	}
	public String layHoTen(){
		return hoTen;
	}
	public void hienThi(){
		System.out.printf("\n|%20s", hoTen);
		System.out.printf("|%11s", ngaySinh);
		System.out.printf("|%20s", diaChi);
		System.out.printf("|%5s", gioiTinh);
		System.out.printf("|%10s", phongBan);
		System.out.printf("|%5.2f", heSoLuong);
		System.out.printf("|%5.2f", thamNien);
		System.out.printf("|%10.2f|\n", luongCoBan);
	}
	public float tinhLuong(){
		return luongCoBan * heSoLuong * (1 + thamNien/100);
	}
}