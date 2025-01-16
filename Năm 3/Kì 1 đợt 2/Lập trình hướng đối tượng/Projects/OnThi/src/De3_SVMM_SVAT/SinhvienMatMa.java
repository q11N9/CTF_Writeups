/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De3_SVMM_SVAT;

/**
 *
 * @author maima
 */
public class SinhvienMatMa extends Sinhvien {
    private double donviluong;

    public SinhvienMatMa() {
    }
    
    public SinhvienMatMa(double donviluong, String Masv, String hoten, String gioitinh, String ngaysinh, String diachi, double DTB) {
        super(Masv, hoten, gioitinh, ngaysinh, diachi, DTB);
        this.donviluong = donviluong;
    }

    public double getDonviluong() {
        return donviluong;
    }

    public void setDonviluong(double donviluong) {
        this.donviluong = donviluong;
    }
    @Override
    public void Hienthitt(){
        super.Hienthitt();
        System.out.print("don vi luong : "+getDonviluong());
    }
}
