package FactoryMethod;
public class FabricaEnvioTerrestre extends FabricaEnvios {
    @Override
    public Envio crearEnvio() {
        return new EnvioTerrestre();
    }
}