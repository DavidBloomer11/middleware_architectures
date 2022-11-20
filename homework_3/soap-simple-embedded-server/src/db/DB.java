package db;
import java.util.ArrayList;
import java.util.Hashtable;
import java.util.ArrayList;
import java.util.Set;

public class DB {
    private static DB instance = null;
    private Hashtable<Integer, Booking> ht = new Hashtable();

    public static DB getInstance() {
        if (instance == null)
            instance = new DB();        
        return instance;
    }
    public void addObject(Booking t){
        ht.put(t.getId(), t);
    }
    public Booking getObject(int id) {     
        return ht.get(id);
    }

    public void removeObject(int id) {
        ht.remove(id);
    }

    public ArrayList<Booking> getAllObjects() {
        ArrayList<Booking> list = new ArrayList<Booking>();
        Set<Integer> keys = ht.keySet();

        for(int key: keys) {
            list.add(getObject(key));
        }

        return list;
    }
}