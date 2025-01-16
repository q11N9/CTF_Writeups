/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De1_PersonStudent;

/**
 *
 * @author maima
 */
public class Student extends Person {
    String maSV, email; 
    double diemTK;
    public Student(String maSV, String email, double diemTK, String hoTen, String ngaySinh, String diaChi, String gioiTinh) {
        super(hoTen, ngaySinh, diaChi, gioiTinh);
        this.maSV = maSV;
        this.email = email;
        this.diemTK = diemTK;
    }
    @Override
    public void hienThi(){
        super.hienThi();
        System.out.println("Ma sinh vien: " + maSV);
        System.out.println("Email: " + email);
        System.out.println("Diem tong ket: " + diemTK);
    }
    
}
