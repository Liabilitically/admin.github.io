import javax.swing.*;
import java.util.Scanner;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class gui  extends JFrame{
    final private Font mainFont = new Font("Sergoe print",Font.PLAIN,12);
    private String fName,lName;
    private np [] allStocks;
    private double bal;
    private int [] amountOfShares;
    private Account account;
    JTextField tfFname,tfLname;
    JLabel lbWelcome;

    public gui(String firstName, String lastName, double balance){
        fName = firstName;
        lName = lastName;
        bal = balance;
        account = new Account(firstName,lastName,balance);
    }

    public void initialize(){

        JPanel table = new JPanel();
        table.setLayout(new GridLayout(22,3,5,5));

        Stocks stocks = new Stocks();
        allStocks = stocks.newprice();
        amountOfShares = account.getAmtShares();

        JLabel temp = new JLabel("  Current Stocks:  ");
        temp.setHorizontalAlignment(JTextField.CENTER);
        temp.setOpaque(true);
        temp.setBackground(new Color(184, 184, 184));
        temp.setFont(new Font("Sergoe print",Font.BOLD,18));
        table.add(temp);
        temp = new JLabel("  Prices:  ");
        temp.setOpaque(true);
        temp.setBackground(new Color(184, 184, 184));
        temp.setFont(new Font("Sergoe print",Font.BOLD,18));
        temp.setHorizontalAlignment(JTextField.CENTER);
        table.add(temp);
        temp = new JLabel("  Your Shares:  ");
        temp.setOpaque(true);
        temp.setBackground(new Color(184, 184, 184));
        temp.setFont(new Font("Sergoe print",Font.BOLD,18));
        temp.setHorizontalAlignment(JTextField.CENTER);
        table.add(temp);

        int i=0;
        for (np stock:allStocks){
            System.out.println(stock.getName()+":"+stock.getPrice());
            JLabel name = new JLabel("    "+stock.getName()+" ");
            name.setFont(mainFont);
            name.setHorizontalAlignment(JTextField.CENTER);
            JLabel price = new JLabel("    $"+stock.getPrice());
            price.setFont(mainFont);
            price.setHorizontalAlignment(JTextField.CENTER);
            JLabel shares = new JLabel("    "+amountOfShares[i]+" ");
            shares.setFont(mainFont);
            shares.setHorizontalAlignment(JTextField.CENTER);
            table.add(name);
            table.add(price);
            table.add(shares);
            i++;
        }
        table.add(new JLabel());
        temp = new JLabel("  Your Balance:  $"+account.getBalance()+"  ");
        temp.setOpaque(true);
        temp.setBackground(new Color(184, 6, 6));
        temp.setFont(new Font("Sergoe print",Font.BOLD,18));
        temp.setForeground(Color.WHITE);
        temp.setHorizontalAlignment(JTextField.CENTER);
        table.add(temp);
        table.add(new JLabel());
        
        JPanel form = new JPanel();
        form.setLayout(new GridLayout(4,3,5,5));
        
        JLabel text = new JLabel("Add the Stock Abbreviation:");
        text.setOpaque(true);
        text.setBackground(new Color(184, 184, 184));
        text.setFont(new Font("Sergoe print",Font.BOLD,18));
        text.setHorizontalAlignment(JTextField.CENTER);
        form.add(text);
        
        JTextField tfName = new JTextField();
        tfName.setFont(mainFont);
        tfName.setHorizontalAlignment(JTextField.CENTER);
        form.add(tfName);
        
        text = new JLabel("Add the number of stocks:");
        text.setOpaque(true);
        text.setBackground(new Color(184, 184, 184));
        text.setFont(new Font("Sergoe print",Font.BOLD,18));
        text.setHorizontalAlignment(JTextField.CENTER);
        form.add(text);
        
        JTextField tfNum = new JTextField();
        tfNum.setFont(mainFont);
        tfNum.setHorizontalAlignment(JTextField.CENTER);
        form.add(tfNum);
        
        form.add(new JLabel());
        
        JPanel buttons = new JPanel();
        buttons.setLayout(new GridLayout(1,2,5,5));
        
        JButton btnBuy = new JButton("BUY");
        JButton btnSell = new JButton("SELL");
        buttons.add(btnBuy);
        buttons.add(btnSell);
        
        form.add(buttons);
        form.add(new JLabel());

        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());
        mainPanel.add(table,BorderLayout.NORTH);
        mainPanel.add(form,BorderLayout.SOUTH);

        add(mainPanel);

        setTitle("Stock Market");
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) {
        gui myGui = new gui("John","Cena",100.0);
        myGui.initialize();
    }
}
