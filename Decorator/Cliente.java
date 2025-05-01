interface Notificador {
    void enviar(String mensaje);
}

class NotificadorBase implements Notificador {
    @Override
    public void enviar(String mensaje) {
        System.out.println("Notificación estándar: " + mensaje);
    }
}

abstract class DecoradorNotificador implements Notificador {
    protected Notificador notificador;

    public DecoradorNotificador(Notificador notificador) {
        this.notificador = notificador;
    }

    @Override
    public void enviar(String mensaje) {
        notificador.enviar(mensaje);
    }
}

class NotificadorEmail extends DecoradorNotificador {
    public NotificadorEmail(Notificador notificador) {
        super(notificador);
    }

    @Override
    public void enviar(String mensaje) {
        super.enviar(mensaje);
        enviarCorreo(mensaje);
    }

    private void enviarCorreo(String mensaje) {
        System.out.println("Enviando notificación por correo: " + mensaje);
    }
}

class NotificadorSMS extends DecoradorNotificador {
    public NotificadorSMS(Notificador notificador) {
        super(notificador);
    }

    @Override
    public void enviar(String mensaje) {
        super.enviar(mensaje);
        enviarSMS(mensaje);
    }

    private void enviarSMS(String mensaje) {
        System.out.println("Enviando notificación por SMS: " + mensaje);
    }
}

class NotificadorFacebook extends DecoradorNotificador {
    public NotificadorFacebook(Notificador notificador) {
        super(notificador);
    }

    @Override
    public void enviar(String mensaje) {
        super.enviar(mensaje);
        enviarFacebook(mensaje);
    }

    private void enviarFacebook(String mensaje) {
        System.out.println("Enviando notificación por Facebook: " + mensaje);
    }
}

class NotificadorSlack extends DecoradorNotificador {
    public NotificadorSlack(Notificador notificador) {
        super(notificador);
    }

    @Override
    public void enviar(String mensaje) {
        super.enviar(mensaje);
        enviarSlack(mensaje);
    }

    private void enviarSlack(String mensaje) {
        System.out.println("Enviando notificación por Slack: " + mensaje);
    }
}

// Nuevo decorador para enviar notificaciones por WhatsApp
class NotificadorWhatsApp extends DecoradorNotificador {
    public NotificadorWhatsApp(Notificador notificador) {
        super(notificador);
    }

    @Override
    public void enviar(String mensaje) {
        super.enviar(mensaje);
        enviarWhatsApp(mensaje);
    }

    private void enviarWhatsApp(String mensaje) {
        System.out.println("Enviando notificación por WhatsApp: " + mensaje);
    }
}

public class Cliente {
    public static void main(String[] args) {
        // Crear notificador base y encadenar decoradores
        Notificador notificador = new NotificadorBase();
        notificador = new NotificadorEmail(notificador);
        notificador = new NotificadorSMS(notificador);
        notificador = new NotificadorFacebook(notificador);
        notificador = new NotificadorSlack(notificador);
        notificador = new NotificadorWhatsApp(notificador); // Nuevo decorador WhatsApp añadido

        // Enviar notificación a través de todos los canales
        notificador.enviar("¡Alerta de seguridad!");
    }
}