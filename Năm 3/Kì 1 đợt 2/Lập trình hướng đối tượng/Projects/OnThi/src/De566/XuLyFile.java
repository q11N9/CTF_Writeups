/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De566;

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
    private static final String FILE_NAME = "dic.data";
    // Doc du lieu tu file
    public static List<TuVung> docFile(){
        File file = new File(FILE_NAME);
        if(!file.exists()) return new ArrayList<>();
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(FILE_NAME))){
            return (List<TuVung>) ois.readObject();
        }catch (Exception e){
            e.printStackTrace();
            return new ArrayList<>();
        }
    }
    // Ghi du lieu vao file
    public static void ghiFile(List<TuVung> tuVungList){
        try(ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(FILE_NAME))){
            oos.writeObject(tuVungList);
        }catch (IOException e){
            e.printStackTrace();
        }  
    }
    // Tim tu theo tieng Anh
    public static TuVung timTheoTiengAnh(String tiengAnh){
        List<TuVung> tuVungList = docFile();
        for (TuVung tv : tuVungList){
            if (tv.getTiengAnh().equals(tiengAnh))
                return tv;
        }
        return null;
    }
    // Them tu moi
    // Tao mot ham de tu dong tao ID
    public static int taoID(){
        // Doc du lie tu file
        List<TuVung> tuVungList = docFile();
        // Kiem tra xem danh sach co trong hay khong
        if (tuVungList.isEmpty()){
            return 1; // ID mới sẽ bắt đầu từ 1
        }
        // Tìm xem trong danh sách vừa đọc ID lớn nhất
        int maxID = 0;
        for (TuVung tv : tuVungList){
            if (tv.getId() > maxID) maxID = tv.getId();
        }
        return maxID + 1;
    }
    // Kiem tra trung lap
    public static boolean kiemTraTrungLap(String tiengAnh){
        List<TuVung> tuVungList = docFile();
        for (TuVung tv : tuVungList){
            if (tv.getTiengAnh().equalsIgnoreCase(tiengAnh)) return true;
            // Từ đã có trong từ điển
        }
        return false;   // Từ chưa có trong từ điển
    }
    public static void themTuMoi(TuVung tuVung){
        List<TuVung> tuVungList = docFile();
        tuVungList.add(tuVung);
        ghiFile(tuVungList);
    }
    // Sua thong tin
    public static void suaTu(String tiengAnh, String nghiaMoi){
        List<TuVung> tuVungList = docFile();
        for (TuVung tv : tuVungList){
            if (tv.getTiengAnh().equalsIgnoreCase(tiengAnh)){
                tv.setTiengViet(nghiaMoi);
                break;
            }
        }
        ghiFile(tuVungList);
    }
}
