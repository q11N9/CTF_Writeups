/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De2_NhanVien_Person;

import De1_DienThoai.DienThoai;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author maima
 */
public class XuLyFile {
    // Lưu dữ liệu vào file
    public static void luuFile(String tenFile, List<NhanVien> nvList) throws IOException{
        try(BufferedWriter writer = new BufferedWriter(new FileWriter(tenFile))){
            for (NhanVien nv : nvList){
                // Ghi vao file
                writer.write(nv.toString());
                writer.newLine();
            }
        }
    }
    // Đọc dữ liệu từ file
    public static List<NhanVien> docFile(String tenFile) throws IOException{
        List<NhanVien> nvList = new ArrayList<>();
        try(BufferedReader reader = new BufferedReader(new FileReader(tenFile))){
            String line;
            while((line = reader.readLine()) != null){
                String[] phanTu = line.split("-");
                if (phanTu.length == 9){
                    NhanVien nv = new NhanVien( phanTu[0], phanTu[1], phanTu[2], 
                                                phanTu[3], phanTu[4], Double.parseDouble(phanTu[5]), 
                                                Double.parseDouble(phanTu[6]), 
                                                Double.parseDouble(phanTu[7]));
                }
            }
        }
        return nvList;
    }
}
