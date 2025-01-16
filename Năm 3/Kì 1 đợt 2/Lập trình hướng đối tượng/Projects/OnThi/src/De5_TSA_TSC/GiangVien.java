/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De5_TSA_TSC;

import java.io.Serializable;

/**
 *
 * @author maima
 */
public class GiangVien implements Serializable{
    int id;
    String hoTen, maGV, diaChi, gioiTinh, khoa;
    public GiangVien() {
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setHoTen(String hoTen) {
        this.hoTen = hoTen;
    }

    public void setMaGV(String maGV) {
        this.maGV = maGV;
    }

    public void setDiaChi(String diaChi) {
        this.diaChi = diaChi;
    }

    public void setGioiTinh(String gioiTinh) {
        this.gioiTinh = gioiTinh;
    }

    public void setKhoa(String khoa) {
        if (khoa.equals("DTVT") && khoa.equals("CNTT")
                && khoa.equals("ATTT") && khoa.equals("MM") && khoa.equals("CB")){
            this.khoa = khoa;
        }
        else{
            throw new IllegalArgumentException("Khoa khong hop le! Khoa phai nam trong cac gia tri \"DTVT, CNTT, "
                    + "ATTT, MM, CB\"");
        }
    }

    public int getId() {
        return id;
    }

    public String getHoTen() {
        return hoTen;
    }

    public String getMaGV() {
        return maGV;
    }

    public String getDiaChi() {
        return diaChi;
    }

    public String getGioiTinh() {
        return gioiTinh;
    }

    public String getKhoa() {
        return khoa;
    }

    public GiangVien(int id, String hoTen, String maGV, String diaChi, String gioiTinh, String khoa) {
        if (khoa.equals("DTVT") || khoa.equals("CNTT")
                || khoa.equals("ATTT") || khoa.equals("MM") || khoa.equals("CB")){
            this.id = id;
            this.hoTen = hoTen;
            this.maGV = maGV;
            this.diaChi = diaChi;
            this.gioiTinh = gioiTinh;
            this.khoa = khoa;
        }
        else{
            throw new IllegalArgumentException("Khoa khong hop le! Khoa phai nam trong cac gia tri \"DTVT, CNTT, "
                    + "ATTT, MM, CB\"");
        }
    }
    public String hienThi(){
        return "- ID:" + id + " - Ho va ten: " + hoTen + " - Ma giang vien: "+ maGV +" - " +
                 "Dia chi: "+ diaChi + " - Gioi tinh: " + gioiTinh + " - Khoa: " + khoa + "\n" ;
    }
}
