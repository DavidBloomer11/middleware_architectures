package db;
import java.util.ArrayList;
import java.util.Hashtable;
import java.util.ArrayList;
import java.util.Set;

public class DB {
    private static DB instance = null;
    private Hashtable<Integer, Payment> ht = new Hashtable();

    public static DB getInstance() {
        if (instance == null)
            instance = new DB();        
        return instance;
    }
    public void addObject(Payment t){
        ht.put(t.getOrderId(), t);
    }
    public Payment getObject(int id) {     
        return ht.get(id);
    }

    public void removeObject(int id) {
        ht.remove(id);
    }

    public ArrayList<Payment> getAllObjects() {
        ArrayList<Payment> list = new ArrayList<Payment>();
        Set<Integer> keys = ht.keySet();

        for(int key: keys) {
            list.add(getObject(key));
        }

        return list;
    }
}