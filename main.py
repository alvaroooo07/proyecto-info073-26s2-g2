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

# Detecta automáticamente la carpeta donde está guardado este script (.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Apunta a una carpeta dentro de "main"

DIR_TEXTURAS = os.path.join(BASE_DIR, "textures")
DIR_SONIDOS = os.path.join(DIR_TEXTURAS, "sonidos")

# Ruta hacia la subcarpeta de animaciones del ciervo

DIR_CUERPO_CIERVO = os.path.join(DIR_TEXTURAS, "cuerpo ciervo") #carpeta para las nuevas texturas del cuerpo del ciervo (cuando se alarga)
DIR_CUERPO_TRONCO = os.path.join(DIR_TEXTURAS, "cuerpo tronco") #Carpeta para las nuevas texturas del tronco

#--- Direcciones animaciones ciervo ---

DIR_CIERVO_PRINCIPAL = os.path.join(DIR_TEXTURAS, "animaciones ciervo") #Carpeta para las animaciones del ciervo inicial
DIR_ANIM_CABEZA = os.path.join(DIR_CIERVO_PRINCIPAL, "animacion cabeza") #Carpeta para las animaciones de la cabeza ciervo 
DIR_ANIM_TRASERO = os.path.join(DIR_CIERVO_PRINCIPAL, "animacion trasero") #Carpeta para las animaciones del trasero ciervo 
DIR_ANIM_COMPACTO = os.path.join(DIR_CIERVO_PRINCIPAL, "animacion compacto") #Carpeta para las animaciones del ciervo compacto inicial

# El formato de imagen utilizado puede ser PNG, JPG/JPEG, BMP, o GIF.
# Se específica el nombre de la ruta combinando el directorio base y el archivo.
PANTALLA_INICIO = os.path.join(DIR_TEXTURAS, "Pant_Inicio.png")
PANTALLA_INSTRUCCIONES = os.path.join(DIR_TEXTURAS, "instructionTEST.jpg") #
PANTALLA_VICTORIA = os.path.join(DIR_TEXTURAS, "Pant_Victoria.png")
PANTALLA_DERROTA = os.path.join(DIR_TEXTURAS, "Pant_Muerte.png")

# Rutas de música de fondo (pueden ser .mp3 o .ogg)
MUSICA_INICIO = os.path.join(DIR_SONIDOS, "song_inicio.mp3")
MUSICA_JUEGO = os.path.join(DIR_SONIDOS, "song_juego_test.mp3")
MUSICA_VICTORIA = os.path.join(DIR_SONIDOS, "song_victory_test.mp3")
MUSICA_DERROTA = os.path.join(DIR_SONIDOS, "song_dead.mp3")

# Rutas de efectos de sonido (se recomienda .wav o .ogg para efectos cortos)
SND_MANZANA = os.path.join(DIR_SONIDOS, "sfx_manzana.wav")
SND_CHOQUE = os.path.join(DIR_SONIDOS, "sfx_dead.wav")

# Rutas a imágenes personalizadas
# --- ANIMACIONES DE LA CABEZA ---
IMG_JUGADOR_ANIM = {
    (0, 1):  [os.path.join(DIR_ANIM_CABEZA, "deer_down_1.png"),  os.path.join(DIR_ANIM_CABEZA, "deer_down_2.png")],
    (0, -1): [os.path.join(DIR_ANIM_CABEZA, "deer_up_1.png"),    os.path.join(DIR_ANIM_CABEZA, "deer_up_2.png")],
    (-1, 0): [os.path.join(DIR_ANIM_CABEZA, "deer_left_1.png"),  os.path.join(DIR_ANIM_CABEZA, "deer_left_2.png")],
    (1, 0):  [os.path.join(DIR_ANIM_CABEZA, "deer_right_1.png"), os.path.join(DIR_ANIM_CABEZA, "deer_right_2.png")],
    (0, 0):  [os.path.join(DIR_ANIM_CABEZA, "deer_down_1.png"),  os.path.join(DIR_ANIM_CABEZA, "deer_down_2.png")]
}

