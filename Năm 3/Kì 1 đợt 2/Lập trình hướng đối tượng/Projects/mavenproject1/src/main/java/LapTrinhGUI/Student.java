/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package LapTrinhGUI;

/**
 *
 * @author maima
 */
import java.util.*;
public class Student extends Person {
    private String maSV, email; 
    private double diemTongKet;
    public Student(String maSV, String email, int diemTongKet, String hoTen, 
            String ngaySinh, String diaChi, String gioiTinh) {
        super(hoTen, ngaySinh, diaChi, gioiTinh);
        this.maSV = maSV;
        this.email = email;
        this.diemTongKet = diemTongKet;
    }

    public Student(String hoTen, String ngaySinh, String diaChi, String gioiTinh
            , String maSV, String email, double diemTongKet) {
        super(hoTen, ngaySinh, diaChi, gioiTinh);
        this.maSV = maSV;
        this.email=email;
        this.diemTongKet = diemTongKet;
    }
    @Override
    public void hienThiThongTin(){
        super.hienThiThongTin();
        System.out.println("Mã sinh viên: " + maSV);
        System.out.println("Email: " + email);
        System.out.println("Điểm tổng kết: " + diemTongKet);
    }
    
}
