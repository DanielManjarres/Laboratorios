package FactoryMethod;

public class EnvioAereo implements Envio {
    @Override
    public String procesarEnvio() {
        return "Envío Aéreo: Paquete enviado por avión.";
    }
}