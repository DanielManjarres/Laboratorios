# Abstracción: La clase Dispositivo
class Dispositivo:
    def __init__(self, implementacion):
        self.implementacion = implementacion

    def encender(self):
        self.implementacion.encender()

    def apagar(self):
        self.implementacion.apagar()

    def establecer_canal(self, canal):
        self.implementacion.establecer_canal(canal)

# Implementaciones Concretas
class TVImplementacion:
    def encender(self):
        print("TV: Encendiendo")

    def apagar(self):
        print("TV: Apagando")

    def establecer_canal(self, canal):
        print(f"TV: Estableciendo canal en {canal}")

class RadioImplementacion:
    def encender(self):
        print("Radio: Encendiendo")

    def apagar(self):
        print("Radio: Apagando")

    def establecer_canal(self, canal):
        print(f"Radio: Sintonizando estación {canal}")

class DVDImplementacion:
    def encender(self):
        print("DVD: Encendiendo")

    def apagar(self):
        print("DVD: Apagando")

    def establecer_canal(self, canal):
        print(f"DVD: No aplica establecer canal, pero se recibió: {canal}")

    def agregar_cd_rom(self):
        print("DVD: CD-ROM insertado")

# Cliente
tv = Dispositivo(TVImplementacion())
radio = Dispositivo(RadioImplementacion())
dvd_implementacion = DVDImplementacion()
dvd = Dispositivo(dvd_implementacion)

tv.encender()
tv.establecer_canal(5)
tv.apagar()

radio.encender()
radio.establecer_canal("98.5 FM")
radio.apagar()

dvd.encender()
dvd.establecer_canal("Película")  # Para mantener compatibilidad con la interfaz
dvd_implementacion.agregar_cd_rom()
dvd.apagar()