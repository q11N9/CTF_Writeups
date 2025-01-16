/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package QLSV;

/**
 *
 * @author maima
 */
import java.util.ArrayList;
import java.util.Scanner;
import java.io.*;
public class DSSinhVien{
	private final ArrayList<SinhVien> danhSach;
	public DSSinhVien(){
		danhSach = new ArrayList<>();
	}
	public void nhapDanhSach(){
		Scanner sc = new Scanner(System.in);
		while (true){
			System.out.println("1. Nhap sinh vien ATTT");
			System.out.println("2. Nhap sinh vien Mat ma");
			System.out.println("0. Ket thuc nhap");
			int choice = sc.nextInt();
			sc.nextLine();
			if (choice == 0) break;
			SinhVien sv = null;
			if (choice == 1) sv = new SinhVienATTT();
			else sv = new SinhVienMatMa();
			if (sv != null){
				sv.nhap();
				danhSach.add(sv);
			}

		}

	}
	public void inDanhSach(){
		for (SinhVien sv : danhSach){
			sv.hienThi();
		}
	}
	public void luuSinhVien(String fileName) throws IOException{
		ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName));
		oos.writeObject(danhSach);
		oos.close();
	}
	public void luuTheoLoai() throws IOException{
            ObjectOutputStream oosMatMa;
            try (ObjectOutputStream oosATTT = new ObjectOutputStream(new FileOutputStream("svat.dat"))) {
                oosMatMa = new ObjectOutputStream(new FileOutputStream("svmm.dat"));
                ArrayList<SinhVien> svATTT = new ArrayList<>();
                ArrayList<SinhVien> svMatMa = new ArrayList<>();
                for (SinhVien sv : danhSach){
                    if (sv instanceof SinhVienATTT) svATTT.add(sv);
                    else if (sv instanceof SinhVienMatMa) svMatMa.add(sv);
                }
                oosATTT.writeObject(svATTT);
                oosMatMa.writeObject(svMatMa);
            }
		oosMatMa.close();
	}
	public void suaThongTin(String maSinhVien){
		Scanner sc = new Scanner(System.in);
		for (SinhVien sv : danhSach){
			if (sv.getMaSinhVien().equals(maSinhVien)){
				System.out.print("Nhap ho ten moi: ");
				sv.setHoTen(sc.nextLine());
				System.out.print("Nhap ngay sinh moi: ");
				sv.setNgaySinh(sc.nextLine());
				System.out.println("Cap nhat thanh cong. ");
				return;
			}
		}
		System.out.println("Khong tim thay sinh vien voi ma: " + maSinhVien);
	}
}