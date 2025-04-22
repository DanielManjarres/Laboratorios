import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Crear un objeto Scanner para leer la entrada del usuario
        Scanner scanner = new Scanner(System.in);

        // Solicitar el tamaño de la pizza al usuario
        System.out.print("Ingrese el tamaño de la pizza (por ejemplo, Pequeña, Mediana, Grande): ");
        String tamano = scanner.nextLine();

        // Solicitar los ingredientes de la pizza al usuario
        System.out.print("Ingrese los ingredientes de la pizza (separados por comas, por ejemplo, Jamón, Piña): ");
        String ingredientes = scanner.nextLine();

        // Crear el Builder pasando el tamaño y los ingredientes ingresados
        PizzaBuilder builder = new PizzaHawaianaBuilder(tamano, ingredientes);
        Pizzeria pizzeria = new Pizzeria(builder);  // Crear el Director
        Pizza miPizza = pizzeria.hacerPizza();  // Usar el Director para construir la pizza
        miPizza.mostrarPizza();  // Mostrar la pizza final

        // Cerrar el scanner
        scanner.close();
    }
}