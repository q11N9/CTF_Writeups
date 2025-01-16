/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De566;

import java.io.Serializable;

/**
 *
 * @author maima
 */
public class TuVung implements Serializable{
    private int id;
    private String tiengAnh, tiengViet;
    public TuVung() {
    }

    public TuVung(int id, String tiengAnh, String tiengViet) {
        this.id = id;
        this.tiengAnh = tiengAnh;
        this.tiengViet = tiengViet;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setTiengAnh(String tiengAnh) {
        this.tiengAnh = tiengAnh;
    }

    public void setTiengViet(String tiengViet) {
        this.tiengViet = tiengViet;
    }

    public int getId() {
        return id;
    }

    public String getTiengAnh() {
        return tiengAnh;
    }

    public String getTiengViet() {
        return tiengViet;
    }
    
    @Override
    public String toString(){
        return "ID: " + id + ", Tieng Anh: " + tiengAnh + ", Tieng Viet: " + tiengViet;
    }
}
