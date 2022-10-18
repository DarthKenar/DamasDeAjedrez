def mostrar_tablero (tablero, cant_damas):

    for i in range(0, cant_damas):

        for j in range(0, cant_damas):

            print(f"[{tablero[i][j]}]", end="")

        print("\n")

def comprobacion (tablero, cant_damas):

    damas_en_tablero = 0
    for i in range(0, cant_damas):

        for j in range(0, cant_damas):
        
            if tablero[i][j] == 0:

                tablero[i][j] = "D"
                damas_en_tablero += 1
                #Introducir valor 1 en casillas donde ataque esta dama
                for q in range(i)
                
            else:
                continue
            

cant_damas = int(input("Ingrese la cantidad de damas: "))
lista = []
tablero = []

#Creacion de tablero
for i in range(0,cant_damas):

    print("Gola")
    lista.append(0)

for j in range(0,cant_damas):

    tablero.append(lista)

mostrar_tablero(tablero, cant_damas)




