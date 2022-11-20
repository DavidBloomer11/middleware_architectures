
package https.courses_fit_cvut_cz.ni_am1.hw.web_services;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import javax.xml.bind.annotation.XmlType;


/**
 * &lt;p&gt;Java class for anonymous complex type.
 * 
 * &lt;p&gt;The following schema fragment specifies the expected content contained within this class.
 * 
 * &lt;pre&gt;
 * &amp;lt;complexType&amp;gt;
 *   &amp;lt;complexContent&amp;gt;
 *     &amp;lt;restriction base="{http://www.w3.org/2001/XMLSchema}anyType"&amp;gt;
 *       &amp;lt;sequence&amp;gt;
 *         &amp;lt;element name="cardNumber" type="{http://www.w3.org/2001/XMLSchema}string"/&amp;gt;
 *         &amp;lt;element name="cardOwner" type="{http://www.w3.org/2001/XMLSchema}string"/&amp;gt;
 *       &amp;lt;/sequence&amp;gt;
 *     &amp;lt;/restriction&amp;gt;
 *   &amp;lt;/complexContent&amp;gt;
 * &amp;lt;/complexType&amp;gt;
 * &lt;/pre&gt;
 * 
 * 
 */
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {
    "cardNumber",
    "cardOwner"
})
@XmlRootElement(name = "validateCardRequest")
public class ValidateCardRequest {

    @XmlElement(required = true)
    protected String cardNumber;
    @XmlElement(required = true)
    protected String cardOwner;

    /**
     * Gets the value of the cardNumber property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getCardNumber() {
        return cardNumber;
    }

    /**
     * Sets the value of the cardNumber property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setCardNumber(String value) {
        this.cardNumber = value;
    }

    /**
     * Gets the value of the cardOwner property.
     * 
     * @return
     *     possible object is
     *     {@link String }
     *     
     */
    public String getCardOwner() {
        return cardOwner;
    }

    /**
     * Sets the value of the cardOwner property.
     * 
     * @param value
     *     allowed object is
     *     {@link String }
     *     
     */
    public void setCardOwner(String value) {
        this.cardOwner = value;
    }

}
