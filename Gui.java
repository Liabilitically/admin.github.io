import javax.swing.*;
import java.util.Scanner;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Gui  extends JFrame{
    final private Font mainFont = new Font("Sergoe print",Font.PLAIN,12);
    private String fName,lName;
    private np [] allStocks;
    private double bal;
    private int [] amountOfShares;
    private Account account;
    JTextField tfFname,tfLname;
    JLabel lbWelcome;

    public Gui(String firstName, String lastName, double balance){
        fName = firstName;
        lName = lastName;
        bal = balance;
        account = new Account(firstName,lastName,balance);
    }

    public void initialize(){

        JPanel table = new JPanel();
        table.setLayout(new GridLayout(22,4,5,5));

        Stocks stocks = new Stocks();
        allStocks = stocks.newprice();
        amountOfShares = account.getAmtShares();

        JLabel temp = new JLabel("  Current Stocks:  ");
        temp.setOpaque(true);
        temp.setBackground(new Color(184, 184, 184));
        temp.setFont(new Font("Sergoe print",Font.BOLD,18));
        table.add(temp);
        temp = new JLabel("  Prices:  ");
        temp.setOpaque(true);
        temp.setBackground(new Color(184, 184, 184));
        temp.setFont(new Font("Sergoe print",Font.BOLD,18));
        table.add(temp);
        temp = new JLabel("  Your Shares:  ");
        temp.setOpaque(true);
        temp.setBackground(new Color(184, 184, 184));
        temp.setFont(new Font("Sergoe print",Font.BOLD,18));
        table.add(temp);
        table.add(new JLabel());

        int i=0;
        for (np stock:allStocks){
            System.out.println(stock.getName()+":"+stock.getPrice());
            JLabel name = new JLabel("    "+stock.getName()+" ");
            name.setFont(mainFont);
            JLabel price = new JLabel("    $"+stock.getPrice());
            price.setFont(mainFont);
            JLabel shares = new JLabel("    "+amountOfShares[i]+" ");
            shares.setFont(mainFont);
            JButton buy = new JButton("BUY");
            buy.setFont(mainFont);
            table.add(name);
            table.add(price);
            table.add(shares);
            table.add(buy);
            i++;
        }

        temp = new JLabel("  Your Balance:  ");
        temp.setOpaque(true);
        temp.setBackground(new Color(184, 6, 6));
        temp.setFont(new Font("Sergoe print",Font.BOLD,18));
        temp.setForeground(Color.WHITE);
        table.add(temp);
        table.add(new JLabel());

        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());
        mainPanel.add(table,BorderLayout.WEST);

        add(mainPanel);

        setTitle("Stock Market");
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) {
        Gui myGui = new Gui("John","Cena",100.0);
        myGui.initialize();
    }
}
