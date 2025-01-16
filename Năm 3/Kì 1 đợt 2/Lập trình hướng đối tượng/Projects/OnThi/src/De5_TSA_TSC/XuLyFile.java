/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De5_TSA_TSC;

import java.io.EOFException;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author maima
 */
public class XuLyFile {
    private static final String FILE_NAME = "./giangvien.dat";
    // Doc du lieu tu file
    public static List<GiangVien> docFile(){
        File file = new File("giangvien.dat"); 
        if (!file.exists()) {
            System.out.println("File not found. Returning an empty list.");
            return new ArrayList<>();
        }

        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file))) {
           
            return (List<GiangVien>) ois.readObject();
        } catch (EOFException e) {
            System.out.println("File is empty. Returning an empty list.");
            return new ArrayList<>(); 
        } catch (IOException e) {
            System.out.println("Error reading the file: " + e.getMessage());
            e.printStackTrace();
            return new ArrayList<>(); 
        } catch (ClassNotFoundException e) {
            System.out.println("Class not found: " + e.getMessage());
            e.printStackTrace();
            return new ArrayList<>();
        }
               
    }
    // Ghi 1 danh sach vao file
    public static void ghiGVListFile(List<GiangVien> gvList){
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(FILE_NAME))){
            oos.writeObject(gvList);
        }catch (IOException e){
            System.out.println("Loi khi ghi file " + e.getMessage());
        }
    }
    // Ghi 1 GiangVien vao file
    public static boolean ghiGVFile(GiangVien new_gv){
        // Lay list GiangVien ra khoi file
        List<GiangVien> gvList = docFile();
        
        // Kiem tra xem ID da ton tai hay chua
        for (GiangVien gv : gvList){
            if (gv.getId() == new_gv.getId()){
                System.out.println("Giang vien da ton tai!");
                return false;
            }
        }
        // Ghi giang vien vao list va ghi vao file
        gvList.add(new_gv);
        ghiGVListFile(gvList);
        System.out.println("Ghi file thanh cong!");
        return true;
    }
    
    // Tim mot GiangVien theo ten
    public static List<GiangVien> timGVTheoTen(String hoTen){
        List<GiangVien> gvList = docFile();
        // Tao ra mot list de luu tru thong tin da tim kiem
        List<GiangVien> gvInfo = new ArrayList<>();
        for (GiangVien gv : gvList){
            if (gv.getHoTen().equals(hoTen)){
                gvInfo.add(gv);
            }
        }
        return gvInfo;
    }
}
