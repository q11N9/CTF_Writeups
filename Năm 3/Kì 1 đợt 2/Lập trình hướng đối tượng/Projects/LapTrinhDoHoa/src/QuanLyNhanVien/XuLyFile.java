/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package QuanLyNhanVien;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author maima
 */
public class XuLyFile {
    private static final String FILE_NAME = "nhanvien.dat";

    // Ghi nhân viên vào file (thêm vào cuối file) với định dạng mong muốn
    public static void saveToFile(NhanVien nv) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(FILE_NAME, true))) {
            String line = "- " + nv.getMaNV() + ", " + nv.getHoTen() + ", " + nv.getDienThoai() + ", " 
                          + nv.getHeSoLuong() + ", " + nv.getLuong();
            writer.write(line);
            writer.newLine(); // Xuống dòng sau mỗi nhân viên
        }
    }

    // Đọc danh sách nhân viên từ file với định dạng mong muốn
    public static List<NhanVien> readFromFile() throws IOException {
        List<NhanVien> danhSach = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(FILE_NAME))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.startsWith("- ")) { // Bỏ qua nếu không đúng định dạng
                    line = line.substring(2); // Bỏ dấu "- " ở đầu dòng
                    String[] parts = line.split(", ");
                    if (parts.length == 5) {
                        String maNV = parts[0];
                        String hoTen = parts[1];
                        String dienThoai = parts[2];
                        double heSoLuong = Double.parseDouble(parts[3]);
                        NhanVien nv = new NhanVien(maNV, hoTen, dienThoai, heSoLuong);
                        danhSach.add(nv);
                    }
                }
            }
        }
        return danhSach;
    }
}
