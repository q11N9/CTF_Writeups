/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DiemVaHinhTron;

/**
 *
 * @author maima
 */
import java.util.*;
public class HinhTron extends Diem{
    float R;
	public HinhTron(){
		super();
		R = 0;
	}
	public HinhTron(float R, float x, float y){
		super(x,y);
		this.R = R;
	}
	public void nhapHT(){
		Scanner sc = new Scanner(System.in);
		super.nhap();
		System.out.print("Nhap ban kinh: ");
		R = sc.nextFloat();
	}
	public void xuatHT(){
		super.xuat();
		System.out.printf("\nBan kinh: %.2f", R);
		System.out.printf("\nDien tich: %.2f", dienTich());
	}
	public float dienTich(){
		return (float)Math.PI*R*R;
	}
}
