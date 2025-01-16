/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De6_Category_Book;

/**
 *
 * @author maima
 */
public class Book {
    private String id , authors , title;
    private Category category;

    public Book(String id, String authors, String title, String category) {
        this.id = id;
        this.authors = authors;
        this.title = title;
        if(category.compareToIgnoreCase("KHXH") == 0)
        {
            this.category = new Category( category );
        }else if(category.compareToIgnoreCase("KHTN")==0)
        {
            this.category = new Category( category );
        }else if(category.compareToIgnoreCase("Luan Van")==0)
        {
            this.category = new Category( category );
        }else if(category.compareToIgnoreCase("Tap chi")==0)
        {
            this.category = new Category( category );
        }
    }

    public Book() {
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getAuthors() {
        return authors;
    }

    public void setAuthors(String authors) {
        this.authors = authors;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Category getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = new Category(category);
    }
}