# --- ANIMACIONES DEL TRASERO ---
IMG_TRASERO_ANIM = {
    (0, 1):  [os.path.join(DIR_ANIM_TRASERO, "tail_down_1.png"),  os.path.join(DIR_ANIM_TRASERO, "tail_down_2.png")],
    (0, -1): [os.path.join(DIR_ANIM_TRASERO, "tail_up_1.png"),    os.path.join(DIR_ANIM_TRASERO, "tail_up_2.png")],
    (-1, 0): [os.path.join(DIR_ANIM_TRASERO, "tail_left_1.png"),  os.path.join(DIR_ANIM_TRASERO, "tail_left_2.png")],
    (1, 0):  [os.path.join(DIR_ANIM_TRASERO, "tail_right_1.png"), os.path.join(DIR_ANIM_TRASERO, "tail_right_2.png")],
    (0, 0):  [os.path.join(DIR_ANIM_TRASERO, "tail_down_1.png"),  os.path.join(DIR_ANIM_TRASERO, "tail_down_2.png")]
}

IMG_OBSTACULO = os.path.join(DIR_TEXTURAS, "rock.png")
IMG_MANZANA = os.path.join(DIR_TEXTURAS, "apple.png") 
IMG_FONDO = os.path.join(DIR_TEXTURAS, "World_Map.png")

# --- NUEVOS SPRITES FIJOS ---
# --- NUEVAS TEXTURAS DEL CUERPO ---
IMG_CUERPO_X = os.path.join(DIR_CUERPO_CIERVO, "body_x.png")       # Lomo horizontal
IMG_CUERPO_Y = os.path.join(DIR_CUERPO_CIERVO, "body_y.png")       # Lomo vertical
IMG_CUERPO_ESQUINA = os.path.join(DIR_CUERPO_CIERVO, "body_corner.png") # Para los giros

# --- NUEVAS TEXTURAS DEL TRONCO ---
IMG_TRONCO_IZQ = os.path.join(DIR_CUERPO_TRONCO, "tronco_izq.png")   # Mitad izquierda
IMG_TRONCO_DER = os.path.join(DIR_CUERPO_TRONCO, "tronco_der.png")   # Mitad derecha

# --- Animacion INICIAL (COMPACTO) ---
IMG_COMPACTO_ANIM = {
    (0, 1):  [os.path.join(DIR_ANIM_COMPACTO, "com_deer_down_1.png"),  os.path.join(DIR_ANIM_COMPACTO, "com_deer_down_2.png")],
    (0, -1): [os.path.join(DIR_ANIM_COMPACTO, "com_deer_up_1.png"),    os.path.join(DIR_ANIM_COMPACTO, "com_deer_up_2.png")],
    (-1, 0): [os.path.join(DIR_ANIM_COMPACTO, "com_deer_left_1.png"),  os.path.join(DIR_ANIM_COMPACTO, "com_deer_left_2.png")],
    (1, 0):  [os.path.join(DIR_ANIM_COMPACTO, "com_deer_right_1.png"), os.path.join(DIR_ANIM_COMPACTO, "com_deer_right_2.png")],
    (0, 0):  [os.path.join(DIR_ANIM_COMPACTO, "com_deer_down_1.png"),  os.path.join(DIR_ANIM_COMPACTO, "com_deer_down_2.png")]
}
# Para evitar que el jugador se mueva demasiado rápido
RETRASO = 200

# Códigos de cada elemento del tablero
VACIO = 0
OBSTACULO = 1
JUGADOR = 2
MANZANA = 3
TRONCO = 4

#Tamaño de la ventana
ANCHO_VENTANA = 1040
ALTO_VENTANA = 800
LADO_TABLERO = 800
ANCHO_PANEL = ANCHO_VENTANA - LADO_TABLERO

# Tamaño del tablero
# Si se cambian estas constantes, se debe modificar la definición
# del tablero que se encuentra en función reiniciar().
FILAS = 15
COLUMNAS = 15

# Condiciones para ganar
MANZANAS_PARA_GANAR = 10

