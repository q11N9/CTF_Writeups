/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ruong;

/**
 *
 * @author maima
 */
import java.util.ArrayList;
import java.util.List;

// Base Class
class Ruong {
    private String name;

    public Ruong(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Ruong: " + name;
    }
}

// Subclass 1: Square Chest
class RuongVuong extends Ruong {
    private double sideLength;

    public RuongVuong(String name, double sideLength) {
        super(name);
        this.sideLength = sideLength;
    }

    public double getSideLength() {
        return sideLength;
    }

    @Override
    public String toString() {
        return super.toString() + ", Side Length: " + sideLength;
    }
}

// Subclass 2: Rectangle Chest
class RuongChuNhat extends Ruong {
    private double width;
    private double height;

    public RuongChuNhat(String name, double width, double height) {
        super(name);
        this.width = width;
        this.height = height;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }

    @Override
    public String toString() {
        return super.toString() + ", Width: " + width + ", Height: " + height;
    }
}

public class Main {
    public static void main(String[] args) {
        // List of Ruong
        List<Ruong> ruongList = new ArrayList<>();

        // Add objects of different types
        ruongList.add(new Ruong("Generic Ruong"));
        ruongList.add(new RuongVuong("Square Ruong 1", 5.0));
        ruongList.add(new RuongChuNhat("Rectangle Ruong 1", 4.0, 6.0));
        ruongList.add(new RuongVuong("Square Ruong 2", 7.0));
        ruongList.add(new RuongChuNhat("Rectangle Ruong 2", 3.0, 8.0));

        // Separate and print each type
        System.out.println("== RuongVuong List ==");
        for (Ruong ruong : ruongList) {
            if (ruong instanceof RuongVuong) {
                RuongVuong square = (RuongVuong) ruong;
                System.out.println(square);
            }
        }

        System.out.println("\n== RuongChuNhat List ==");
        for (Ruong ruong : ruongList) {
            if (ruong instanceof RuongChuNhat) {
                RuongChuNhat rectangle = (RuongChuNhat) ruong;
                System.out.println(rectangle);
            }
        }

        System.out.println("\n== Generic Ruong List ==");
        for (Ruong ruong : ruongList) {
            if (!(ruong instanceof RuongVuong) && !(ruong instanceof RuongChuNhat)) {
                System.out.println(ruong);
            }
        }
    }
}
