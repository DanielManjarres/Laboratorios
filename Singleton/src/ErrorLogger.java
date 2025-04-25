
public class ErrorLogger {
    private static ErrorLogger instancia;

    // Constructor privado para evitar instanciación externa
    private ErrorLogger() {
    }

    // Método público para obtener la instancia
    public static ErrorLogger getInstancia() {
        if (instancia == null) {
            instancia = new ErrorLogger();
        }
        return instancia;
    }

    // Método para registrar un error
    public void logError(String mensaje) {
        System.err.println("[ERROR] " + mensaje);
    }
}

