/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De6_Category_Book;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.List;

/**
 *
 * @author maima
 */
public class XuLyFile {
    public static void nhapFile(String filename, List<Book> bookList){
        try{
            File file = new File(filename);
            PrintWriter printWriter = new PrintWriter(file);
            for (Book b : bookList){
                printWriter.printf("%s-%s-%s-%s\n", 
                        b.getId(), b.getAuthors(), b.getTitle(), b.getCategory().getType()); 
            }
        printWriter.close();
        }catch(FileNotFoundException ex){
            
        } 
    }
    public static List<Book> docFile(String filename){
        return null;
    }
}
