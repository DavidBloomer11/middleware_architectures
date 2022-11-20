package db;

public class Payment {

    private String cardNumber;
    private String cardOwner;
    private int orderId;

    public Payment() {
        this.cardNumber = "5081021021";
        this.cardOwner = "John Doe";
        this.orderId = 0;
    }

    public Payment(String cn, String co, int id) {
        this.cardNumber = cn;
        this.cardOwner = co;
        this.orderId = id;
    }

    public String getCardNumber() {
        return cardNumber;
    }

    public void setCardNumber(String cardNumber) {
        this.cardNumber = cardNumber;
    }

    public int getOrderId() {
        return orderId;
    }

    public void setOrderId(int orderId) {
        this.orderId = orderId;
    }

    public String getCardOwner() {
        return cardOwner;
    }

    public void setCardOwner(String cardOwner) {
        this.cardOwner = cardOwner;
    }

}
