package AT190344;

import java.io.Serializable;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author maima
 */
public class HoThue implements Serializable{
    String soHopDong, chuHopDong, diaChi;
    double giaDien; 
    int soDien;
    // Setter
    public void setSoHopDong(String soHopDong) {
        this.soHopDong = soHopDong;
    }

    public void setChuHopDong(String chuHopDong) {
        this.chuHopDong = chuHopDong;
    }

    public void setDiaChi(String diaChi) {
        this.diaChi = diaChi;
    }

    public void setGiaDien(double giaDien) {
        this.giaDien = giaDien;
    }

    public void setSoDien(int soDien) {
        this.soDien = soDien;
    }
    
    
    //Getter
    public String getSoHopDong() {
        return soHopDong;
    }

    public String getChuHopDong() {
        return chuHopDong;
    }

    public String getDiaChi() {
        return diaChi;
    }

    public double getGiaDien() {
        return giaDien;
    }

    public int getSoDien() {
        return soDien;
    }

    public HoThue() {
    }
    
    public HoThue(String soHopDong, String chuHopDong, String diaChi, double giaDien, int soDien) {
        this.soHopDong = soHopDong;
        this.chuHopDong = chuHopDong;
        this.diaChi = diaChi;
        this.giaDien = giaDien;
        this.soDien = soDien;
    }
    public double giaDienHangThang(){
        return giaDien*soDien;
    }
    
}