def dibujar_panel(screen,fuente,manzanas_comidas):
    #rectangulo del panel: empieza donde termina el tablero.
    panel = pygame.Rect(LADO_TABLERO, 0 , ANCHO_PANEL , ALTO_VENTANA)
    pygame.draw.rect(screen, "gray15" , panel)

    # Margen izquierdo del texto dentro del panel
    x = LADO_TABLERO + 24

    # Titulo
    titulo = fuente.render("DEAR DEER" , True , "white")
    screen.blit(titulo, (x,30))

    # Contador de manzanas actuales
    contador_txt = fuente.render(f"Manzanas: {manzanas_comidas}", True, "white")
    screen.blit(contador_txt , (x,100))

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

#creamos una funcion para que aparezca un tronco de 1x2 en el tablero si no lo puede colocar se elimina el primer bloque y se intenta nuevamente
def aparecer_tronco(tablero):
    while True:
        columna, fila = aparecer_aleatorio(tablero, TRONCO, incluir_borde=False)

        # Si la casilla de la derecha está libre, forma un tronco 1x2
        if columna + 1 < COLUMNAS and tablero[fila][columna + 1] == VACIO:
            tablero[fila][columna + 1] = TRONCO
            break

        # Si no se pudo, elimina el primer bloque e intenta nuevamente
        tablero[fila][columna] = VACIO

def poblar_tablero(tablero):
    """
    Coloca un obstáculo y la manzana en el tablero.

    Parámetros:
        - tablero: El tablero con sus posiciones actuales.
    """
    CANT_OBSTACULOS = 10
    cantidad_troncos = 5
    for i in range ( cantidad_troncos ) :
        aparecer_tronco(tablero)
    for i in range ( CANT_OBSTACULOS ) :
        aparecer_aleatorio(tablero, OBSTACULO,incluir_borde = False)
    aparecer_aleatorio(tablero, MANZANA)

