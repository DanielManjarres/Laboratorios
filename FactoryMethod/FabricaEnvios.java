package FactoryMethod;
public abstract class FabricaEnvios {
    public abstract Envio crearEnvio();

    public void gestionarEnvio() {
        Envio envio = crearEnvio();
        if (envio == null) {
            System.out.println("Error: No se pudo crear el envío.");
            return;
        }
        System.out.println("Resultado del envío: " + envio.procesarEnvio());
    }
}