
import java.awt.Button;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.Label;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author maima
 */
public class BieuDo_Frame extends Frame implements ActionListener{
    Label lb1, lb2, lb3, lb4; 
    TextField txtRed, txtBlue, txtGreen, txtPink; 
    Button btnVe, btnThoat;
    
    int rr, bb, gg, pp; 
    public BieuDo_Frame(){
        lb1 = new Label("Red: ");
        lb2 = new Label("Blue: ");
        lb3 = new Label("Green: ");
        lb4 = new Label("Pink: ");
        txtRed = new TextField("70", 5);
        txtBlue = new TextField("50", 5);
        txtGreen = new TextField("100", 5);
        txtPink = new TextField("80", 5);
        btnVe = new Button("Draw");
        btnThoat = new Button("Exit");

        btnVe.addActionListener(this);
        btnThoat.addActionListener(this);
        setLayout(new FlowLayout());
        add(lb1);add(txtRed);
        add(lb2);add(txtBlue);
        add(lb3);add(txtGreen);
        add(lb4);add(txtPink);
        add(btnVe);add(btnThoat);
        rr = Integer.parseInt(txtBlue.getText());
        bb = Integer.parseInt(txtBlue.getText());
        gg = Integer.parseInt(txtGreen.getText());
        pp = Integer.parseInt(txtPink.getText());
        addWindowListener(new WindowAdapter(){
            @Override
            public void windowClosing(WindowEvent e){
                System.exit(0);
            }
        });
    }
    @Override
    public void paint(Graphics g){
        g.drawLine(50, 50, 50, 250);
        g.drawLine(50, 250, 350, 250);
        
        g.setColor(Color.red);
        g.fillRect(70, 250-rr, 30, rr);
        g.drawString(String.valueOf(rr), 70, 250-rr);
        
        g.setColor(Color.blue);
        g.fillRect(130, 250-bb, 30, bb);
        g.drawString(String.valueOf(bb), 130, 250-rr);
        
        g.setColor(Color.green);
        g.fillRect(190, 250-gg, 30, gg);
        g.drawString(String.valueOf(gg), 190, 250-gg);
        
        g.setColor(Color.pink);
        g.fillRect(250, 250-pp, 30, pp);
        g.drawString(String.valueOf(pp), 250, 250-pp);
    }
    @Override
    public void actionPerformed(ActionEvent e){
        rr = Integer.parseInt(txtRed.getText());
        bb = Integer.parseInt(txtBlue.getText());
        gg = Integer.parseInt(txtGreen.getText());
        pp = Integer.parseInt(txtPink.getText());
        
        if (e.getSource() == btnVe){
            repaint();
        }
        if (e.getSource() == btnThoat){
            System.exit(0);
        }
    }
    public static void main(String[] args) {
        BieuDo_Frame t = new BieuDo_Frame();
        t.setSize(400, 300);
        t.setVisible(true);
    }
}