#Cambio tomeisor: Agregué el parámetro "incluir_borde" a la función aparecer_aleatorio para que, al colocar obstáculos, no se coloquen en el borde del tablero. Esto hace que el juego sea más justo, ya que el jugador no puede quedar atrapado en una esquina sin posibilidad de movimiento. Además, modifiqué la función poblar_tablero para que los obstáculos se coloquen sin incluir el borde del tablero.
def refrescar_tablero(screen, tablero, sprites_cabeza, sprite_cuerpo_x, sprite_cuerpo_y, sprite_cuerpo_esquina, sprites_trasero, sprites_compacto, sprite_obstaculo, sprite_tronco_izq, sprite_tronco_der, sprite_manzana, sprite_fondo, direccion, frame_actual, pos_cuerpo, manzanas_comidas, fuente):
    # ETAPA 1: Dibujar el fondo
    screen.blit(sprite_fondo, (0, 0))
    alto_elem = LADO_TABLERO / FILAS
    ancho_elem = LADO_TABLERO / COLUMNAS

    # ETAPA 2: Dibujar elementos estáticos del mapa
    for i in range(FILAS):
        for j in range(COLUMNAS):
            pos_x = j * ancho_elem
            pos_y = i * alto_elem
            
            if tablero[i][j] == OBSTACULO:
                screen.blit(sprite_obstaculo, (pos_x, pos_y))
                
            elif tablero[i][j] == TRONCO:
                # Si la casilla a la izquierda está dentro de la matriz y también es TRONCO,
                # significa que esta casilla actual es la parte derecha del tronco.
                if j - 1 >= 0 and tablero[i][j - 1] == TRONCO:
                    screen.blit(sprite_tronco_der, (pos_x, pos_y))
                else:
                    screen.blit(sprite_tronco_izq, (pos_x, pos_y))
                    
            elif tablero[i][j] == MANZANA:
                screen.blit(sprite_manzana, (pos_x, pos_y))

    # ETAPA 3: Dibujar la anatomía del ciervo
    # CASO ESPECIAL: Si la partida recién inicia y mide 1 casilla, se ve el cuerpo completo compacto
    if len(pos_cuerpo) == 1:
        col, fila = pos_cuerpo[0]
        # Buscamos la lista de animación según la dirección; si no existe, usa la de por defecto (0, 0)
        lista_animacion = sprites_compacto.get(direccion, sprites_compacto[(0, 0)])
        screen.blit(lista_animacion[frame_actual], (col * ancho_elem, fila * alto_elem))
    else:
        # Si ya se alargó, dibujamos pieza por pieza secuencialmente
        for indice, pos in enumerate(pos_cuerpo):
            col, fila = pos
            pos_x = col * ancho_elem
            pos_y = fila * alto_elem

            if indice == 0:
                # CABEZA
                lista_animacion = sprites_cabeza.get(direccion, sprites_cabeza[(0, 0)])
                screen.blit(lista_animacion[frame_actual], (pos_x, pos_y))

            elif indice == len(pos_cuerpo) - 1:
                # TRASERO
                # Obtenemos el bloque de cuerpo justo antes de la cola
                bloque_anterior = pos_cuerpo[indice - 1]
                
                # dirección real del trasero (restando las posiciones)
                # bloque_anterior (x, y) - cola (x, y)
                dir_trasero_x = bloque_anterior[0] - col
                dir_trasero_y = bloque_anterior[1] - fila
                dir_trasero = (dir_trasero_x, dir_trasero_y)

                # Busca la animación usando su propia dirección calculada
                lista_animacion = sprites_trasero.get(dir_trasero, sprites_trasero[(0, 0)])
                screen.blit(lista_animacion[frame_actual], (pos_x, pos_y))

            else:
                # CUERPO INTERMEDIO (Lógica de conexiones e intermedios)
                pos_anterior = pos_cuerpo[indice - 1] # Hacia la cabeza
                pos_siguiente = pos_cuerpo[indice + 1] # Hacia el trasero
                
                # Evaluamos los ejes comparando los vecinos
                mismo_eje_x = (pos_anterior[0] == col == pos_siguiente[0])
                mismo_eje_y = (pos_anterior[1] == fila == pos_siguiente[1])
                
                if mismo_eje_x:
                    # El segmento viene de arriba y va hacia abajo (Eje vertical Y)
                    screen.blit(sprite_cuerpo_y, (pos_x, pos_y))
                elif mismo_eje_y:
                    # El segmento viene de la izquierda y va a la derecha (Eje horizontal X)
                    screen.blit(sprite_cuerpo_x, (pos_x, pos_y))
                else:
                    # ¡LOGICA DE ESQUINAS ROTATIVAS!
                    # Calculamos los vectores relativos de los dos vecinos respecto a la casilla actual
                    vecino1_x = pos_anterior[0] - col
                    vecino1_y = pos_anterior[1] - fila
                    vecino2_x = pos_siguiente[0] - col
                    vecino2_y = pos_siguiente[1] - fila
                    
                    # Sumamos los vectores para saber en qué diagonal se forma el "codo" o esquina
                    G_X = vecino1_x + vecino2_x
                    G_Y = vecino1_y + vecino2_y
                    
                    
                    # que conecta la ARRIBA con la DERECHA (Esquina Superior Derecha ◜ )
                    if G_X == 1 and G_Y == -1:    # Conecta Arriba y Derecha
                        esquina_rotada = sprite_cuerpo_esquina
                    elif G_X == -1 and G_Y == -1:  # Conecta Arriba e Izquierda (Girar 90° en sentido horario)
                        esquina_rotada = pygame.transform.rotate(sprite_cuerpo_esquina, 90)
                    elif G_X == -1 and G_Y == 1:   # Conecta Abajo e Izquierda (Girar 180°)
                        esquina_rotada = pygame.transform.rotate(sprite_cuerpo_esquina, 180)
                    elif G_X == 1 and G_Y == 1:    # Conecta Abajo e Derecha (Girar 270°)
                        esquina_rotada = pygame.transform.rotate(sprite_cuerpo_esquina, 270)
                    else:
                        esquina_rotada = sprite_cuerpo_esquina # Fallback por seguridad
                        
                    screen.blit(esquina_rotada, (pos_x, pos_y))
                    
    # Se agrega el panel a la ventana de juego
    dibujar_panel(screen, fuente, manzanas_comidas)

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
    if keys == pygame.K_w and direccion_actual != (0,1):
        # La tupla nos indica que horizontalmente (columnas) no hará nada (0) y
        # que verticalmente (filas) disminuirá el índice en el tablero (-1).
        return (0, -1)

    # Tecla S
    if keys== pygame.K_s and direccion_actual != (0,-1) :
        # En este caso avanzará a través de las filas del tablero.
        return (0, 1)

    # Tecla A
    if keys== pygame.K_a and direccion_actual != (1,0) :
        # Retrocede por las columnas del tablero.
        return (-1, 0)

    # Tecla D
    if keys == pygame.K_d and direccion_actual != (-1,0):
        # Avanza por las columnas del tablero.
        return (1, 0)

    # Si no se presiona ninguna de las teclas anteriores, la dirección
    # será la misma que la anterior.
    return None


