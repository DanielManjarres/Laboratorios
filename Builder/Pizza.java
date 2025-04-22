
// Product, el objeto final a construir
public class Pizza {
    private String masa;
    private String tamano;
    private String ingredientes;

    // Setters con validación
    public void setMasa(String masa) {
        if (masa == null || masa.trim().isEmpty()) {
            throw new IllegalArgumentException("La masa no puede ser nula o vacía");
        }
        this.masa = masa;
    }

    public void setTamano(String tamano) {
        if (tamano == null || tamano.trim().isEmpty()) {
            throw new IllegalArgumentException("El tamaño no puede ser nulo o vacío");
        }
        this.tamano = tamano;
    }

    public void setIngredientes(String ingredientes) {
        if (ingredientes == null || ingredientes.trim().isEmpty()) {
            throw new IllegalArgumentException("Los ingredientes no pueden ser nulos o vacíos");
        }
        this.ingredientes = ingredientes;
    }

    // Getters
    public String getMasa() {
        return masa;
    }

    public String getTamano() {
        return tamano;
    }

    public String getIngredientes() {
        return ingredientes;
    }

    // Método para mostrar la pizza final
    public void mostrarPizza() {
        System.out.println("Pizza [Masa: " + masa + ", Tamaño: " + tamano + ", Ingredientes: " + ingredientes + "]");
    }
}
