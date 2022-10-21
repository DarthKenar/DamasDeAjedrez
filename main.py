def show_chessboard (tablero, queens_number):

    for i in range(0, queens_number):

        for j in range(0, queens_number):

            print(f"[{tablero[i][j]}]", end="")

        print("\n")

def queen_threat(x, y):

    if chessboard_transfer[x][y] != "D":

        chessboard_transfer[x][y] = 1

def verification (chessboard_template, queens_number):


    

    for posicion_nueva_dama_y in range(0, queens_number):
        for posicion_nueva_dama_x in range(0, queens_number):

            #renueva el tablero para que inicie una nueva verification desde 0 con el indice adelantado
            chessboard_transfer = chessboard_template.copy()
            #Ayuda a reconocer cuantas damas hay en el tablero
            queens_counter = 0
            #Indicates the number of solutions found
            solutions = 0

            for i in range(posicion_nueva_dama_y, queens_number):
                for j in range(posicion_nueva_dama_x, queens_number):

                    # i representada por el valor Y del eje de coordenadas
                    # j representada por el valor X del eje de coordenadas

                    if chessboard_transfer[i][j] == 0:

                        

                        chessboard_transfer[i][j] = "D"
                        queens_counter += 1
                        
                        #3
                        for move_x in range(j,queens_number):
                            
                            queen_threat(i, move_x)

                        #4.5
                        for move_x in range(j, queens_number):
                            for move_y in range(i, queens_number):

                                queen_threat(move_y, move_x)
                        
                        #6
                        for move_y in range(i, queens_number):

                            queen_threat(move_y, j)
                        
                        #7.5 (good)
                        for move_x in range(j-1, 0, -1):
                            for move_y in range(i+1, queens_number):
                                
                                queen_threat(move_y, move_x)
                        
                        #9
                        for move_x in range(j-1, 0, -1):

                            queen_threat(i, move_x)
                        
                        #10.5
                        for move_x in range(j-1, 0, -1):
                            for move_y in range(i-1, 0, -1):

                                queen_threat(move_y, move_x)
                        
                        #12
                        for move_y in range(i-1, 0, -1):

                            queen_threat(move_y, j)

                        #1.5
                        for move_x in range(j, queens_number):
                            for move_y in range(i-1, 0, -1):

                                queen_threat(move_y, move_x)


            if queens_number == queens_counter:
                
                chessboard_solution = chessboard_transfer.copy()
                solutions += 1
            
    if solutions > 0:

        show_chessboard(chessboard_solution, queens_number)
        print(f"The number of possible solutions is : {solutions}")

    else:
        print(f"No solutions were found to position {queens_number} queens on a {queens_number}x{queens_number} board")

queens_number = int(input("Enter the number of queens: "))

#Board creation initialized to 0 using the list_comprehension technique
chessboard_template = [[0 for i in range(queens_number)]for j in range(queens_number)]
chessboard_transfer = chessboard_template.copy()
#test for data visualization
verification(chessboard_template,queens_number)