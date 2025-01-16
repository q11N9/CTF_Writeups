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
public class ThisinhkhoiA extends Thisinh {

    private double dtoan, dly, dhoa;

    public ThisinhkhoiA() {
    }

    public ThisinhkhoiA(double dtoan, double dly, double dhoa) {
        this.dtoan = dtoan;
        this.dly = dly;
        this.dhoa = dhoa;
    }

    public ThisinhkhoiA(double dtoan, double dly, double dhoa, String hoten, String ngaysinh, String diachi) {
        super(hoten, ngaysinh, diachi);
        this.dtoan = dtoan;
        this.dly = dly;
        this.dhoa = dhoa;
    }

    public double getDtoan() {
        return dtoan;
    }

    public void setDtoan(double dtoan) {
        this.dtoan = dtoan;
    }

    public double getDly() {
        return dly;
    }

    public void setDly(double dly) {
        this.dly = dly;
    }

    public double getDhoa() {
        return dhoa;
    }

    public void setDhoa(double dhoa) {
        this.dhoa = dhoa;
    }
    public void HienthikhoiA(){
        System.out.printf("%-15s%-15s%-15s%-15.2f%-15.2f%-15.2f\n",gethoten(),getngaysinh()
                ,getdiachi(),getDtoan(),getDly(),getDhoa());
    }
    @Override
    public String toString(){
        return String.format("%-15s%-15s%-15s%-15.2f%-15.2f%-15.2f",
            gethoten(), getngaysinh(), getdiachi(), getDtoan(), getDly(), getDhoa());
    }

    public ThisinhkhoiA NhapthongThisinhkhoiA(Scanner input) {
        System.out.println("Nhap ho ten : ");
        String hoten = input.nextLine();
        System.out.println("Nhap ngay sinh : ");
        String ngaysinh = input.nextLine();
        System.out.println("Nhap dia chi : ");
        String diachi = input.nextLine();
        System.out.println("Nhap diem toan: ");
        double dtoan = Double.parseDouble(input.nextLine());
        System.out.println("Nhap diem ly : ");
        double dly = Double.parseDouble(input.nextLine());
        System.out.println("Nhap diem hoa : ");
        double dhoa = Double.parseDouble(input.nextLine());
        return new ThisinhkhoiA(dtoan, dly, dhoa, hoten, ngaysinh, diachi);
    }

}
