/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De5_TSA_TSC;

import java.util.Scanner;

/**
 *
 * @author maima
 */
public class Thisinh {

   private String hoten, ngaysinh, diachi;

    public Thisinh() {
    }

    public Thisinh(String hoten, String ngaysinh, String diachi) {
        this.hoten = hoten;
        this.ngaysinh = ngaysinh;
        this.diachi = diachi;
    }

    public String gethoten() {
        return hoten;
    }

    public void sethoten(String hoten) {
        this.hoten = hoten;
    }

    public String getngaysinh() {
        return ngaysinh;
    }

    public void setngaysinh(String ngaysinh) {
        this.ngaysinh = ngaysinh;
    }

    public String getdiachi() {
        return diachi;
    }

    public void setdiachi(String diachi) {
        this.diachi = diachi;
    }
    //in thong tin dung to string cho nhan

    @Override
    public String toString() {
        return "Thisinh{" + "hoten=" + hoten + ", ngaysinh=" + ngaysinh + ", diachi=" + diachi + '}';
    }

    public Thisinh nhapTT(Scanner input) {
        System.out.println("Nhap ho ten : ");
        String hoten = input.nextLine();
        System.out.println("Nhap ngay sinh : ");
        String ngaysinh = input.nextLine();
        System.out.println("Nhap dia chi : ");
        String diachi = input.nextLine();
        return new Thisinh(hoten, ngaysinh, diachi);
    }
}
