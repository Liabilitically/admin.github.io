import javax.swing.*;
import java.util.Scanner;
import java.util.function.ToIntBiFunction;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.*;
import static java.util.concurrent.TimeUnit.SECONDS;

public class Stock_Market extends JFrame implements ActionListener,Runnable
{
    private final Font mainFont = new Font("Sergoe print",Font.PLAIN,12);
    private String fName,lName;
    private np [] allStocks;
    private double bal;
    private int [] amountOfShares;
    private Account account;
    private JLabel tm;
    private int timerCnt = 30;
    private static int currentTimer = 30;
    private String[] abbrev = {"MSFT","GOOG","SNAP","F","T","TSLA","AAPL","AMZN","WMT","COST","AMD","COIN","BRK","MCD","GME","BBY","META","DFS","WM","DELL"};
    private int[] update = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    private JTextField tfFname,tfLname;
    private JLabel lbWelcome;
    private JPanel displayTablePanel;
    private JTextField tfStockName, tfShareCount;
    private JButton btnBuy, btnSell, btnRefresh;
    private JPanel mainPanel;
    private String[][] stockData;
    private final int MaxStocks = 20;
    private final int TotalRows = 22;
    private final int TotalColumns = 3;
    private final int HeaderRow = 0;

    public Stock_Market(String firstName, String lastName, double balance){
        fName = firstName;
        lName = lastName;
        bal = balance;
        account = new Account(firstName,lastName,balance);
    }

    public void initialize()
    {
        Stocks stocks = new Stocks();
        allStocks = stocks.newprice();
        

        stockData = new String[MaxStocks][3];

        PrepareDisplayData();

        // Create Buy button and add listener
        btnBuy = new JButton("BUY");
        btnBuy.addActionListener(this);

        // Create Sell button and add listener
        btnSell = new JButton("SELL");
        btnSell.addActionListener(this);
        
        btnRefresh = new JButton("REFRESH");
        btnRefresh.addActionListener(this);

        // mainPanel = new JPanel();

        UpdatePanel();

    }

    private void PrepareDisplayData()
    {
        // String[][] displayData = new String[MaxStocks][3];

        amountOfShares = account.getAmtShares();

        int rowNo = 0;

        for (np stock:allStocks)
        {
            // Add stock name
            stockData[rowNo][0] = stock.getName();

            // Add price
            stockData[rowNo][1] = String.valueOf(stock.getPrice());

            // Add shares count
            stockData[rowNo][2] = String.valueOf(amountOfShares[rowNo]);

            rowNo++;
        }

    }

