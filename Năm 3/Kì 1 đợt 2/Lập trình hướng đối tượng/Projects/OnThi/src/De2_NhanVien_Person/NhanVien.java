/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De2_NhanVien_Person;

/**
 *
 * @author maima
 */

public class NhanVien extends Person {
    // Thuoc tinh
    private String phongBan;
    private double heSoLuong, thamNien, luongCoBan;
    private static final String[] PHONG_BAN = {"Thiết bị", "Nhân sự", "R&D", "Kinh doanh"};
    // Setter
    public void setPhongBan(String phongBan){
        // Kiem tra xem co hop le khong
        for (String pb : PHONG_BAN){
            if (pb.equals(phongBan)){
                this.phongBan = phongBan;
                return;
            }
        }
        throw new IllegalArgumentException("Phòng ban không hợp lệ!");
        
    }
    //Getter
    public String getPhongBan() {
        return phongBan;
    }

    public double getHeSoLuong() {
        return heSoLuong;
    }

    public double getThamNien() {
        return thamNien;
    }

    public double getLuongCoBan() {
        return luongCoBan;
    }

    public String getHoTen() {
        return hoTen;
    }

    public String getNgaySinh() {
        return ngaySinh;
    }

    public String getDiaChi() {
        return diaChi;
    }

    public String getGioiTinh() {
        return gioiTinh;
    }
    // Constructor
    public NhanVien(String hoTen, String ngaySinh, String diaChi, String gioiTinh, 
            String phongBan, double heSoLuong, double thamNien, double luongCoBan) {
        super(hoTen, ngaySinh, diaChi, gioiTinh);
        this.phongBan = phongBan;
        this.heSoLuong = heSoLuong;
        this.thamNien = thamNien;
        this.luongCoBan = luongCoBan;
    }
    public void hienThi(){
        System.out.printf("Họ tên: %s - Ngày sinh: %s - Địa chỉ: %s - Giới tính: %s"
                + "Phòng ban: %s - Hệ số lương: %.2f - Thâm niên: %.2f - Lương cơ bản: %.2f - Lương thực lĩnh: %.2f"
                , hoTen, ngaySinh, diaChi, gioiTinh, phongBan,
                heSoLuong, thamNien, luongCoBan);
    }
    public double luongThucLinh(){
        return luongCoBan*heSoLuong*(1+thamNien/100);
    }
    // Hàm toString để phục vụ cho ghi file
    @Override
    public String toString(){
        return String.format("%s-%s-%s-%s-%s-%.2f-%.2f-%.2f-%.2f", hoTen, ngaySinh, 
                diaChi, gioiTinh, phongBan, heSoLuong, thamNien, luongCoBan, 
                String.valueOf(this.luongThucLinh()));
    }
 
}
