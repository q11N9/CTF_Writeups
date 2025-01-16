/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package AT190344;

/**
 *
 * @author maima
 */
public class HoDanDung extends HoThue{

    public HoDanDung() {
    }
    private double phiBaoTri;
    public double getPhiBaoTri() {
        return phiBaoTri;
    }

    public void setPhiBaoTri(double phiBaoTri) {
        this.phiBaoTri = phiBaoTri;
    }
    
    @Override
    public String getSoHopDong() {
        return soHopDong;
    }

    @Override
    public void setSoHopDong(String soHopDong) {
        this.soHopDong = soHopDong;
    }

    @Override
    public String getChuHopDong() {
        return chuHopDong;
    }

    @Override
    public void setChuHopDong(String chuHopDong) {
        this.chuHopDong = chuHopDong;
    }

    @Override
    public String getDiaChi() {
        return diaChi;
    }

    @Override
    public void setDiaChi(String diaChi) {
        this.diaChi = diaChi;
    }

    @Override
    public double getGiaDien() {
        return giaDien;
    }

    @Override
    public void setGiaDien(double giaDien) {
        this.giaDien = giaDien;
    }

    @Override
    public int getSoDien() {
        return soDien;
    }

    @Override
    public void setSoDien(int soDien) {
        this.soDien = soDien;
    }

    public HoDanDung(double phiBaoTri) {
        this.phiBaoTri = phiBaoTri;
    }

    public HoDanDung(double phiBaoTri, String soHopDong, String chuHopDong, String diaChi, double giaDien, int soDien) {
        super(soHopDong, chuHopDong, diaChi, giaDien, soDien);
        this.phiBaoTri = phiBaoTri;
    }
    @Override
    public double giaDienHangThang(){
        return giaDien*soDien + phiBaoTri;
    }
    @Override
    public String toString(){
        return "Số hợp đồng: " + soHopDong + ", Chủ hợp đồng: " + chuHopDong + 
                ", Địa chỉ: " + diaChi+ ", Giá điện cơ bản: " + giaDien + ", Số điện: "+soDien +
                ", Phí bảo trì: " + phiBaoTri + "Giá điện hàng tháng: " + giaDienHangThang();
    }
}
