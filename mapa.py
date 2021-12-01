import os
import readchar
import random

#DECLARACION DE CONSTANTES
POSICION_X = 0
POSICION_Y = 1
MAP_ANCHO = 20
MAP_ALTO = 15
NUM_OBSTACULOS = 11

#DECLARACION DE VARIABLES
posicion_jugador = [3, 5]


posicion_obstaculos = []


cola_length = 0
cola = []
end_game = False
died = False

while not end_game:
    os.system("cls")

    while len(posicion_obstaculos) < NUM_OBSTACULOS:
        new_obstaculo = [random.randint(0, MAP_ALTO), random.randint(0, MAP_ANCHO)]
        if new_obstaculo not in posicion_obstaculos and posicion_jugador != new_obstaculo:
            posicion_obstaculos.append(new_obstaculo)

    #DIBUJAR MAPA
    print("+" + "-" * MAP_ANCHO * 3 + "+")

    for coordenada_x in range(MAP_ALTO):

        print("|", end="")

        for coordenada_y in range(MAP_ANCHO):

            char_to_draw = " "
            object_in_cell = None
            indice = 0

            for obstaculo in posicion_obstaculos:
                if obstaculo[POSICION_X] == coordenada_x and obstaculo[POSICION_Y] == coordenada_y:
                    char_to_draw = "*"
                    object_in_cell = obstaculo

            for parte_cola in cola:
                if parte_cola[POSICION_X] == coordenada_x and parte_cola[POSICION_Y] == coordenada_y:
                    char_to_draw = "@"

            if posicion_jugador[POSICION_X] == coordenada_x and posicion_jugador[POSICION_Y] == coordenada_y:
                char_to_draw = "@"
                if object_in_cell:
                    posicion_obstaculos.remove(object_in_cell)
                    cola_length += 1
                for objeto_cola in cola:
                    if posicion_jugador[POSICION_X] == objeto_cola[POSICION_X] and posicion_jugador[POSICION_Y] == objeto_cola[POSICION_Y]:
                        end_game = True
                        died = True
            print(" {} ".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * MAP_ANCHO * 3 + "+")

    #PREGUNTAMOS AL USUARIO
    direccion = readchar.readchar().decode()

    if direccion == "w":
        cola.insert(0, posicion_jugador.copy())
        cola = cola[:cola_length]
        posicion_jugador[POSICION_X] -= 1
        posicion_jugador[POSICION_X] = posicion_jugador[POSICION_X] % MAP_ALTO

    elif direccion == "s":
        cola.insert(0, posicion_jugador.copy())
        cola = cola[:cola_length]
        posicion_jugador[POSICION_X] += 1
        posicion_jugador[POSICION_X] = posicion_jugador[POSICION_X] % MAP_ALTO

    elif direccion == "a":
        cola.insert(0, posicion_jugador.copy())
        cola = cola[:cola_length]
        posicion_jugador[POSICION_Y] -= 1
        posicion_jugador[POSICION_Y] = posicion_jugador[POSICION_Y] % MAP_ANCHO

    elif direccion == "d":
        cola.insert(0, posicion_jugador.copy())
        cola = cola[:cola_length]
        posicion_jugador[POSICION_Y] += 1
        posicion_jugador[POSICION_Y] = posicion_jugador[POSICION_Y] % MAP_ANCHO

    elif direccion == "q":
        print("----------------| PARTIDA FINALIZADA POR QUE HA SALIDO DEL JUEGO |---------------- :(")
        end_game = True



    if died:
        print("Has muertooooo")