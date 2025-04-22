package FactoryMethod;
public class DemoEnvios {
    public static void main(String[] args) {
        System.out.println("Probando la Fábrica de Envíos Terrestres:");
        FabricaEnvios fabricaTerrestre = new FabricaEnvioTerrestre();
        fabricaTerrestre.gestionarEnvio();

        System.out.println("\nProbando la Fábrica de Envíos Marítimos:");
        FabricaEnvios fabricaMaritimo = new FabricaEnvioMaritimo();
        fabricaMaritimo.gestionarEnvio();

        System.out.println("\nProbando la Fábrica de Envíos Aéreos:");
        FabricaEnvios fabricaAereo = new FabricaEnvioAereo();
        fabricaAereo.gestionarEnvio();
    }
}
