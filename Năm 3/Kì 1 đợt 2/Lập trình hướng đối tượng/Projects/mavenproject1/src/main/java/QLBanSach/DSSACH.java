/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package QLBanSach;

/**
 *
 * @author maima
 */
import java.util.*;
public class DSSACH{
	ArrayList<SACH> lstSach = new ArrayList();
	public void nhapDSSach() 
	{
		int n;
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhap so sach: ");
		n = sc.nextInt();
		for(int i =0; i < n;i++){
			SACH s = new SACH();
			System.out.printf("Thong tin quyen sach so " + (i + 1));
			s.nhapSach();
			lstSach.add(s);
		}
	}
	public void inDSSach(){
		System.out.print("\nDanh sach da nhap: \n");
		int i = 0;
		for(SACH s:lstSach) {
			System.out.printf("Thong tin quyen sach so " + (i + 1));
			s.inSach();
			i += 1;
		}
	}
	public void tongTienSach(){
		float sum =0;
		for (SACH s:lstSach) sum = sum + s.thanhTien();
		System.out.print("\nTong tien sach: " + sum);
	}
	public void sapXepDSSachTangDanThanhTien(){
		Collections.sort(lstSach, new SachComparator());
		inDSSach();
	}
}
