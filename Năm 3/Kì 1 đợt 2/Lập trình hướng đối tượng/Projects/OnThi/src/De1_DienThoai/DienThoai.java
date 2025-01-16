/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De1_DienThoai;

import java.nio.file.attribute.PosixFileAttributes;

/**
 *
 * @author maima
 */
public class DienThoai extends HangHoa {
    String nhaSanXuat, mauSac, dungLuongBoNho;
    
    // Getter
    public String getNhaSanXuat() {
        return nhaSanXuat;
    }

    public String getMauSac() {
        return mauSac;
    }

    public String getDungLuongBoNho() {
        return dungLuongBoNho;
    }
    public String getMaHang() {
        return maHang;
    }

    public String getTen() {
        return ten;
    }

    public double getGiaBan() {
        return giaBan;
    }
    // Phương thức khởi tạo
    public DienThoai(String maHang, String ten, double giaBan, String nhaSanXuat, String mauSac, String dungLuongBoNho) {
        super(maHang, ten, giaBan);
        this.nhaSanXuat = nhaSanXuat;
        this.mauSac = mauSac;
        this.dungLuongBoNho = dungLuongBoNho;
    }
    
    // Phương thức hiển thị
    @Override
    public void hienThi(){
        super.hienThi();
        System.out.println("Nha san xuat: " + nhaSanXuat + "\nDung luong bo nho: " + dungLuongBoNho 
                + "\nMau sac: " + mauSac);
    }
    @Override
    public String toString(){
        return String.format("%s-%s-%.2f-%s-%s-%s", maHang, ten, 
                giaBan, nhaSanXuat, dungLuongBoNho, mauSac);
    }
    public static void main(String[] args) {
        DienThoai dt = new DienThoai("A1234", 
                "Iphone 7 Plus", 500000, "Ha Noi", "Den", "128GB");
        dt.hienThi();
    }
}
