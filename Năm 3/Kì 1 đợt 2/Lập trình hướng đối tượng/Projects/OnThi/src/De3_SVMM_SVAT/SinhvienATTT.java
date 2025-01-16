/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De3_SVMM_SVAT;

/**
 *
 * @author maima
 */
public class SinhvienATTT extends Sinhvien{
    private double hocphi;

    public SinhvienATTT() {
    }
    
    public SinhvienATTT(double hocphi, String Masv, String hoten, String gioitinh, String ngaysinh, String diachi, double DTB) {
        super(Masv, hoten, gioitinh, ngaysinh, diachi, DTB);
        this.hocphi = hocphi;
    }

    public double getHocphi() {
        return hocphi;
    }

    public void setHocphi(double hocphi) {
        this.hocphi = hocphi;
    }
    @Override
    public void Hienthitt(){
        super.Hienthitt();
        System.out.println("hoc phi : "+getHocphi());
    }
}
