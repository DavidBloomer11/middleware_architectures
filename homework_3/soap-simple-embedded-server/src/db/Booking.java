package db;

import java.io.Serializable;

import db.Passenger;
 
public class Booking implements Serializable {
    private int id;
    private String name;
    private String dateDeparture;
    private String dateArrival;
    private int airportId;

    public Booking(){
        this(0, "John Doe","11-11-2022","12-11-2020",0);
    }

    public Booking(int id, String name, String dateDeparture, String dateArrival, int airportId) {
        this.id = id;
        this.name = name;
        this.dateArrival = dateArrival;
        this.dateDeparture = dateDeparture;
        this.airportId = airportId;
    }
    
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getId() {
        return id;
    }
        
    public void setId(int id) {
        this.id = id;
    }

    public void setDateDeparture(String dateDeparture) {
        this.dateDeparture = dateDeparture;
    }

    public String getDateDeparture() {
        return this.dateDeparture;
    }

    public void setDateArrival(String dateArrival) {
        this.dateArrival = dateArrival;
    }

    public String getDateArrival() {
        return this.dateArrival;
    }

    public int getAirportId() {
        return airportId;
    }

    public void setAirportId(int airportId) {
        this.airportId = airportId;
    }

}