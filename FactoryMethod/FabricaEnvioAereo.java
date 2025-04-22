package FactoryMethod;
public class FabricaEnvioAereo extends FabricaEnvios {
    @Override
    public Envio crearEnvio() {
        return new EnvioAereo();
    }
}