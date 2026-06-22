# Importamos módulos requeridos
import os
import random
import pygame.image
import pygame
import sys

# Estados del juego
ESTADO_INICIO = "inicio"
ESTADO_INSTRUCCIONES = "instrucciones"
ESTADO_JUGANDO = "jugando"
ESTADO_DERROTA = "derrota"
ESTADO_VICTORIA = "victoria"

# Rutas a la carpeta de imágenes de pantallas
DIR_PANTALLAS = os.path.join(os.path.dirname(__file__), "data", "pantallas")

# 1. Detectar automáticamente la carpeta donde está guardado este script (.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Apuntar a una carpeta dentro de tu proyecto (por ejemplo: "Textures")
DIR_TEXTURAS = os.path.join(BASE_DIR, "Textures")

# El formato de imagen utilizado puede ser PNG, JPG/JPEG, BMP, o GIF.
# Se específica el nombre de la ruta combinando el directorio base y el archivo.
PANTALLA_INICIO = os.path.join(DIR_TEXTURAS, "inicioTEST.jpg")
PANTALLA_INSTRUCCIONES = os.path.join(DIR_TEXTURAS, "instructionTEST.jpg")
PANTALLA_VICTORIA = os.path.join(DIR_TEXTURAS, "victoryTEST.jpg")
PANTALLA_DERROTA = os.path.join(DIR_TEXTURAS, "lostTEST.jpg")

# Rutas a imágenes personalizadas
IMG_PERSONAJE = os.path.join(DIR_TEXTURAS, "deerTEST.png")
IMG_OBSTACULO = os.path.join(DIR_TEXTURAS, "rockTEST.jpg")
IMG_MANZANA = os.path.join(DIR_TEXTURAS, "appleTEST.jpg")
IMG_FONDO = os.path.join(DIR_TEXTURAS, "world_mapTEST.jpg")

# Para evitar que el jugador se mueva demasiado rápido
RETRASO = 200

# Códigos de cada elemento del tablero
VACIO = 0
OBSTACULO = 1
JUGADOR = 2
MANZANA = 3

# Tamaño del tablero
# Si se cambian estas constantes, se debe modificar la definición
# del tablero que se encuentra en función reiniciar().
FILAS = 15
COLUMNAS = 15
MANZANAS_PARA_GANAR = 5


def aparecer_aleatorio(tablero, id_elem, incluir_borde = True):
    """
    Coloca un elemento en una casilla vacía aleatoria del tablero.

    Parámetros:
        - tablero: El tablero con sus posiciones actuales.
        - id_elem: El número identificador del elemento que queremos colocar.

    Retorna:
        - (columna, fila): Tupla que indica posición en la que se colocó el elemento.
    """

    # Debemos detectar los espacios vacíos, para ello recorremos
    # el tablero y almacenamos tuplas de (columna, fila) las posiciones
    # en las que un elemento "VACIO" (el número 0 en este caso) se encuentre.
    vacios = []

    # Forma vista en clases de recorrer el arreglo multidimensional.
    # Tanto fila como columna son números.
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            # Obtenemos el elemento que se encuentra en esa fila y columna.
            elem_pos = tablero[fila][columna]

            if elem_pos == VACIO:
                # Al utilizar los paréntesis () dentro de la función, lo estaremos
                # añadiendo como una tupla con la estructura (columna, fila).
                vacios.append((columna, fila))

    # También se puede utilizar comprensión de listas para rellenar el arreglo
    # a la vez que lo recorremos:
    #
    # vacios = [
    #     (columna, fila)
    #     for fila in range(FILAS)
    #     for columna in range(COLUMNAS)
    #     if tablero[fila][columna] == VACIO
    # ]

    # Si no hay casillas vacías, retornamos un valor especial.
    if not incluir_borde :
        BORDE = ([( c , 0) for c in range ( COLUMNAS ) ]
        + [( c , FILAS - 1) for c in range ( COLUMNAS ) ]
        + [(0 , f ) for f in range (1 , FILAS - 1) ]
        + [( COLUMNAS - 1 , f ) for f in range (1 , FILAS - 1) ])
        vacios = [ pos for pos in vacios if pos not in BORDE ]    
    if len(vacios) == 0:
        return -1, -1

    # Usando la función random.choice(lista) podremos obtener una tupla
    # aleatoria desde el arreglo "vacios" que definimos anteriormente.
    columna, fila = random.choice(vacios)

    # Finalmente, colocamos el elemento al poner su número en la casilla
    # del tablero correspondiente.
    tablero[fila][columna] = id_elem

    return columna, fila


