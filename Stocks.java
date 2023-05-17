
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author 824891
 */
public class Stocks {
    public np[] stock = new np[20];
    //the actual stocks as stock objects
    private int count = 0;
    //count to decide if the price should go up over the next 10 turns or down
    private static double vol = 9.0;
    //the volitality of how much the stock moves every turn the lower the more volitile
    public Stocks (){
        stock[0]= new np("Microsoft (MSFT)", 120.00);
        stock[1]= new np("Google (GOOG)", 113.00);
        stock[2]= new np("SnapChat (SNAP)", 8.50);
        stock[3]= new np("Ford (F)", 11.00);
        stock[4]= new np("AT&T (T)", 17.00);
        stock[5]= new np("Tesla (TSLA)", 170.00);
        stock[6]= new np("Apple (AAPL)", 172.50);
        stock[7]= new np("Amazon (AMZN)", 111.00);
        stock[8]= new np("Walmart (WMT)", 154.00);
        stock[9]= new np("Costco (COST)", 370.00);
        stock[10]= new np("Advanced Micro Devices (AMD)", 94.00);
        stock[11]= new np("CoinBase (COIN)", 55.00);
        stock[12]= new np("Berkshire Hathaway B (BRK)", 370.00);
        stock[13]= new np("McDonalds (MCD)", 295.00);
        stock[14]= new np("GameStop (GME)", 20.00);
        stock[15]= new np("BestBuy (BBY)", 71.00);
        stock[16]= new np("Meta (META)", 170.00);
        stock[17]= new np("Discover (DFS)", 96.00);
        stock[18]= new np("Waste Management (WM)", 170.00);
        stock[19]= new np("Dell (DELL)", 44.00);
    }
    //does fancy math to decide how much each stock should move
    //its relative to each stock
    public np[] newprice(){
        for (int r = 0; r < stock.length;r++)
        {
           double range = (Math.random()*vol)+2;
           double cPri = stock[r].getPrice();
           double temp = cPri/10;
           stock[r].setPrice(Math.round((cPri-(temp)+(Math.random()*2*temp))*100.0)/100.0);
        }
        return stock;
    }
    //sets the volitility of how much the stock moves
    public void setvol(int v){
        if (v == 1){
            vol = 9.0;
        }
        if (v == 2){
            vol = 7.0;
        }
        if (v == 3){
            vol = 5.0;
        }
        if (v == 4){
            vol = 3.0;
        }
        if (v == 5){
            vol = 1.0;
        }
    }
}
