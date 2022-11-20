package services;

import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.jws.WebParam;

import db.*;
import java.util.ArrayList;

@WebService
public class TourService {

	@WebMethod
	public void addBooking(@WebParam(name = "bookingId") int id, 
	@WebParam(name = "passengerName") String name, 
	@WebParam(name = "dateDeparture") String dateDeparture,
	@WebParam(name = "dateArrival") String dateArrival,
	@WebParam(name = "airportId") int airportId) {

		Booking booking = new Booking(id,name,dateDeparture,dateArrival,airportId);
		DB db = DB.getInstance();

		db.addObject(booking);
	}

	@WebMethod
	public Booking getBooking(@WebParam(name = "bookingId")int id) {
		DB db = DB.getInstance();
		Booking booking = db.getObject(id);
		return booking;
	}


	@WebMethod
	public void removeBooking(@WebParam(name = "bookingId") int id) {
		DB db = DB.getInstance();
		db.removeObject(id);
	}

	@WebMethod
	public ArrayList<Booking> getAllBookings() {
		DB db = DB.getInstance();
		ArrayList<Booking> bookings = db.getAllObjects();

		return bookings;
	}

}