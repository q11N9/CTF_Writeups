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
public class Person implements Serializable{
    String hoTen, ngaySinh, diaChi, gioiTinh;

    public Person() {
    }

    public Person(String hoTen, String ngaySinh, String diaChi, String gioiTinh) {
        this.hoTen = hoTen;
        this.ngaySinh = ngaySinh;
        this.diaChi = diaChi;
        this.gioiTinh = gioiTinh;
    }
    @Override
    public String toString(){
        return hoTen + "$" + ngaySinh + "$" + diaChi + "$" + gioiTinh;
    }
    public void hienThi(){
        System.out.print("\n\n Ho ten: " + hoTen);
        System.out.print("\n Ngay sinh: " + ngaySinh);
        System.out.print("\n Dia chi: " + diaChi);
        System.out.print("\n Gioi tinh: " + gioiTinh);
    }
}