def avanzar(tablero, pos_cuerpo, direccion, manzanas_comidas):
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
    ind_actual_col, ind_actual_fila = pos_cuerpo[0]
      # Tupla (columna, fila) que representa los índices en el tablero.


    # Aplicamos la dirección a la posición del jugador.
    ind_nueva_col = ind_actual_col + dir_col
    ind_nueva_fila = ind_actual_fila + dir_fila

    # Verificamos que no haya choque con el borde del tablero.
    if not (0 <= ind_nueva_col < COLUMNAS and 0 <= ind_nueva_fila < FILAS):
        return "derrota", pos_cuerpo, manzanas_comidas 

    # Obtenemos el elemento que se encuentre en el tablero en la nueva posición del jugador.
    pos_elem = tablero[ind_nueva_fila][ind_nueva_col]

    if pos_elem == OBSTACULO or pos_elem == TRONCO:
        return "derrota", pos_cuerpo, manzanas_comidas 
    
    # Verificamos que no choque contra si mismo
    if (ind_nueva_col, ind_nueva_fila) in pos_cuerpo [:-1]:
        return "derrota", pos_cuerpo, manzanas_comidas

    ind_cola_col, ind_cola_fila = pos_cuerpo[-1]

    for i in range (len(pos_cuerpo)-1,0,-1):
        pos_cuerpo[i] = pos_cuerpo [i-1]
    
    pos_cuerpo[0]= (ind_nueva_col, ind_nueva_fila)
    tablero[ind_nueva_fila][ind_nueva_col]=JUGADOR

    tablero[ind_cola_fila][ind_cola_col] = VACIO
    
    if pos_elem == MANZANA :
        manzanas_comidas += 1
        # Mover al jugador a la nueva casilla
        pos_cuerpo.append((ind_cola_col, ind_cola_fila))
        tablero[ind_cola_fila][ind_cola_col]=JUGADOR
        # Si llegamos al objetivo, victoria
        if manzanas_comidas >= MANZANAS_PARA_GANAR:
            return "victoria", pos_cuerpo, manzanas_comidas
        aparecer_aleatorio(tablero, MANZANA)
        return "manzana", pos_cuerpo, manzanas_comidas

    return "ok", pos_cuerpo, manzanas_comidas
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
    pos_cuerpo = [aparecer_aleatorio(tablero, JUGADOR)]

    return tablero, pos_cuerpo


