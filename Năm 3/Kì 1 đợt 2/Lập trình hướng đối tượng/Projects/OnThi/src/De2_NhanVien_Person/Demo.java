/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package De2_NhanVien_Person;

/**
 *
 * @author maima
 */
class Msg{
    public Msg(){
        System.out.println("Hello");
    }
    public void sayGoodBye(){
        System.out.println("Goodbye");
    }
}
class TestMsg extends Msg{
    public void sayGoodBye(){
        System.out.println("Goodbye Java");
    }
}
public class Demo {
    public static void main(String[] args) {
        Msg m1 = new Msg();
        Msg m2 = new TestMsg();
        m1.sayGoodBye();
        m2.sayGoodBye();
    }
}
