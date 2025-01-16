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
public class ThiSinhKhoiC extends Thisinh{
    private double dvan , dsu , ddia ;

    public ThiSinhKhoiC() {
    }

    public ThiSinhKhoiC(double dvan, double dsu, double ddia) {
        this.dvan = dvan;
        this.dsu = dsu;
        this.ddia = ddia;
    }

    public ThiSinhKhoiC(double dvan, double dsu, double ddia, String hoten, String ngaysinh, String diachi) {
        super(hoten, ngaysinh, diachi);
        this.dvan = dvan;
        this.dsu = dsu;
        this.ddia = ddia;
    }

    public double getDvan() {
        return dvan;
    }

    public void setDvan(double dvan) {
        this.dvan = dvan;
    }

    public double getDsu() {
        return dsu;
    }

    public void setDsu(double dsu) {
        this.dsu = dsu;
    }

    public double getDdia() {
        return ddia;
    }

    public void setDdia(double ddia) {
        this.ddia = ddia;
    }
    public void HienthikhoiC(){
        System.out.printf("%-15s%-15s%-15s%-15.2f%-15.2f%-15.2f\n",gethoten(),getngaysinh(),getdiachi(),getDvan(),getDsu(),getDdia());
    }

    @Override
    public String toString(){
        return String.format("%-15s%-15s%-15s%-15.2f%-15.2f%-15.2f",
            gethoten(), getngaysinh(), getdiachi(), getDvan(), getDsu(), getDdia());
    }
    public ThiSinhKhoiC NhapthongThisinhkhoiC(Scanner input) {
        System.out.println("Nhap ho ten : ");
        String hoten = input.nextLine();
        System.out.println("Nhap ngay sinh : ");
        String ngaysinh = input.nextLine();
        System.out.println("Nhap dia chi : ");
        String diachi = input.nextLine();
        System.out.println("Nhap diem van: ");
        double dvan = Double.parseDouble(input.nextLine());
        System.out.println("Nhap diem su : ");
        double dsu = Double.parseDouble(input.nextLine());
        System.out.println("Nhap diem dia : ");
        double ddia = Double.parseDouble(input.nextLine());
        return new ThiSinhKhoiC(dvan, dsu, ddia, hoten, ngaysinh, diachi);
    
    }
   }