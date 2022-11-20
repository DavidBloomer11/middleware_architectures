package services;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.WebParam;

import db.*;
import controller.*;
import java.util.ArrayList;

@WebService
public class PaymentService {

	@WebMethod
	public boolean addPayment(
		@WebParam(name = "cardNumber") String cardNumber,
		@WebParam(name = "cardOwner") String cardOwner,
		@WebParam(name = "orderId") int orderId) {

		Payment payment = new Payment(cardNumber,cardOwner,orderId);
		DB db = DB.getInstance();

		PaymentValidator validator = new PaymentValidatorImpl();
		boolean response = validator.validatePayment(cardNumber, cardOwner);

		if (response == true) {
			// Let payment go through
			db.addObject(payment);
		}
		return response;
	}

	@WebMethod
	public Payment getPayment(@WebParam(name = "orderId") int id) {
		DB db = DB.getInstance();
		Payment payment = db.getObject(id);
		return payment;
	}

	@WebMethod
	public ArrayList<Payment> getAllPayments() {
		DB db = DB.getInstance();
		ArrayList<Payment> paymentList = db.getAllObjects();

		return paymentList;
	}

}