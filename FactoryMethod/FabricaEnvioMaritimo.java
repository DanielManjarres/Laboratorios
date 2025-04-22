package FactoryMethod;
public class FabricaEnvioMaritimo extends FabricaEnvios {
    @Override
    public Envio crearEnvio() {
        return new EnvioMaritimo();
    }
}