

// 3. ConcreteBuilder (implementa los pasos de construcción de la pizza hawaiana)
public class PizzaHawaianaBuilder implements PizzaBuilder {
    private Pizza pizza;
    private String tamano;  // Nuevo campo para almacenar el tamaño ingresado
    private String ingredientes;  // Nuevo campo para almacenar los ingredientes ingresados

    // Constructor que acepta tamaño e ingredientes como parámetros
    public PizzaHawaianaBuilder(String tamano, String ingredientes) {
        this.pizza = new Pizza();
        this.tamano = tamano;
        this.ingredientes = ingredientes;
    }

    @Override
    public void buildMasa() {
        pizza.setMasa("Fina");  // La masa sigue siendo fija para la pizza hawaiana
    }

    @Override
    public void buildTamano() {
        pizza.setTamano(tamano);  // Usa el tamaño ingresado por el usuario
    }

    @Override
    public void buildIngredientes() {
        pizza.setIngredientes(ingredientes);  // Usa los ingredientes ingresados por el usuario
    }

    @Override
    public Pizza getPizza() {
        return pizza;
    }
}