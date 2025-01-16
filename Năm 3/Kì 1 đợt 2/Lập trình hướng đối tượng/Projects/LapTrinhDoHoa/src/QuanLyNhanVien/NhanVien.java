/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package QuanLyNhanVien;

import java.io.Serializable;

/**
 *
 * @author maima
 */
public class NhanVien implements Serializable {
    private String maNV;
    private String hoTen;
    private String dienThoai;
    private double heSoLuong;

    public NhanVien(String maNV, String hoTen, String dienThoai, double heSoLuong) {
        this.maNV = maNV;
        this.hoTen = hoTen;
        this.dienThoai = dienThoai;
        this.heSoLuong = heSoLuong;
    }

    public String getMaNV() {
        return maNV;
    }

    public void setMaNV(String maNV) {
        this.maNV = maNV;
    }

    public String getHoTen() {
        return hoTen;
    }

    public void setHoTen(String hoTen) {
        this.hoTen = hoTen;
    }

    public String getDienThoai() {
        return dienThoai;
    }

    public void setDienThoai(String dienThoai) {
        this.dienThoai = dienThoai;
    }

    public double getHeSoLuong() {
        return heSoLuong;
    }

    public void setHeSoLuong(double heSoLuong) {
        this.heSoLuong = heSoLuong;
    }

    public double getLuong() {
        return heSoLuong * 1650000;
    }

    @Override
    public String toString() {
        return "-"+ maNV + ", " + hoTen + ", " + dienThoai + ", " + heSoLuong + ", " + getLuong();
    }
}