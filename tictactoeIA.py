import random

# Función para dibujar el tablero
def dibujar_tablero(tablero):
    print("-------------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" " + tablero[i][j] + " |", end="")
        print("\n-------------")

# Función para verificar si hay un ganador
def hay_ganador(tablero, jugador):
    # Verificar filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == jugador:
            return True

    # Verificar columnas
    for j in range(3):
        if tablero[0][j] == tablero[1][j] == tablero[2][j] == jugador:
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

# Función para realizar el movimiento del jugador
def movimiento_jugador(tablero):
    while True:
        fila = int(input("Ingresa la fila (0-2): "))
        columna = int(input("Ingresa la columna (0-2): "))

        if fila >= 0 and fila < 3 and columna >= 0 and columna < 3 and tablero[fila][columna] == " ":
            tablero[fila][columna] = "X"
            break
        else:
            print("Movimiento inválido. Intenta de nuevo.")

# Función para realizar el movimiento de la IA
def movimiento_IA(tablero):
    while True:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "O"
            break

# Función principal del juego
def jugar_tic_tac_toe():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    turno = "X"  # Empieza el jugador

    while True:
        dibujar_tablero(tablero)

        if turno == "X":
            movimiento_jugador(tablero)
        else:
            movimiento_IA(tablero)

        if hay_ganador(tablero, turno):
            dibujar_tablero(tablero)
            if turno == "X":
                print("¡Has ganado!")
            else:
                print("¡La IA ha ganado!")
            break

        if all(tablero[i][j] != " " for i in range(3) for j in range(3)):
            dibujar_tablero(tablero)
            print("¡Es un empate!")
            break

        turno = "O" if turno == "X" else "X"

# Iniciar el juego
jugar_tic_tac_toe()
