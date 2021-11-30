import os
import readchar

#DECLARACION DE CONSTANTES
POSICION_X = 0
POSICION_Y = 1
MAP_ANCHO = 20
MAP_ALTO = 15

#DECLARACION DE VARIABLES
cont_serpiente = 1
indice = 0
hacomido = False
posicion_jugador = [3, 5]
posicion_obstaculos = [[7, 6], [8,5], [3,7], [13, 10]]
while True:
    serpiente = "@" * cont_serpiente
    #DIBUJAR MAPA
    print("+" + "-" * MAP_ANCHO * 3 + "+")

    for coordenada_x in range(MAP_ALTO):
        print("|", end="")
        for coordenada_y in range(MAP_ANCHO):
            char_to_draw = " "
            for obstaculo in posicion_obstaculos:
                if obstaculo[POSICION_X] == coordenada_x and obstaculo[POSICION_Y] == coordenada_y:
                    char_to_draw = "*"

            if posicion_jugador[POSICION_X] == coordenada_x and posicion_jugador[POSICION_Y] == coordenada_y:
                print(" {} ".format(serpiente), end="")
            else:
                print(" {} ".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * MAP_ANCHO * 3 + "+")

    #ELIMINA OBSTACULOS Y HACE QUE CREZCA LA SERPIENTE
    if len(posicion_obstaculos) >= 0:
        for obstaculo in posicion_obstaculos:
            if obstaculo[POSICION_X] == posicion_jugador[POSICION_X] and obstaculo[POSICION_Y] == posicion_jugador[POSICION_Y]:
                hacomido = True
            elif hacomido == False:
                indice += 1

        if hacomido == True:
            cont_serpiente += 1
            posicion_obstaculos.pop(indice)

    hacomido = False
    indice = 0

    #PREGUNTAMOS AL USUARIO
    direccion = readchar.readchar().decode()

    if direccion == "w":
        posicion_jugador[POSICION_X] -= 1
        posicion_jugador[POSICION_X] = posicion_jugador[POSICION_X] % MAP_ALTO

    elif direccion == "s":
        posicion_jugador[POSICION_X] += 1
        posicion_jugador[POSICION_X] = posicion_jugador[POSICION_X] % MAP_ALTO

    elif direccion == "a":
        posicion_jugador[POSICION_Y] -= 1
        posicion_jugador[POSICION_Y] = posicion_jugador[POSICION_Y] % MAP_ANCHO

    elif direccion == "d":
        posicion_jugador[POSICION_Y] += 1
        posicion_jugador[POSICION_Y] = posicion_jugador[POSICION_Y] % MAP_ANCHO

    elif direccion == "q":
        break

    os.system("cls")