/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package ViduMinhHoa;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author maima
 */
public class NhanVienModelTable extends AbstractTableModel {
    private final ArrayList<NhanVien> lstNV;
    private final String[] columnName = new String[]{"Họ Tên", "Ngày Sinh", "Địa Chỉ", 
                                                    "Giới Tính", "Phòng Ban", "Hệ Số Lương", "Thâm Niên", "Thực Lĩnh"};
    public NhanVienModelTable(ArrayList<NhanVien> lstNV){
        this.lstNV = lstNV;
    }
    @Override
    public int getRowCount(){
        return lstNV.size();
    }
    @Override
    public int getColumnCount(){
        return columnName.length;
    }
    @Override
    public Object getValueAt(int rowIndex, int columnnIndex){
        NhanVien nv = lstNV.get(rowIndex);
        switch (columnnIndex) {
            case 0 -> {
                return nv.getHoTen();
            }
            case 1 -> {
                return nv.getNgaySinh();
            }
            case 2 -> {
                return nv.getDiaChi();
            }
            case 3 -> {
                return nv.getGioiTinh();
            }
            case 4 -> {
                return nv.getPhongBan();
            }
            case 5 -> {
                return nv.getHeSoLuong();
            }
            case 6 -> {
                return nv.getThamNien();
            }
            case 7 -> {
                return nv.tinhLuong();
            }
            default -> {
            }
        }
        return nv;
    }
    @Override
    public String getColumnName(int col){
        return columnName[col];
    }
    public NhanVien getNhanVienIndex(int k){
        return lstNV.get(k);
    }
}
