/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package QuanLyNhanVien;

/**
 *
 * @author maima
 */
import java.util.*;
import java.io.*;
public class XuLyFile_DSNV_DataObject{
	public static void luuFileDSNV(ArrayList<NhanVien> dsNV)
		throws FileNotFoundException, IOException
	{
		File fName = new File("./dsnhanvien.dat");
		FileOutputStream fout = new FileOutputStream(fName);
		ObjectOutputStream out = new ObjectOutputStream(fout);
		out.writeObject(dsNV);
		out.close();
		fout.close();
	}
	public static ArrayList<NhanVien> docFileDSNV()
		throws FileNotFoundException, IOException, ClassNotFoundException
	{
		File fName = new File("./dsnhanvien.dat");
		ArrayList<NhanVien> dsNV = new ArrayList<NhanVien>();
		FileInputStream fin = new FileInputStream(fName);
		ObjectInputStream in = new ObjectInputStream(fin);
		dsNV = (ArrayList<NhanVien>)in.readObject();
		in.close();
		fin.close();
		return dsNV;
	}
}