def poblar_tablero(tablero):
    """
    Coloca un obstáculo y la manzana en el tablero.

    Parámetros:
        - tablero: El tablero con sus posiciones actuales.
    """
    CANT_OBSTACULOS = 10
    for i in range ( CANT_OBSTACULOS ) :
        aparecer_aleatorio(tablero, OBSTACULO,incluir_borde = False)
    aparecer_aleatorio(tablero, MANZANA)

#Cambio tomeisor: Agregué el parámetro "incluir_borde" a la función aparecer_aleatorio para que, al colocar obstáculos, no se coloquen en el borde del tablero. Esto hace que el juego sea más justo, ya que el jugador no puede quedar atrapado en una esquina sin posibilidad de movimiento. Además, modifiqué la función poblar_tablero para que los obstáculos se coloquen sin incluir el borde del tablero.
def refrescar_tablero(screen, tablero, sprite_jugador, sprite_obstaculo, sprite_manzana, sprite_fondo):
    """
    Dibuja el estado actual del tablero en la pantalla utilizando imágenes personalizadas.
    """
    # Rellena el fondo
    screen.blit(sprite_fondo, (0, 0))

    # Cálculo del tamaño de cada casilla
    alto_elem = screen.get_height() / FILAS
    ancho_elem = screen.get_width() / COLUMNAS

    # Posición en eje "y" en unidad de píxeles.
    pos_y = 0

    for i in range(FILAS):
        # Posición en eje "x" en unidad de píxeles.
        pos_x = 0
        for j in range(COLUMNAS):
            if tablero[i][j] == OBSTACULO:
                # Dibujamos el obstáculo personalizado
                screen.blit(sprite_obstaculo, (pos_x, pos_y))
                
            elif tablero[i][j] == JUGADOR:
                # Dibujamos al jugador personalizado
                screen.blit(sprite_jugador, (pos_x, pos_y))
                
            elif tablero[i][j] == MANZANA:
                # Dibujamos la manzana personalizada
                screen.blit(sprite_manzana, (pos_x, pos_y))

            # Avanzamos al siguiente elemento en el eje X
            pos_x += ancho_elem
        # Avanzamos al siguiente elemento en el eje Y
        pos_y += alto_elem

    # Refresca el contenido que se ve en pantalla.
    pygame.display.flip()


def cambiar_direccion(keys, direccion_actual):
    """
    Cambia la dirección del jugador.

    Parámetros:
        - keys: Arreglo de teclas presionadas.
        - direccion_actual: La dirección en la que estaba avanzando justo antes de analizar
            si hubo un cambio de dirección.

    Retorna:
        - direccion_actual: La nueva dirección del jugador.
    """

    # Tecla W
    if keys[pygame.K_w]:
        # La tupla nos indica que horizontalmente (columnas) no hará nada (0) y
        # que verticalmente (filas) disminuirá el índice en el tablero (-1).
        return (0, -1)

    # Tecla S
    if keys[pygame.K_s]:
        # En este caso avanzará a través de las filas del tablero.
        return (0, 1)

    # Tecla A
    if keys[pygame.K_a]:
        # Retrocede por las columnas del tablero.
        return (-1, 0)

    # Tecla D
    if keys[pygame.K_d]:
        # Avanza por las columnas del tablero.
        return (1, 0)

    # Si no se presiona ninguna de las teclas anteriores, la dirección
    # será la misma que la anterior.
    return direccion_actual


