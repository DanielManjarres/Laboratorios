package FactoryMethod;
public class EnvioTerrestre implements Envio {
    @Override
    public String procesarEnvio() {
        return "Envío Terrestre: Paquete enviado por carretera.";
    }
}