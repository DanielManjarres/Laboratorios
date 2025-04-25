
public class Main {
    public static void main(String[] args) {
        ErrorLogger logger = ErrorLogger.getInstancia();

        try {
            // Simular un error
            int resultado = 10 / 0;
        } catch (ArithmeticException e) {
            logger.logError("División por cero: " + e.getMessage());
        }

        logger.logError("Archivo de configuración no encontrado.");
    }
}
