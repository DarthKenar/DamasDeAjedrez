def movimiento_12 (tablero, cant_damas):

    for i in range(tablero, cant_damas):

        for j in range(tablero, cant_damas):

            if tablero[i][j] == "D":
                continue############

def mostrar_tablero (tablero, cant_damas):

    for i in range(0, cant_damas):

        for j in range(0, cant_damas):

            print(f"[{tablero[i][j]}]", end="")

        print("\n")

def comprobacion (tablero, cant_damas):

    soluciones = 0
    damas_en_tablero = 0
    tablero_copia = tablero.copy()

    #Debería agregar doble bucle anidado? para realizar nuevamente la comprobacion cuando no encuentre seolucion?

    for i in range(0, cant_damas):

        for j in range(0, cant_damas):

            # i representada por el valor Y del eje de coordenadas
            # j representada por el valor X del eje de coordenadas

            if tablero_copia[i][j] == 0:

                

                tablero_copia[i][j] = "D"
                damas_en_tablero += 1
                
                #3
                for movimiento_X in range(j,cant_damas):

                    tablero_copia[i][movimiento_X] = 1

                #4.5
                for movimiento_X in range(j, cant_damas):
                    for movimiento_Y in range(i, cant_damas):

                        tablero_copia[movimiento_Y][movimiento_X] = 1
                
                #6
                for movimiento_Y in range(i, cant_damas):

                    tablero_copia[movimiento_Y][j] = 1
                
                #7.5 (good)
                for movimiento_X in range(j-1, 0, -1):
                    for movimiento_Y in range(i+1, cant_damas):
                        
                        tablero_copia[movimiento_Y][movimiento_X] = 1
                
                #9
                for movimiento_X in range(j-1, 0, -1):

                    tablero_copia[i][movimiento_X] = 1
                
                #10.5
                for movimiento_X in range(j-1, 0, -1):
                    for movimiento_Y in range(i-1, 0, -1):

                        tablero_copia[movimiento_Y][movimiento_X] = 1
                
                #12
                for movimiento_Y in range(i-1, 0, -1):

                    tablero_copia[movimiento_Y][j] = 1

                #1.5
                for movimiento_X in range(j, cant_damas):
                    for movimiento_Y in range(i-1, 0, -1):

                        tablero_copia[movimiento_Y][movimiento_X] = 1


    if cant_damas == damas_en_tablero:
        
        tablero_solucion = tablero_copia.copy()
        soluciones += 1
    
    if soluciones > 0:
        mostrar_tablero(tablero_solucion, cant_damas)
        print(f"La cantidad de soluciones posibles es: {soluciones}")
    else:
        print(f"No se encontraron soluciones para posicionar {cant_damas} damas en un tablero de {cant_damas}x{cant_damas}")

cant_damas = int(input("Ingrese la cantidad de damas: "))

#Creacion de tablero inicializado en 0 utilizando la técnica list_comprehension
tablero = [[0 for i in range(cant_damas)]for j in range(cant_damas)]

#prueba para visualización de datos
mostrar_tablero(tablero, cant_damas)
comprobacion(tablero,cant_damas)