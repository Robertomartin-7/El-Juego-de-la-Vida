import random

def crear_tablero(filas: int, columnas: int) -> list[list[bool]]:
    """
    Crea un nuevo tablero vacío, con todas las células muertas.
    Parametros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
    Devuelve:
        Una lista de listas con todos los elementos False.
    """
    tablero = []
    for i in range (filas):
        fila = []
        for j in range (columnas):
            fila.append(False)  
        tablero.append(fila) 
    
    return tablero

def crear_tablero_aleatorio(filas: int, columnas: int, probabilidad_vida: float) -> list[list[bool]]:
    """
    Crea un tablero con células vivas distribuidas aleatoriamente.

    Parámetros:
        filas (int): Número de filas del tablero.
        columnas (int): Número de columnas del tablero.
        probabilidad_vida (float): Un valor entre 0.0 y 1.0 que representa la
                                   probabilidad de que una célula esté viva.

    Devuelve:
        Una lista de listas que representa el tablero con células vivas (True) y muertas (False).
    """
    tablero = crear_tablero(filas, columnas)
    for i in range (filas):
        for j in range (columnas):
            if random.random() < probabilidad_vida:
                tablero[i][j] = True
            else:
                tablero[i][j] = False
    return tablero

def insertar_patron(tablero: list[list[bool]], patron: list[list[bool]], pos_fila: int, pos_col: int):
    """
    Inserta un patrón (una pequeña matriz) en el tablero en una posición dada.
    Parámetros:
        tablero (list[list[bool]]): El tablero donde se insertará el patrón.
        patron (list[list[bool]]): El patrón a insertar.
        pos_fila (int): La fila en la que se insertará la esquina superior izquierda del patrón.
        pos_col (int): La columna en la que se insertará la esquina superior izquierda del patrón.
    """

    num_filas_patron = len(patron)
    num_columnas_patron = len(patron[0])

    for i in range(num_filas_patron):
        for j in range(num_columnas_patron):
            tablero[pos_fila + i][pos_col + j] = patron[i][j]
    return tablero


def contar_vecinos(tablero: list[list[bool]], fila: int, col: int) -> int:
    """
    Cuenta el número de vecinos vivos de una célula en la posición (fila, col).
    El tablero es toroidal, lo que significa que los bordes se conectan.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
        fila (int): La fila de la célula.
        col (int): La columna de la célula.
    Devuelve:
        El número de vecinos vivos (int).
    """ 
    vecinos = 0

    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == 0 and j == 0:
                continue
            f_vecina = (fila + i) % len(tablero)
            c_vecina = (col + j) % len(tablero[0])
            if tablero[f_vecina][c_vecina]:
                vecinos += 1
    return vecinos


def calcular_siguiente_generacion(tablero):
    """
    Calcula el estado del tablero en el siguiente paso de tiempo basándose en las reglas
    del Juego de la Vida.
    Parámetros:
        tablero (list[list[bool]]): El tablero actual.
    Devuelve:
        Una nueva lista de listas que representa el tablero en la siguiente generación.
    """
    filas = len(tablero)
    columnas = len(tablero[0])

    res = []
    for k in range(filas):
        fila = [False] * columnas
        res.append(fila)
    
    for i in range(filas):
        for j in range(columnas):
            vecinos_vivos = contar_vecinos(tablero, i, j)
            # Celda viva
            if tablero[i][j]:
                # Supervivencia: sigue viva si tiene 2 o 3 vecinas vivas
                res[i][j] = vecinos_vivos in (2, 3)
            else:
                # Nacimiento: una celda muerta revive si tiene exactamente 3 vecinas vivas
                res[i][j] = vecinos_vivos == 3

    return res
    # TODO: Ejercicio 5

