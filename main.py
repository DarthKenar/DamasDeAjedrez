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
    tablero_copia = []

    for i in range(0, cant_damas):

        for j in range(0, cant_damas):
            
            if tablero[i][j] == 0:

                tablero_copia = tablero.copy()

                tablero_copia[i][j] = "D"
                damas_en_tablero += 1
                
                #3
                for movimiento_horizontal in range(j,cant_damas):

                    tablero_copia[i][j + movimiento_horizontal] = 1
                    
                
                
                
            else:
                if cant_damas == damas_en_tablero:
                    
                    tablero_solucion = tablero_copia.copy()
                    soluciones += 1
                else:
                    continue
    
    if soluciones > 0:
        mostrar_tablero(tablero_solucion, cant_damas)
        print(f"La cantidad de soluciones posibles es: {soluciones}")
    else:
        print(f"No se encontraron soluciones para posicionar {cant_damas} damas en un tablero de {cant_damas}x{cant_damas}")

cant_damas = int(input("Ingrese la cantidad de damas: "))
lista = []
tablero = []
#tablero_copia = []

#Creacion de tablero
for i in range(0,cant_damas):

    print("Gola")
    lista.append(0)
    for j in range(0,cant_damas):

        tablero.append(lista)



mostrar_tablero(tablero, cant_damas)
tablero[2][2] = "1"
mostrar_tablero(tablero, cant_damas)