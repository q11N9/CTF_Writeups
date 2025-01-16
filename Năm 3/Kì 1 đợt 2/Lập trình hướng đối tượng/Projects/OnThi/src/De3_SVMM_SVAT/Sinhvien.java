/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De3_SVMM_SVAT;

import java.io.Serializable;

/**
 *
 * @author maima
 */
public class Sinhvien implements Serializable{
    private String Masv , hoten , gioitinh , ngaysinh , diachi;
    private double DTB;

    public Sinhvien() {
    }

    public Sinhvien(String Masv, String hoten, String gioitinh, String ngaysinh, String diachi, double DTB) {
        this.Masv = Masv;
        this.hoten = hoten;
        this.gioitinh = gioitinh;
        this.ngaysinh = ngaysinh;
        this.diachi = diachi;
        this.DTB = DTB;
    }

    public String getMasv() {
        return Masv;
    }

    public void setMasv(String Masv) {
        this.Masv = Masv;
    }

    public String getHoten() {
        return hoten;
    }

    public void setHoten(String hoten) {
        this.hoten = hoten;
    }

    public String getGioitinh() {
        return gioitinh;
    }

    public void setGioitinh(String gioitinh) {
        this.gioitinh = gioitinh;
    }

    public String getNgaysinh() {
        return ngaysinh;
    }

    public void setNgaysinh(String ngaysinh) {
        this.ngaysinh = ngaysinh;
    }

    public String getDiachi() {
        return diachi;
    }

    public void setDiachi(String diachi) {
        this.diachi = diachi;
    }

    public double getDTB() {
        return DTB;
    }

    public void setDTB(double DTB) {
        this.DTB = DTB;
    }
    public void Hienthitt(){
        System.out.println("Ma sv : "+getMasv());
        System.out.println("Ho ten : "+getHoten());
        System.out.println("Gioi Tinh : "+getGioitinh());
        System.out.println("Ngay sinh : "+getNgaysinh());
        System.out.println("Dia chi  : "+getDiachi());
        System.out.println("DiemTB : "+getDTB());
    }
}