def reproducir_musica(ruta_archivo):
    """Detiene la música actual y reproduce una nueva en bucle infinito."""
    try:
        pygame.mixer.music.stop()
        pygame.mixer.music.load(ruta_archivo)
        pygame.mixer.music.play(-1) # -1 significa que se repetirá indefinidamente
    except pygame.error:
        print(f"No se pudo reproducir el archivo de música: {ruta_archivo}")


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
        imagen = pygame.transform.scale(imagen, (LADO_TABLERO, ALTO_VENTANA))

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

    #Establecemos la resolucion de la pantalla.
    screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    
    # Establecemos la fuente que aparecera en el panel
    fuente = pygame.font.SysFont("Courier New", 30)

    #Establecemos el titulo de la ventana
    pygame.display.set_caption("DEAR DEER")

    tamano_casilla = (int(LADO_TABLERO / COLUMNAS), int(ALTO_VENTANA / FILAS))
    
    # DICCIONARIO PARA GUARDAR LOS SPRITES YA PROCESADOS
    sprites_jugador_escalados = {}
    sprites_trasero = {} # Se inicializa el diccionario vacío aquí
    sprites_compacto = {}

    try:
        # CARGA Y ESCALA DE ANIMACIONES DE LA CABEZA Y TRASERO
        for dir_tupla, rutas_lista in IMG_JUGADOR_ANIM.items():
            sprites_jugador_escalados[dir_tupla] = [
                pygame.transform.scale(pygame.image.load(ruta).convert_alpha(), tamano_casilla)
                for ruta in rutas_lista
            ]
        for dir_tupla, rutas_lista in IMG_TRASERO_ANIM.items():
            sprites_trasero[dir_tupla] = [
                pygame.transform.scale(pygame.image.load(ruta).convert_alpha(), tamano_casilla)
                for ruta in rutas_lista
            ]
        for dir_tupla, rutas_lista in IMG_COMPACTO_ANIM.items():
            sprites_compacto[dir_tupla] = [
                pygame.transform.scale(pygame.image.load(ruta).convert_alpha(), tamano_casilla)
                for ruta in rutas_lista
            ]

        # CORRECCIÓN: Cargar los sprites individuales que faltaban
        sprite_obstaculo = pygame.transform.scale(pygame.image.load(IMG_OBSTACULO).convert_alpha(), tamano_casilla)
        sprite_manzana = pygame.transform.scale(pygame.image.load(IMG_MANZANA).convert_alpha(), tamano_casilla)
        sprite_fondo = pygame.transform.scale(pygame.image.load(IMG_FONDO).convert(), (LADO_TABLERO, ALTO_VENTANA))
        
        # --- NUEVOS SPRITES CARGADOS ---
        # Carga de variaciones del lomo/cuerpo
        sprite_cuerpo_x = pygame.transform.scale(pygame.image.load(IMG_CUERPO_X).convert_alpha(), tamano_casilla)
        sprite_cuerpo_y = pygame.transform.scale(pygame.image.load(IMG_CUERPO_Y).convert_alpha(), tamano_casilla)
        sprite_cuerpo_esquina = pygame.transform.scale(pygame.image.load(IMG_CUERPO_ESQUINA).convert_alpha(), tamano_casilla)
        
        # Carga de las dos mitades del tronco continuo
        sprite_tronco_izq = pygame.transform.scale(pygame.image.load(IMG_TRONCO_IZQ).convert_alpha(), tamano_casilla)
        sprite_tronco_der = pygame.transform.scale(pygame.image.load(IMG_TRONCO_DER).convert_alpha(), tamano_casilla)
        
        # Cargar objetos de efectos de sonido
        sonido_manzana = pygame.mixer.Sound(SND_MANZANA)
        sonido_choque = pygame.mixer.Sound(SND_CHOQUE)
        
        # Asignamos cabeza usando el diccionario de animaciones que ya cargué
        sprites_cabeza = sprites_jugador_escalados
        # Nota: sprites_trasero se cargó correctamente arriba con mis propias imágenes

    except FileNotFoundError as e:
        print(f"Error al cargar los sprites: {e}. Asegúrate de que existan en la carpeta.")
        pygame.quit()
        return

    running = True
    estado = ESTADO_INICIO
    tablero = []
    pos_cuerpo = []
    direccion = (0, 0)
    direccion_actual = (0,0)
    tiempo_ultimo_mov = 0
    manzanas_comidas = 0
    frame_actual = 0

    mostrar_pantalla(screen, PANTALLA_INICIO)
    reproducir_musica(MUSICA_INICIO)
    paso_procesado = True  

    while running:
        tiempo_actual = pygame.time.get_ticks()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False

            if evento.type == pygame.KEYDOWN:
                # 1. ESTADO INICIO
                if estado == ESTADO_INICIO:
                    if evento.key == pygame.K_SPACE:
                        tablero, pos_cuerpo = reiniciar() # REEMPLAZADO: Faltaba inicializar el tablero aquí
                        manzanas_comidas = 0
                        direccion = (0, 0)
                        direccion_actual = (0,0)
                        frame_actual = 0 
                        tiempo_ultimo_mov = pygame.time.get_ticks()
                        estado = ESTADO_JUGANDO
                        reproducir_musica(MUSICA_JUEGO) 
                        
                        # Limpia el búfer de teclas antes de empezar
                        pygame.event.clear(pygame.KEYDOWN) 
                        
                        # CORRECCIÓN LÍNEA 617: Pasamos todos los argumentos reales
                        refrescar_tablero(screen, tablero, sprites_cabeza, sprite_cuerpo_x, sprite_cuerpo_y, sprite_cuerpo_esquina, sprites_trasero, sprites_compacto, sprite_obstaculo, sprite_tronco_izq, sprite_tronco_der, sprite_manzana, sprite_fondo, direccion, frame_actual, pos_cuerpo, manzanas_comidas, fuente)
                    
                    elif evento.key == pygame.K_i:
                        estado = ESTADO_INSTRUCCIONES
                        mostrar_pantalla(screen, PANTALLA_INSTRUCCIONES)

                # 2. ESTADO INSTRUCCIONES
                elif estado == ESTADO_INSTRUCCIONES:
                    estado = ESTADO_INICIO
                    mostrar_pantalla(screen, PANTALLA_INICIO)

                # 3. ESTADOS FINALES
                elif estado in (ESTADO_DERROTA, ESTADO_VICTORIA):
                    if evento.key == pygame.K_r:
                        tablero, pos_cuerpo = reiniciar() # REEMPLAZADO: Faltaba inicializar al reiniciar
                        manzanas_comidas = 0
                        direccion = (0, 0)
                        direccion_actual = (0,0)
                        frame_actual = 0
                        tiempo_ultimo_mov = pygame.time.get_ticks()
                        estado = ESTADO_JUGANDO
                        reproducir_musica(MUSICA_JUEGO) 
                        
                        pygame.event.clear(pygame.KEYDOWN) 
                        
                        # CORRECCIÓN AQUÍ TAMBIÉN: Pasamos todos los argumentos reales
                        refrescar_tablero(screen, tablero, sprites_cabeza, sprite_cuerpo_x, sprite_cuerpo_y, sprite_cuerpo_esquina, sprites_trasero, sprites_compacto, sprite_obstaculo, sprite_tronco_izq, sprite_tronco_der, sprite_manzana, sprite_fondo, direccion, frame_actual, pos_cuerpo, manzanas_comidas, fuente)
                    
                    if evento.key == pygame.K_ESCAPE:
                        estado = ESTADO_INICIO
                        reproducir_musica(MUSICA_INICIO) 
                        mostrar_pantalla(screen, PANTALLA_INICIO)

                # 4. ESTADO JUGANDO (Solo aquí reacciona a WASD)
                elif estado == ESTADO_JUGANDO:
                    # Filtramos para que solo procese si la tecla es efectivamente de movimiento
                    if evento.key in (pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d):
                        if paso_procesado:  
                            nueva_dir = cambiar_direccion(evento.key, direccion_actual)
                            if nueva_dir is not None:
                                direccion = nueva_dir
                                paso_procesado = False  

        # --- LÓGICA DE MOVIMIENTO ---
        if estado == ESTADO_JUGANDO:
            if direccion != (0, 0) and tiempo_actual - tiempo_ultimo_mov >= RETRASO:
                resultado, pos_cuerpo, manzanas_comidas = avanzar(tablero, pos_cuerpo, direccion, manzanas_comidas)

                if resultado == "derrota":
                    estado = ESTADO_DERROTA
                    sonido_choque.play()             # Efecto de choque
                    reproducir_musica(MUSICA_DERROTA)# Música de Game Over
                    mostrar_pantalla(screen, PANTALLA_DERROTA)
                elif resultado == "victoria":
                    estado = ESTADO_VICTORIA
                    sonido_manzana.play()             # Come la última manzana
                    reproducir_musica(MUSICA_VICTORIA)# Música de Victoria
                    mostrar_pantalla(screen, PANTALLA_VICTORIA)
                else:
                    if resultado == "manzana":
                        sonido_manzana.play()

                    tiempo_ultimo_mov = tiempo_actual
                    direccion_actual = direccion
                    frame_actual = 1 - frame_actual 
                    paso_procesado = True  
                    
                    refrescar_tablero(screen, tablero, sprites_cabeza, sprite_cuerpo_x, sprite_cuerpo_y, sprite_cuerpo_esquina, sprites_trasero, sprites_compacto, sprite_obstaculo, sprite_tronco_izq, sprite_tronco_der, sprite_manzana, sprite_fondo, direccion, frame_actual, pos_cuerpo, manzanas_comidas, fuente)

    pygame.quit()


if __name__ == "__main__":
    main()