def avanzar(tablero, pos_jugador, direccion, manzanas_comidas):
    """
    Avanza el jugador un paso en la dirección dada.

    Parámetros:
        - tablero: El tablero con sus posiciones actuales.
        - pos_jugador: Tupla con la posición actual (índice con
            estructura (columna, fila)) del jugador en el tablero.
        - direccion: Tupla con la dirección en la que está avanzando actualmente el jugador.

    Retorna:
        - (resultado, nueva_pos_jugador): Retorna el resultado que se obtiene
            al avanzar (derrota, victoria o "ok" (no cambia de pantalla)) y la nueva posición del jugador.
    """

    # Obtenemos los componentes "x" e "y" de cada tupla recibida
    # con información de la dirección y posición del jugador.
    dir_col, dir_fila = direccion
    ind_actual_col, ind_actual_fila = (
        pos_jugador  # Tupla (columna, fila) que representa los índices en el tablero.
    )

    # Aplicamos la dirección a la posición del jugador.
    ind_nueva_col = ind_actual_col + dir_col
    ind_nueva_fila = ind_actual_fila + dir_fila

    # Verificamos que no haya choque con el borde del tablero.
    if not (0 <= ind_nueva_col < COLUMNAS and 0 <= ind_nueva_fila < FILAS):
        return "derrota", pos_jugador, manzanas_comidas 

    # Obtenemos el elemento que se encuentre en el tablero en la nueva posición del jugador.
    pos_elem = tablero[ind_nueva_fila][ind_nueva_col]

    if pos_elem == OBSTACULO:
        return "derrota", pos_jugador, manzanas_comidas 

    if pos_elem == MANZANA :
        manzanas_comidas += 1
        # Mover al jugador a la nueva casilla
        tablero [ ind_actual_fila ][ ind_actual_col ] = VACIO
        tablero [ ind_nueva_fila ] [ ind_nueva_col ] = JUGADOR
        # Si llegamos al objetivo, victoria
        if manzanas_comidas >= MANZANAS_PARA_GANAR:
            return "victoria", (ind_nueva_col, ind_nueva_fila), manzanas_comidas
        aparecer_aleatorio(tablero, MANZANA)
        return "ok", (ind_nueva_col, ind_nueva_fila), manzanas_comidas

    tablero[ind_actual_fila][ind_actual_col] = VACIO
    tablero[ind_nueva_fila][ind_nueva_col] = JUGADOR
    return "ok", (ind_nueva_col, ind_nueva_fila), manzanas_comidas
def reiniciar():
    """
    Crea un nuevo tablero y estado para una nueva partida.

    Retorna:
        - (tablero, pos_jugador): Tablero nuevo y la nueva posición aleatoria del jugador.
            pos_jugador corresponda a una tupla (columna, fila) donde columna y fila son índices
            de matriz tablero.
    """

    # Si se modifica constante FILAS o COLUMNAS al inicio, también
    # se debe modificar este arreglo de tablero con los valores correspondientes.
    # Esto puede ser mejorado usando dos bucles "for" anidados o comprensión de listas.
    tablero = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    # Usando dos bucles "for" anidados se haría de la siguiente manera:
    # tablero = []
    # for _ in range(FILAS):
    #     fila_tablero = []
    #
    #     for _ in range(COLUMNAS):
    #         fila_tablero.append(VACIO)
    #
    #     tablero.append(fila_tablero)
    # Otra manera usando comprensión de listas:
    # tablero = [[VACIO] * COLUMNAS for _ in range(FILAS)]
    # El _ en el "for" indica que no usamos la variable con la que iteramos.

    poblar_tablero(tablero)

    # Colocamos al jugador en una posición aleatoria.
    pos_jugador = aparecer_aleatorio(tablero, JUGADOR)

    return tablero, pos_jugador


def mostrar_pantalla(screen, nombre_archivo):
    """
    Carga una imagen y la muestra escalada a la ventana.

    Parámetros:
        - screen: La pantalla donde colocaremos la imagen.
        - nombre_archivo: El nombre del archivo de la imagen.
    """

    #ruta = os.path.join(DIR_PANTALLAS, nombre_archivo)
    ruta = nombre_archivo

    try:
        imagen = pygame.image.load(ruta)
        imagen = pygame.transform.scale(imagen, screen.get_size())

        # Dibujamos la imagen en la pantalla en la coordenada (0, 0).
        screen.blit(imagen, (0, 0))

        # Refrescamos pantalla.
        pygame.display.flip()
    except FileNotFoundError:
        # Fallback de seguridad en caso de que las imágenes no existan aún
        screen.fill("black")
        pygame.display.flip()
        print(f"Advertencia: No se encontró la imagen {ruta}")


