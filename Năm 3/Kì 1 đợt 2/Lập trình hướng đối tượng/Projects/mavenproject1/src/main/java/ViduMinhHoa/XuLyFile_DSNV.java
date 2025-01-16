/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ViduMinhHoa;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

/**
 *
 * @author maima
 */
public class XuLyFile_DSNV {
    public static void luuDSNVFile(ArrayList<NhanVien> dsNV){
        try {
            File f = new File("nhanvien.txt");
            FileWriter fw = new FileWriter(f);
            for (NhanVien x : dsNV){
                fw.write(x.toString() + "\n");
            }
            fw.close();
            System.out.println("\n Ghi file thanh cong!");
        } catch (IOException e) {
            System.out.println("\n Loi ghi file: " + e);
        }
    }
    public static ArrayList<NhanVien> docDSNVFile(){
        ArrayList<NhanVien> dsNV = new ArrayList<NhanVien>();
        try {
            File f = new File("nhanvien.txt");
            BufferedReader br;
            try (FileReader fr = new FileReader(f)) {
                br = new BufferedReader(fr);
                String line;
                while((line = br.readLine()) != null){
                    NhanVien x = new NhanVien(line);
                    dsNV.add(x);
                }
            }
            br.close();
            System.out.println("Doc file thanh cong!");
        } catch (IOException e) {
            System.out.println("Loi doc file: " + e);
        }
        return dsNV;
    }
}