    private void UpdatePanel()
    {
        displayTablePanel = new JPanel();
        displayTablePanel.setLayout(new GridLayout(TotalRows, TotalColumns, 5, 5));

        JLabel lbl;

        // Add column #1 ('Stocks') header text
        lbl = new JLabel("Stocks");
        lbl.setHorizontalAlignment(JTextField.CENTER);
        lbl.setOpaque(true);
        lbl.setBackground(new Color(184, 184, 184));
        lbl.setFont(new Font("Sergoe print",Font.BOLD,18));
        displayTablePanel.add(lbl);

        // Add column #2 ('Price') header text
        lbl = new JLabel("Price");
        lbl.setOpaque(true);
        lbl.setBackground(new Color(184, 184, 184));
        lbl.setFont(new Font("Sergoe print",Font.BOLD,18));
        lbl.setHorizontalAlignment(JTextField.CENTER);
        displayTablePanel.add(lbl);

        //Add column #3 ('Shares') header text
        lbl = new JLabel("Shares");
        lbl.setOpaque(true);
        lbl.setBackground(new Color(184, 184, 184));
        lbl.setFont(new Font("Sergoe print",Font.BOLD,18));
        lbl.setHorizontalAlignment(JTextField.CENTER);
        displayTablePanel.add(lbl);

        for(int stockCnt = 0; stockCnt < MaxStocks; stockCnt++)
        {
            // Add stock name in column 1
            lbl = new JLabel(stockData[stockCnt][0]);
            lbl.setFont(mainFont);
            lbl.setHorizontalAlignment(JTextField.CENTER);
            displayTablePanel.add(lbl);

            // Add price in column 2
            lbl = new JLabel(stockData[stockCnt][1]);
            lbl.setFont(mainFont);
            lbl.setHorizontalAlignment(JTextField.CENTER);
            displayTablePanel.add(lbl);

            // Add shares count in column 3
            lbl = new JLabel(stockData[stockCnt][2]);
            lbl.setFont(mainFont);
            lbl.setHorizontalAlignment(JTextField.CENTER);
            displayTablePanel.add(lbl);
        }


        // Add balance row
        displayTablePanel.add(new JLabel()); // first column is empty

        lbl = new JLabel("Balance: $" + Math.round(account.getBalance()*100.0)/100.0); // Prep second column
        lbl.setOpaque(true);
        lbl.setBackground(new Color(184, 6, 6));
        lbl.setFont(new Font("Sergoe print",Font.BOLD,18));
        lbl.setForeground(Color.WHITE);
        lbl.setHorizontalAlignment(JTextField.CENTER);
        displayTablePanel.add(lbl);

        displayTablePanel.add(new JLabel()); // third column is empty   
        
        JPanel form = new JPanel();
        form.setLayout(new GridLayout(5,3,5,5));
        
        JLabel text = new JLabel("Add the Stock Abbreviation:");
        text.setOpaque(true);
        text.setBackground(new Color(184, 184, 184));
        text.setFont(new Font("Sergoe print",Font.BOLD,18));
        text.setHorizontalAlignment(JTextField.CENTER);
        form.add(text);
        
        tfStockName = new JTextField();
        tfStockName.setFont(mainFont);
        tfStockName.setHorizontalAlignment(JTextField.CENTER);
        form.add(tfStockName);
        
        text = new JLabel("Add the number of stocks:");
        text.setOpaque(true);
        text.setBackground(new Color(184, 184, 184));
        text.setFont(new Font("Sergoe print",Font.BOLD,18));
        text.setHorizontalAlignment(JTextField.CENTER);
        form.add(text);
        
        tfShareCount = new JTextField();
        tfShareCount.setFont(mainFont);
        tfShareCount.setHorizontalAlignment(JTextField.CENTER);
        form.add(tfShareCount);
        
        tm = new JLabel("Time Remaining: "+currentTimer);
        tm.setOpaque(true);
        tm.setBackground(new Color(184, 6, 6));
        tm.setForeground(Color.WHITE);
        tm.setFont(new Font("Sergoe print",Font.BOLD,18));
        tm.setHorizontalAlignment(JTextField.CENTER);
        form.add(tm);
        Thread threadTimer = new Thread(this);
        threadTimer.start();
        
        JPanel buttons = new JPanel();
        buttons.setLayout(new GridLayout(1,2,5,5));
        
        buttons.add(btnBuy);
        buttons.add(btnSell);
        
        form.add(buttons);
        
        form.add(new JLabel());

        form.add(btnRefresh);
        form.add(new JLabel());

        JComponent pane = (JComponent) this.getContentPane();

        if (pane.getComponentCount()>0)
            pane.removeAll();

        mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());
        mainPanel.add(displayTablePanel,BorderLayout.NORTH);
        mainPanel.add(form,BorderLayout.SOUTH);
        

        add(mainPanel);

        setTitle("Stock Market");
        setExtendedState(JFrame.MAXIMIZED_BOTH);
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
        
        pane.revalidate();
    }

    public void actionPerformed(ActionEvent e) 
    {
        JButton btn = (JButton) e.getSource();

        switch(btn.getText().toLowerCase())
        {
            case "buy":
                //Get Stock name
                String stockToBuy = tfStockName.getText();

                // Get share count
                int buyCnt = Integer.parseInt(tfShareCount.getText());

                int indexToBuy = indexInArray(stockToBuy);
                double buyPrice = buyCnt * allStocks[indexToBuy].getPrice();

                if (indexToBuy > 0 && buyPrice <= account.getBalance() && buyCnt!=0){
                    account.Withdraw(buyPrice);
                    account.updateStocks(indexToBuy, buyCnt);
                }
                
                break;

            case "sell":
                String stockToSell = tfStockName.getText();

                // Get share count
                int sellCnt = Integer.parseInt(tfShareCount.getText());

                int indexToSell = indexInArray(stockToSell);
                double sellRevenue = sellCnt * allStocks[indexToSell].getPrice();
                
                if (indexToSell>0 && sellCnt<=amountOfShares[indexToSell] && sellCnt!=0){
                    account.updateStocks(indexToSell,(-1)*sellCnt);
                    account.Insert(sellRevenue);
                }
                
                break;
                
            case "refresh":
                Stocks stocks = new Stocks();
                allStocks = stocks.newprice();
                break;
        };
        

        PrepareDisplayData();
        UpdatePanel();
        
    }
    
    public void run(){
        
        Timer timer = new Timer();

        timer.scheduleAtFixedRate(new TimerTask() {
            int i = currentTimer;

            public void run() {

                currentTimer = i;
                tm.setText(""+i);
                i--;
                
                if (i == -1) {
                    timer.cancel();
                    currentTimer = 30;
                    Stocks stocks = new Stocks();
                    allStocks = stocks.newprice();
                    PrepareDisplayData();
                    UpdatePanel();
                }
            }
        }, 0, 1000);
    }
    
    private int indexInArray(String abb){
        for (int i=0;i<abbrev.length;i++){
            if (abbrev[i].equalsIgnoreCase(abb))
                return i;
        }
        return -1;
    }
}