def main():
    pygame.init()

    # Establecemos la resolución de la pantalla.
    screen = pygame.display.set_mode((800, 800))

    # Establecemos el título de la ventana.
    pygame.display.set_caption("Juego Básico")

    # Calculamos el tamaño exacto que debe tener cada imagen en píxeles
    tamano_casilla = (int(screen.get_width() / COLUMNAS), int(screen.get_height() / FILAS))
    
    # Cargamos y escalamos los diseños para que encajen perfecto en la cuadrícula
    try:
        sprite_jugador = pygame.transform.scale(pygame.image.load(IMG_PERSONAJE).convert_alpha(), tamano_casilla)
        sprite_obstaculo = pygame.transform.scale(pygame.image.load(IMG_OBSTACULO).convert_alpha(), tamano_casilla)
        sprite_manzana = pygame.transform.scale(pygame.image.load(IMG_MANZANA).convert_alpha(), tamano_casilla)
        # Cargamos el fondo escalado al tamaño completo de la pantalla (800x800)
        sprite_fondo = pygame.transform.scale(pygame.image.load(IMG_FONDO).convert(), screen.get_size())
        #imagen de pantallas
        
    except FileNotFoundError as e:
        print(f"Error al cargar los sprites: {e}. Asegúrate de que existan en la carpeta.")
        pygame.quit()
        return
    # ---------------------------------

    running = True

    estado = ESTADO_INICIO
    tablero = []
    pos_jugador = (0, 0)
    direccion = (0, 0)
    tiempo_ultimo_mov = 0
    manzanas_comidas = 0
    mostrar_pantalla(screen, PANTALLA_INICIO)

    # Este es el bucle principal del juego, todo lo que sucede en el juego
    # está aquí.
    while running:
        # Se analizan los eventos del bucle actual.
        for evento in pygame.event.get():
            # Si es que se quiere cerrar la ventana.
            if evento.type == pygame.QUIT:
                running = False

            # Si es que se presiona alguna tecla.
            if evento.type == pygame.KEYDOWN:
                if estado == ESTADO_INICIO:
                    if evento.key == pygame.K_SPACE:
                        tablero, pos_jugador = reiniciar()
                        manzanas_comidas = 0
                        direccion = (0, 0)
                        # Obtiene tiempo en milisegundos
                        tiempo_ultimo_mov = pygame.time.get_ticks()
                        estado = ESTADO_JUGANDO
                        refrescar_tablero(screen, tablero, sprite_jugador, sprite_obstaculo, sprite_manzana, sprite_fondo)
                    elif evento.key == pygame.K_i:
                        estado = ESTADO_INSTRUCCIONES
                        mostrar_pantalla(screen, PANTALLA_INSTRUCCIONES)

                elif estado == ESTADO_INSTRUCCIONES:
                    estado = ESTADO_INICIO
                    mostrar_pantalla(screen, PANTALLA_INICIO)

                elif estado in (ESTADO_DERROTA, ESTADO_VICTORIA):
                    if evento.key == pygame.K_r:
                        tablero, pos_jugador = reiniciar()
                        manzanas_comidas= 0
                        direccion = (0, 0)
                        tiempo_ultimo_mov = pygame.time.get_ticks()
                        estado = ESTADO_JUGANDO
                        refrescar_tablero(screen, tablero, sprite_jugador, sprite_obstaculo, sprite_manzana, sprite_fondo)

                    if evento.key == pygame.K_ESCAPE:
                        estado = ESTADO_INICIO
                        mostrar_pantalla(screen, PANTALLA_INICIO)

                elif estado == ESTADO_JUGANDO:
                    direccion = cambiar_direccion(pygame.key.get_pressed(), direccion)

        if estado == ESTADO_JUGANDO:
            tiempo_actual = pygame.time.get_ticks()  # En milisegundos

            # La variable RETRASO hace que si no han pasado esa cantidad de ticks,
            # entonces no se avanzará en el tablero.
            if direccion != (0, 0) and tiempo_actual - tiempo_ultimo_mov >= RETRASO:
                resultado, pos_jugador, manzanas_comidas = avanzar (tablero, pos_jugador, direccion, manzanas_comidas)

                if resultado == "derrota":
                    estado = ESTADO_DERROTA
                    mostrar_pantalla(screen, PANTALLA_DERROTA)
                elif resultado == "victoria":
                    estado = ESTADO_VICTORIA
                    mostrar_pantalla(screen, PANTALLA_VICTORIA)
                else:
                    tiempo_ultimo_mov = tiempo_actual
                    refrescar_tablero(screen, tablero, sprite_jugador, sprite_obstaculo, sprite_manzana, sprite_fondo)

    pygame.quit()


if __name__ == "__main__":
    main()
