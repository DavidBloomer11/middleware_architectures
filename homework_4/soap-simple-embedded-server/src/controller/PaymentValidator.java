package controller;

public interface PaymentValidator {
    public boolean validatePayment(String cardNumber, String cardOwner);
}
