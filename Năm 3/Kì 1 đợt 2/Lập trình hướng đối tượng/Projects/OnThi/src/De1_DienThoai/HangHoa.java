/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De1_DienThoai;

import java.io.Serializable;

/**
 *
 * @author maima
 */
public class HangHoa implements Serializable{

    String maHang, ten;
    double giaBan;
    public HangHoa(String maHang, String ten, double giaBan) {
        this.maHang = maHang;
        this.ten = ten;
        this.giaBan = giaBan;
    }
    public void hienThi(){
        System.out.print("Ma hang: " + maHang + "\nTen hang: " + ten + "\nGia ban: " + giaBan + "\n");
    }
}
