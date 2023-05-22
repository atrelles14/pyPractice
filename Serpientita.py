import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Definir dimensiones de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Definir tamaño del bloque y velocidad de la serpiente
TAMANIO_BLOQUE = 20
VELOCIDAD_SERPIENTE = 20

# Crear la ventana del juego
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego de la Serpiente")

# Clase para representar la serpiente
class Serpiente:
    def __init__(self):
        self.longitud = 1
        self.posiciones = [(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2)]
        self.direccion = random.choice(["ARRIBA", "ABAJO", "IZQUIERDA", "DERECHA"])
        self.color = VERDE

    def mover(self):
        x, y = self.posiciones[0]
        if self.direccion == "ARRIBA":
            y -= TAMANIO_BLOQUE
        elif self.direccion == "ABAJO":
            y += TAMANIO_BLOQUE
        elif self.direccion == "IZQUIERDA":
            x -= TAMANIO_BLOQUE
        elif self.direccion == "DERECHA":
            x += TAMANIO_BLOQUE
        nueva_posicion = (x, y)
        self.posiciones.insert(0, nueva_posicion)
        if len(self.posiciones) > self.longitud:
            self.posiciones.pop()

    def dibujar(self):
        for posicion in self.posiciones:
            pygame.draw.rect(pantalla, self.color, (posicion[0], posicion[1], TAMANIO_BLOQUE, TAMANIO_BLOQUE))

    def cambiar_direccion(self, direccion):
        if direccion == "ARRIBA" and self.direccion != "ABAJO":
            self.direccion = direccion
        elif direccion == "ABAJO" and self.direccion != "ARRIBA":
            self.direccion = direccion
        elif direccion == "IZQUIERDA" and self.direccion != "DERECHA":
            self.direccion = direccion
        elif direccion == "DERECHA" and self.direccion != "IZQUIERDA":
            self.direccion = direccion

    def colision_con_limite_pantalla(self):
        cabeza_x, cabeza_y = self.posiciones[0]
        return cabeza_x < 0 or cabeza_x >= ANCHO_PANTALLA or cabeza_y < 0 or cabeza_y >= ALTO_PANTALLA

    def colision_con_cuerpo(self):
        cabeza = self.posiciones[0]
        return cabeza in self.posiciones[1:]

    def aumentar_longitud(self):
        self.longitud += 1

# Clase para representar la comida de la serpiente
class Comida:
    def __init__(self):
        self.posicion = self.generar_posicion()
        self.color = ROJO

    def generar_posicion(self):
        x = random.randint(0, ANCHO_PANTALLA // TAMANIO_BLOQUE - 1) * TAMANIO_BLOQUE
        y = random.randint(0, ALTO_PANTALLA // TAMANIO_BLOQUE - 1) * TAMANIO_BLOQUE
        return (x, y)

    def dibujar(self):
        pygame.draw.rect(pantalla, self.color, (self.posicion[0], self.posicion[1], TAMANIO_BLOQUE, TAMANIO_BLOQUE))

# Función principal del juego
def jugar_juego():
    serpiente = Serpiente()
    comida = Comida()
    reloj = pygame.time.Clock()
    juego_terminado = False

    while not juego_terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_terminado = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    serpiente.cambiar_direccion("ARRIBA")
                elif evento.key == pygame.K_DOWN:
                    serpiente.cambiar_direccion("ABAJO")
                elif evento.key == pygame.K_LEFT:
                    serpiente.cambiar_direccion("IZQUIERDA")
                elif evento.key == pygame.K_RIGHT:
                    serpiente.cambiar_direccion("DERECHA")

        serpiente.mover()

        if serpiente.colision_con_limite_pantalla() or serpiente.colision_con_cuerpo():
            juego_terminado = True

        if serpiente.posiciones[0] == comida.posicion:
            serpiente.aumentar_longitud()
            comida.posicion = comida.generar_posicion()

        pantalla.fill(NEGRO)
        serpiente.dibujar()
        comida.dibujar()
        pygame.display.update()

        reloj.tick(VELOCIDAD_SERPIENTE)

    pygame.quit()

# Ejecutar el juego
jugar_juego()
