/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De1_DienThoai;

import java.util.List;
import java.util.ArrayList;
import java.io.*;

/**
 *
 * @author maima
 */
public class XuLyFile {
    // Lưu data vào file
    public static void luuFile(String tenFile, List<DienThoai> dienThoaiList) throws IOException{
        try(BufferedWriter writer = new BufferedWriter(new FileWriter(tenFile))){
            for (DienThoai dt : dienThoaiList){
                // Ghi vào file
                writer.write(dt.toString());
                writer.newLine();
            }
        }
    }
    // Đọc data từ file
    public static List<DienThoai> docFile(String fileName) throws IOException{
        List<DienThoai> dienThoaiList = new ArrayList<>();
        try(BufferedReader reader = new BufferedReader(new FileReader (fileName))){
            // Đọc từng dòng, phân cách các phần tử bằng - 
            String line; 
            while((line = reader.readLine()) != null){
                String[] phanTu = line.split("-");
                if (phanTu.length == 6){
                    DienThoai dt = new DienThoai(phanTu[0], phanTu[1], 
                            Double.parseDouble(phanTu[2]), phanTu[3], phanTu[4], phanTu[5]);
                    dienThoaiList.add(dt);
                }
            }
        }
        return dienThoaiList;
    }
    
}
