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
public class PhongHoc{
    private int soPhong;
    private String loaiPhong;
    private int tang;
    private float dienTich;
    public PhongHoc(){
            nhapTTPhong();
    }

    public void nhapTTPhong(){
            Scanner sc = new Scanner(System.in);
            System.out.print("Nhap so phong: ");
            this.soPhong = sc.nextInt();
            System.out.print("Nhap loai phong: ");
            this.loaiPhong = sc.nextLine();
            System.out.print("Nhap tang cua phong hoc: ");
            this.tang = sc.nextInt();
            System.out.print("Nhap dien tich cua phong hoc: ");
            this.dienTich = sc.nextFloat();
            sc.nextLine();
    }
    public void inTTPhong(){
            System.out.printf("Phong: %d\t\tLoai phong: %s\n", soPhong,loaiPhong);
            System.out.printf("Tang: %d \t\tDien tich: %.2f\n", tang, dienTich);
    }
    public PhongHoc(int soPhong, String loaiPhong, int tang, int dienTich){
            this.soPhong = soPhong;
            this.loaiPhong = loaiPhong;
            this.tang = tang;
            this.dienTich = dienTich;
    }
}