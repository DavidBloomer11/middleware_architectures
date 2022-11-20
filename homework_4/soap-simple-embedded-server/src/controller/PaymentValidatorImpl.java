package controller;

import java.net.MalformedURLException;
import java.net.URI;
import java.net.URL;

import javax.sound.midi.Soundbank;

import https.courses_fit_cvut_cz.ni_am1.hw.web_services.*;

public class PaymentValidatorImpl implements PaymentValidator {

    @Override
    public boolean validatePayment(String cardNumber, String cardOwner) {
        // TODO Auto-generated method stub

        CardPortService service = new CardPortService();

        final CardPort port = service.getPort(CardPort.class);

        final ObjectFactory factory = new ObjectFactory();

        ValidateCardRequest request = factory.createValidateCardRequest();

        request.setCardNumber(cardNumber);
        request.setCardOwner(cardOwner);

        ValidateCardResponse response = port.validateCard(request);

        System.out.println(response.isResult());

        return response.isResult();
    }
    
}
