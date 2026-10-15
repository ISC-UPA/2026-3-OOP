package personal.patrones;

// ============================================
class DatabaseConnection {
    private static DatabaseConnection instance;
    private String connectionString;
    
    private DatabaseConnection() {
        // Simulando inicialización costosa
        try {
            Thread.sleep(1000);
            connectionString = "jdbc:mysql://localhost:3306/mydb";
            System.out.println("Conexión a base de datos establecida");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    
    public static synchronized DatabaseConnection getInstance() {
        if (instance == null) {
            instance = new DatabaseConnection();
        }
        return instance;
    }
    
    public void query(String sql) {
        System.out.println("Ejecutando query: " + sql + " en " + connectionString);
    }
}

public class SingletonDB {

    public static void main(String[] args) {
        System.out.println("\n=== PRUEBA DATABASE CONNECTION ===");
        DatabaseConnection db1 = DatabaseConnection.getInstance();
        db1.query("SELECT * FROM users   ");

         DatabaseConnection db2 = DatabaseConnection.getInstance();
        db2.query("SELECT * FROM products");
        System.out.println("¿Son la misma conexión? " + (db1 == db2));
    }
    
}
