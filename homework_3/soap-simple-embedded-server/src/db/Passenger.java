package db;

import java.io.Serializable;

public class Passenger implements Serializable {
    private String firstName;
    private String lastName;
    private String passport;

    public Passenger(String firstName, String lastName, String passport) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.passport = passport;
    }


    public String getFirstName() {
        return this.firstName;
    }

    public String getPassport() {
        return this.passport;
    }

    public String getLastName() {
        return this.lastName;
    }
    
}
