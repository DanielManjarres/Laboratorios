import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;

// Clase Flyweight: Representa el estado intrínseco de un árbol (compartido)
class TreeType {
    private String name;    // Ejemplo: "Pino", "Roble"
    private String color;   // Ejemplo: "Verde", "Marrón"
    private String texture; // Ejemplo: "Hoja fina", "Corteza rugosa"

    // Constructor que inicializa el estado intrínseco
    public TreeType(String name, String color, String texture) {
        this.name = name;
        this.color = color;
        this.texture = texture;
    }

    // Método que dibuja el árbol, usando el estado extrínseco (coordenadas x, y)
    public void draw(int x, int y) {
        System.out.println("Dibujando árbol '" + name + "' [" + color + ", " + texture + "] en posición (" + x + ", " + y + ")");
    }
}

// Fábrica Flyweight: Gestiona la creación y reutilización de TreeType
class TreeFactory {
    // Mapa que almacena los TreeType existentes, usando una clave única
    private static Map<String, TreeType> treeTypes = new HashMap<>();

    // Método para obtener o crear un TreeType
    public static TreeType getTreeType(String name, String color, String texture) {
        // Creamos una clave única combinando las propiedades intrínsecas
        String key = name + "-" + color + "-" + texture;

        // Si no existe el TreeType, lo creamos y lo almacenamos
        if (!treeTypes.containsKey(key)) {
            treeTypes.put(key, new TreeType(name, color, texture));
            System.out.println("Creando nuevo TreeType: " + key);
        }
        // Retornamos el TreeType existente o recién creado
        return treeTypes.get(key);
    }
}

// Clase que representa un árbol individual, con estado extrínseco
class Tree {
    private int x, y;          // Posición en el mapa (estado extrínseco)
    private TreeType type;     // Referencia al Flyweight (estado intrínseco)

    // Constructor que asocia un TreeType y una posición
    public Tree(int x, int y, TreeType type) {
        this.x = x;
        this.y = y;
        this.type = type;
    }

    // Método para dibujar el árbol
    public void draw() {
        type.draw(x, y);
    }
}

// Clase cliente: Representa el bosque que contiene muchos árboles
class Forest {
    // Lista de árboles en el bosque
    private List<Tree> trees = new ArrayList<>();

    // Método para "plantar" un árbol en una posición específica
    public void plantTree(int x, int y, String name, String color, String texture) {
        // Obtenemos el TreeType desde la fábrica
        TreeType type = TreeFactory.getTreeType(name, color, texture);
        // Creamos un nuevo árbol con su posición y tipo
        trees.add(new Tree(x, y, type));
        System.out.println("Plantado árbol en (" + x + ", " + y + ")");
    }

    // Método para dibujar todos los árboles del bosque
    public void draw() {
        System.out.println("Renderizando el bosque...");
        for (Tree tree : trees) {
            tree.draw();
        }
    }
}

// Ejemplo de uso
public class FlyweightDemo {
    public static void main(String[] args) {
        Forest forest = new Forest();

        // Plantamos varios árboles, algunos con el mismo tipo
        forest.plantTree(10, 20, "Pino", "Verde", "Hoja fina");
        forest.plantTree(15, 25, "Pino", "Verde", "Hoja fina"); // Reutiliza el mismo TreeType
        forest.plantTree(30, 40, "Roble", "Marrón", "Corteza rugosa");
        forest.plantTree(35, 45, "Pino", "Verde", "Hoja fina"); // Reutiliza nuevamente
        forest.plantTree(50, 60, "Roble", "Marrón", "Corteza rugosa"); // Reutiliza el roble

        // Renderizamos el bosque
        forest.draw();

        // Nota: Aunque plantamos 5 árboles, solo creamos 2 TreeType
    }
}

