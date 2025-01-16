/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ViduMinhHoa;

import java.io.Serializable;

/**
 *
 * @author maima
 */
public class NhanVien extends Person implements Serializable{
    String phongBan;
    float heSoLuong;
    float thamNien;
    static float luongCoBan = 1800000;
    public String getPhongBan() {
        return phongBan;
    }

    public void setPhongBan(String phongBan) {
        this.phongBan = phongBan;
    }

    public float getHeSoLuong() {
        return heSoLuong;
    }

    public void setHeSoLuong(float heSoLuong) {
        this.heSoLuong = heSoLuong;
    }

    public float getThamNien() {
        return thamNien;
    }

    public void setThamNien(float thamNien) {
        this.thamNien = thamNien;
    }

    public static float getLuongCoBan() {
        return luongCoBan;
    }

    public static void setLuongCoBan(float luongCoBan) {
        NhanVien.luongCoBan = luongCoBan;
    }

    public String getHoTen() {
        return hoTen;
    }

    public void setHoTen(String hoTen) {
        this.hoTen = hoTen;
    }

    public String getNgaySinh() {
        return ngaySinh;
    }

    public void setNgaySinh(String ngaySinh) {
        this.ngaySinh = ngaySinh;
    }

    public String getDiaChi() {
        return diaChi;
    }

    public void setDiaChi(String diaChi) {
        this.diaChi = diaChi;
    }

    public String getGioiTinh() {
        return gioiTinh;
    }

    public void setGioiTinh(String gioiTinh) {
        this.gioiTinh = gioiTinh;
    }
    

    public NhanVien() {
    }

    public NhanVien(String phongBan, float heSoLuong, float thamNien, String hoTen, String ngaySinh, String diaChi, String gioiTinh) {
        super(hoTen, ngaySinh, diaChi, gioiTinh);
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
        return super.toString() + "$" + phongBan + "$" + heSoLuong + "$" + 
                thamNien + "$" + luongCoBan;
    }
    public float tinhLuong(){
        return luongCoBan + heSoLuong*(1 + thamNien/100);
    }
    public void hienThi(){
        super.hienThi();
        System.out.print("\n He so luong: " + heSoLuong);
        System.out.print("\n Luong co ban: " + luongCoBan);
        System.out.printf("\n Tien luong: %.1f", tinhLuong());
    }
}
