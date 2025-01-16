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
public class SachComparator implements Comparator<SACH>{
	//Sap xep giam dan
        @Override
	public int compare(SACH s1, SACH s2){
		if(s1.thanhTien() == s2.thanhTien()) return 0;
		else if (s1.thanhTien() == s2. thanhTien()) return 1;
		else return -1;
	}
}
