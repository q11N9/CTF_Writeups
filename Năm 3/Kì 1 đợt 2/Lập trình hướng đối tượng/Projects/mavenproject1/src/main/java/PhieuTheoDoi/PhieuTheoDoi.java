/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package PhieuTheoDoi;

/**
 *
 * @author maima
 */
import java.util.*;
public class PhieuTheoDoi{
    private String soPhieu;
    private String ngayLap;
    private PhongHoc phongHoc;
    private ArrayList<ThietBi> DSThietBi;

    public void nhapPhieu(){		// Nhap danh sach cac phieu theo doi
            Scanner sc = new Scanner(System.in);
            System.out.print("Nhap ma so phieu: ");
            String soPhieu = sc.nextLine();
            System.out.println("Nhap thong tin phong hoc can quan ly: ");
            this.phongHoc = new PhongHoc();
            System.out.print("Nhap so luong thiet bi: ");
            int soLuongThietBi = sc.nextInt();
            for(int i = 1; i <= soLuongThietBi; i++){
                    System.out.printf("Thong tin thiet bi so %d\n", i);
                    ThietBi thietBi = new ThietBi();
                    DSThietBi.add(thietBi);
            }
    }

    public void inPhieu(){		// In danh sach cac phieu da nhap
            System.out.println("So phieu: " + soPhieu);
            phongHoc.inTTPhong();
            System.out.println("TT\tTen Thiet Bi   Hang SX - Nuoc SX   Ngay nhap   So luong   Don gia   Thanh tien");
            int count = 1;
            for (ThietBi thietBi : DSThietBi){
                    System.out.print(count);
                    thietBi.inTTThietBi();
            }
    }
}
