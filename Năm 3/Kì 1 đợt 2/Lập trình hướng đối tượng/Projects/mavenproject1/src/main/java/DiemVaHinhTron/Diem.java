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
public class Diem {
    float x, y;
	public Diem(){
		x = 0; y = 0;
	}
	public Diem(float x, float y){
		this.x = x;
		this.y = y;
	}
	public void nhap(){
		Scanner sc = new Scanner(System.in);
		System.out.print("Nhap toa do x: ");
		x = sc.nextFloat();
		System.out.print("Nhap toa do y: ");
		y = sc.nextFloat();
	}
	public void xuat(){
		System.out.printf("x = %.2f\n", x);
		System.out.printf("y = %.2f\n", y);
	}
}
