import copy

class Enemigo:
    def clonar(self):
        return copy.deepcopy(self)  # devolver una copia exacta del objeto

class Zombi(Enemigo):
    def __init__(self, vida, daño, velocidad, poison_attack=False):
        self.vida = vida
        self.daño = daño
        self.velocidad = velocidad
        self.poison_attack = poison_attack  # Nueva habilidad

    def __str__(self):
        poison_status = "con ataque venenoso" if self.poison_attack else "sin ataque venenoso"
        return f"Zombi {{vida={self.vida}, daño={self.daño}, velocidad={self.velocidad}, {poison_status}}}"

# Simulación del juego
def juego():
    zombi_base = Zombi(100, 10, 1.5)  # se crea un zombi base

    zombi1 = zombi_base.clonar()
    zombi2 = zombi_base.clonar()
    zombi3 = zombi_base.clonar()  # Nuevo zombi clonado

    # Personalizar clones
    zombi1.vida = 120
    zombi2.velocidad = 2.0
    zombi3.poison_attack = True  # Nueva habilidad para el zombi3
    zombi3.vida = 80  # Personalización adicional para diferenciar

    print("Zombi base:", zombi_base)
    print("Zombi 1:", zombi1)
    print("Zombi 2:", zombi2)
    print("Zombi 3:", zombi3)

# Ejecutar
juego()