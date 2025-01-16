/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package AT190344;

/**
 *
 * @author maima
 */
public class HoKinhDoanh extends HoThue{

    public void setThueKinhDoanh(double thueKinhDoanh) {
        this.thueKinhDoanh = thueKinhDoanh;
    }
    private double thueKinhDoanh;
    public double getThueKinhDoanh() {
        return thueKinhDoanh;
    }

    @Override
    public String getSoHopDong() {
        return soHopDong;
    }

    @Override
    public String getChuHopDong() {
        return chuHopDong;
    }

    @Override
    public String getDiaChi() {
        return diaChi;
    }

    @Override
    public double getGiaDien() {
        return giaDien;
    }

    @Override
    public int getSoDien() {
        return soDien;
    }

    public HoKinhDoanh(double thueKinhDoanh) {
        this.thueKinhDoanh = thueKinhDoanh;
    }

    public HoKinhDoanh(String soHopDong, String chuHopDong, String diaChi, double giaDien, int soDien, double thueKinhDoanh) {
        super(soHopDong, chuHopDong, diaChi, giaDien, soDien);
        this.thueKinhDoanh = thueKinhDoanh;
    }

    public HoKinhDoanh() {
    }
    
    @Override
    public double giaDienHangThang(){
        return giaDien*soDien*thueKinhDoanh;
    }
    @Override 
    public String toString(){
        return "Số hợp đồng: " + soHopDong + ", Chủ hợp đồng: " + chuHopDong + 
                ", Địa chỉ: " + diaChi+ ", Giá điện cơ bản: " + giaDien + ", Số điện: "+soDien +
                ", Thuế kinh doanh: " + thueKinhDoanh + ", Giá điện hàng tháng: " + giaDienHangThang();
    }
}
