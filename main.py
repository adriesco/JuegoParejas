import random
import sys

def cerrar_programa():
    sys.exit()

def modo3():
    while True:
        filas = int(input("Elige el número de filas para hacer el tablero (2-6): "))
        columnas = int(input("Elige el número de columnas para hacer el tablero (2-5): "))

        # Calcular el total de posiciones
        total_posiciones = filas * columnas

        # Verificar que el tamaño del tablero sea válido y par
        if 2 <= filas <= 6 and 2 <= columnas <= 5 and total_posiciones % 2 == 0:
            # Crear tablero inicial con interrogaciones
            tablero = []
            for _ in range(filas): 
                fila = ['❓'] * columnas  
                tablero.append(fila)  

            # Lista de emojis para las cartas
            emojis = ["🍕", "🍔", "🍟", "🍣", "🍩", "🍪", "🍿", "🍎", "🍇", "🍉", "🍒", "🔞", "🐷", "⚽", "💩"]
            num_pares = total_posiciones // 2
            cartas = (emojis[:num_pares] * 2)[:total_posiciones]
            random.shuffle(cartas)

            # Asignar cartas al tablero oculto
            tablero_invisible = []
            for i in range(filas):
                fila = []
                for j in range(columnas):
                    fila.append(cartas.pop())
                tablero_invisible.append(fila)

            maquina1_puntuacion = 0
            maquina2_puntuacion = 0
            jugador_actual = True
            memoria_maquina = {}

            while True:
                # Mostrar tablero actual
                print("\nTablero actual:")
                for fila in tablero:
                    print(" ".join(fila))

                if jugador_actual:
                    print("\nTurno de Máquina 1")
                else:
                    print("\nTurno de Máquina 2")

                # Selección de cartas para la máquina
                cartas_disponibles = []
                for i in range(filas):
                    for j in range(columnas):
                        if tablero[i][j] == '❓':
                            cartas_disponibles.append((i, j))
                carta_encontrada = False

                # Verificar la memoria
                for carta, pos1 in memoria_maquina.items():
                    if carta in [tablero_invisible[i][j] for i, j in cartas_disponibles]:
                        for i, j in cartas_disponibles:
                            if tablero_invisible[i][j] == carta and (i, j) != pos1:
                                fila_1, col_1 = pos1
                                fila_2, col_2 = i, j
                                carta_encontrada = True
                                break
                    if carta_encontrada:
                        break

                if not carta_encontrada:
                    fila_1, col_1 = random.choice(cartas_disponibles)
                    cartas_disponibles.remove((fila_1, col_1))
                    fila_2, col_2 = random.choice(cartas_disponibles)

                # Mostrar selecciones de la máquina
                print("La máquina selecciona la posición (" + str(fila_1 + 1) + ", " + str(col_1 + 1) + ")")
                tablero[fila_1][col_1] = tablero_invisible[fila_1][col_1]
                print("\nTablero con la primera carta:")
                for fila in tablero:
                    print(" ".join(fila))

                print("La máquina selecciona la posición (" + str(fila_2 + 1) + ", " + str(col_2 + 1) + ")")
                tablero[fila_2][col_2] = tablero_invisible[fila_2][col_2]
                print("\nTablero con ambas cartas visibles:")
                for fila in tablero:
                    print(" ".join(fila))

                if tablero[fila_1][col_1] == tablero[fila_2][col_2]:
                    print("¡Par encontrado!")
                    if jugador_actual:
                        maquina1_puntuacion += 2
                    else:
                        maquina2_puntuacion += 2
                    emoji = tablero[fila_1][col_1]
                    if emoji in memoria_maquina:
                        del memoria_maquina[emoji]
                else:
                    print("No es un par. Se ocultan las cartas.")
                    if not jugador_actual:
                        memoria_maquina[tablero_invisible[fila_1][col_1]] = (fila_1, col_1)
                        memoria_maquina[tablero_invisible[fila_2][col_2]] = (fila_2, col_2)
                    tablero[fila_1][col_1] = '❓'
                    tablero[fila_2][col_2] = '❓'
                    jugador_actual = not jugador_actual

                # Comprobar si todas las cartas están descubiertas
                juego_terminado = True
                for fila in tablero:
                    for carta in fila:
                        if carta == '❓':
                            juego_terminado = False
                            break
                    if not juego_terminado:
                        break

                # Si el juego ha terminado, imprimir resultados y el ganador
                if juego_terminado:
                    print("\n¡Juego terminado!")
                    print("Puntuación Final de Máquina 1:", maquina1_puntuacion)
                    print("Puntuación Final de Máquina 2:", maquina2_puntuacion)

                    if maquina1_puntuacion > maquina2_puntuacion:
                        print("Máquina 1 es la ganadora.")
                        main()
                    elif maquina2_puntuacion > maquina1_puntuacion:
                        print("Máquina 2 es la ganadora.")
                        main()
                    else:
                        print("¡Es un empate!")
                        main()
                    break
        else:
            print("Error: El tablero debe tener un número par de posiciones y estar entre 2x2 y 6x5.")



    
    

def modo2():
    while True:
        Jugador = input("Introduce tu nombre: ")
        filas = int(input("Elige el número de filas para hacer el tablero (2-6): "))
        columnas = int(input("Elige el número de columnas para hacer el tablero (2-5): "))

        # Calcular el total de posiciones
        total_posiciones = filas * columnas

        # Verificar que el tamaño del tablero sea válido y par
        if 2 <= filas <= 6 and 2 <= columnas <= 5:
            if total_posiciones % 2 == 0:
                # Crear tablero inicial con interrogaciones
                tablero = []
                for _ in range(filas): 
                    fila = ['❓'] * columnas  
                    tablero.append(fila)  

                # Lista de emojis para las cartas
                emojis = ["🍕", "🍔", "🍟", "🍣", "🍩", "🍪", "🍿", "🍎", "🍇", "🍉", "🍒", "🔞", "🐷", "⚽", "💩"]

                # Asegurarse de tener suficientes pares de cartas
                num_pares = total_posiciones // 2
                cartas = (emojis[:num_pares] * 2)[:total_posiciones]  # Crear pares exactos y recortar
                random.shuffle(cartas)  # Mezclar las cartas

                # Asignar cartas al tablero oculto
                tablero_invisible = []
                n = 0
                for i in range(filas):
                    fila = []
                    for j in range(columnas):
                        fila.append(cartas[n])
                        n += 1
                    tablero_invisible.append(fila)
                
                # Inicialización de puntuaciones y turno
                jugador_puntuacion = 0
                maquina_puntuacion = 0
                jugador_actual = True 
                partida = True
                turnos = 0
                
                # Memoria de la máquina
                memoria_maquina = {} 
                
                # Bucle principal del juego
                while partida:
                    print("\nTablero actual:")
                    for fila in tablero:
                        print(" ".join(fila))
                    
                    # Turno del jugador o de la máquina
                    if jugador_actual:
                        print("\nTurno de " + Jugador)
                        
                        # Primera selección de carta
                        fila_1 = int(input("Elige la fila de la primera carta: "))-1
                        col_1 = int(input("Elige la columna de la primera carta: "))-1
                        
                        # Mostrar la primera carta seleccionada
                        if 0 <= fila_1 < filas and 0 <= col_1 < columnas:
                            tablero[fila_1][col_1] = tablero_invisible[fila_1][col_1]
                            print("\nTablero con la primera carta:")
                            for fila in tablero:
                                print(" ".join(fila))
                        else:
                            print("Coordenadas fuera de rango. Inténtalo de nuevo.")

                        # Segunda selección de carta
                        fila_2 = int(input("Elige la fila de la segunda carta: "))-1
                        col_2 = int(input("Elige la columna de la segunda carta: "))-1
                        
                        # Mostrar la segunda carta seleccionada
                        if 0 <= fila_2 < filas and 0 <= col_2 < columnas:
                            if (fila_1, col_1) != (fila_2, col_2):
                                tablero[fila_2][col_2] = tablero_invisible[fila_2][col_2]
                                print("\nTablero con ambas cartas visibles:")
                                for fila in tablero:
                                    print(" ".join(fila))
                            else:
                                print("Las posiciones elegidas deben ser diferentes.")
                                print("\n")
                                main()
                        else:
                            print("Coordenadas fuera de rango. Inténtalo de nuevo.")
                            
                    else:
                        print("\nTurno de la Máquina")
                        # Primera carta de la máquina
                        cartas_disponibles = []
                        for i in range(filas):
                            for j in range(columnas):
                                if tablero[i][j] == '❓':
                                    cartas_disponibles.append((i, j))
                        
                        # Buscar en la memoria o elegir al azar
                        carta_encontrada = False
                        for carta, pos1 in memoria_maquina.items(): #El .items lo he buscado
                            # Verificar si la carta aún está disponible
                            if carta in [tablero_invisible[i][j] for i, j in cartas_disponibles]:
                                # Buscar la carta en las posiciones disponibles
                                for i, j in cartas_disponibles:
                                    if tablero_invisible[i][j] == carta and (i, j) != pos1:
                                        fila_1, col_1 = pos1
                                        fila_2, col_2 = i, j
                                        carta_encontrada = True
                                        break
                            if carta_encontrada:
                                break

                        if not carta_encontrada:
                            # Si no se encontró la carta, seleccionar dos posiciones random
                            fila_1, col_1 = random.choice(cartas_disponibles)
                            cartas_disponibles.remove((fila_1, col_1))          #El .choice tambien lo he buscado
                            fila_2, col_2 = random.choice(cartas_disponibles)
                        
                        # Mostrar selecciones de la máquina
                        print("La máquina selecciona la posición (" + str(fila_1 + 1) + ", " + str(col_1 + 1) + ")")
                        tablero[fila_1][col_1] = tablero_invisible[fila_1][col_1]
                        print("\nTablero con la primera carta:")
                        for fila in tablero:
                            print(" ".join(fila))
                            
                        print("La máquina selecciona la posición (" + str(fila_2 + 1) + ", " + str(col_2 + 1) + ")")
                        tablero[fila_2][col_2] = tablero_invisible[fila_2][col_2]
                        print("\nTablero con ambas cartas visibles:")
                        for fila in tablero:
                            print(" ".join(fila))
                    
                    # Se comprueba si se encontró un par
                    if tablero[fila_1][col_1] == tablero[fila_2][col_2]:
                        print("¡Par encontrado!")
                        if jugador_actual: 
                            jugador_puntuacion += 2
                        else:  
                            maquina_puntuacion += 2
                            # Se limpia la memoria si se han encontrado una pareja igual
                            emoji = tablero[fila_1][col_1]
                            if emoji in memoria_maquina:
                                del memoria_maquina[emoji]
                    else:
                        print("No es un par. Se ocultan las cartas.")
                        # Guardar en memoria si es el turno de la máquina
                        if not jugador_actual:
                            memoria_maquina[tablero_invisible[fila_1][col_1]] = (fila_1, col_1)
                            memoria_maquina[tablero_invisible[fila_2][col_2]] = (fila_2, col_2)
                        tablero[fila_1][col_1] = '❓' 
                        tablero[fila_2][col_2] = '❓' 
                        jugador_actual = not jugador_actual

                    # Verificar si el juego ha terminado
                    juego_terminado = True
                    for fila in tablero:
                        if '❓' in fila:
                            juego_terminado = False
                            break

                    if juego_terminado:
                        print("\n¡Juego terminado!")
                        print("Puntuación Final de", Jugador + ":", jugador_puntuacion)
                        print("Puntuación Final de la Máquina:", maquina_puntuacion)

                        if jugador_puntuacion == maquina_puntuacion:
                            print("¡Es un empate!")
                            main()
                        elif jugador_puntuacion > maquina_puntuacion:
                            print(Jugador + " es el ganador.")
                            main()
                        else:
                            print("La Máquina es la ganadora.")
                            main()

                    turnos += 1
            else:
                print("Error: El tablero debe tener un número par de posiciones.")
        else:
            print("Error: El tamaño debe estar entre 2x2 y 6x5.")

def modo1():
    while True:
        Jugador1 = input("Introduce el nombre del Jugador 1: ")
        Jugador2 = input("Introduce el nombre del Jugador 2: ")
        filas = int(input("Elige el número de filas para hacer el tablero (2-6): "))
        columnas = int(input("Elige el número de columnas para hacer el tablero (2-5): "))

        # Calcular el total de posiciones
        total_posiciones = filas * columnas

        # Verificar que el tamaño del tablero sea válido y par
        if 2 <= filas <= 6 and 2 <= columnas <= 5:
            if total_posiciones % 2 == 0:
                # Crear tablero inicial con interrogaciones
                tablero = []
                for _ in range(filas): 
                    fila = ['❓'] * columnas  
                    tablero.append(fila)  

                # Lista de emojis para las cartas
                emojis = ["🍕", "🍔", "🍟", "🍣", "🍩", "🍪", "🍿", "🍎", "🍇", "🍉", "🍒", "🔞", "🐷", "⚽", "💩"]

                # Asegurarse de tener suficientes pares de cartas
                num_pares = total_posiciones // 2
                cartas = (emojis[:num_pares] * 2)[:total_posiciones]  # Crear pares exactos y recortar
                random.shuffle(cartas)  # Mezclar las cartas

                # Asignar cartas al tablero oculto
                tablero_invisible = []
                n = 0
                for i in range(filas):
                    fila = []
                    for j in range(columnas):
                        fila.append(cartas[n])
                        n += 1
                    tablero_invisible.append(fila)
                
                # Inicialización de puntuaciones y turno
                jugador1_puntuacion = 0
                jugador2_puntuacion = 0
                jugador_actual = True 
                partida = True
                turnos = 0
                
                # Bucle principal del juego
                while partida:
                    print("\nTablero actual:")
                    for fila in tablero:
                        print(" ".join(fila))
                    
                    # Selección del jugador
                    if jugador_actual:
                        print("\nTurno de " + Jugador1)
                    else:
                        print("\nTurno de " + Jugador2)
                    
                    # Primera selección de carta
                    fila_1 = int(input("Elige la fila de la primera carta: "))-1
                    col_1 = int(input("Elige la columna de la primera carta: "))-1
                    
                    # Mostrar la primera carta seleccionada
                    if 0 <= fila_1 < filas and 0 <= col_1 < columnas:
                        tablero[fila_1][col_1] = tablero_invisible[fila_1][col_1]
                        print("\nTablero con las cartas correspondientes hacia arriba:")
                        for fila in tablero:
                            print(" ".join(fila))
                    else:
                        print("Coordenadas fuera de rango. Inténtalo de nuevo.")

                    # Segunda selección de carta
                    fila_2 = int(input("Elige la fila de la segunda carta: "))-1
                    col_2 = int(input("Elige la columna de la segunda carta: "))-1
                    
                    # Mostrar la segunda carta seleccionada
                    if 0 <= fila_2 < filas and 0 <= col_2 < columnas:
                        if (fila_1, col_1) != (fila_2, col_2):
                            tablero[fila_2][col_2] = tablero_invisible[fila_2][col_2]
                            print("\nTablero con ambas cartas visibles:")
                            for fila in tablero:
                                print(" ".join(fila))
                        else:
                            print("Las posiciones elegidas deben ser diferentes.")
                            print("\n")
                            main()
                            

                    else:
                        print("Coordenadas fuera de rango. Inténtalo de nuevo.")
                        
                    
                    # Verificar si se encontró un par
                    if tablero[fila_1][col_1] == tablero[fila_2][col_2]:
                        print("¡Par encontrado!, Sigue Así")
                        if jugador_actual: 
                            jugador1_puntuacion += 2
                        else:  
                            jugador2_puntuacion += 2
                    else:
                        print("No es un par. Se ocultan las cartas.")
                        tablero[fila_1][col_1] = '❓' 
                        tablero[fila_2][col_2] = '❓' 
                        jugador_actual = not jugador_actual

                    # Verificar si el juego ha terminado (no quedan más cartas ocultas)
                    juego_terminado = True
                    for fila in tablero:
                        if '❓' in fila:
                            juego_terminado = False
                            break

                    if juego_terminado:
                        print("\n¡Juego terminado!")
                        print("Puntuación Final del jugador 1:", jugador1_puntuacion)
                        print("Puntuación Final del jugador 2:", jugador2_puntuacion)

                        if jugador1_puntuacion == jugador2_puntuacion:
                            print("¡Es un empate!")
                            main()
                        elif jugador1_puntuacion > jugador2_puntuacion:
                            print(Jugador1 + " es el ganador.")
                            main()
                        else:
                            print(Jugador2 + " es el ganador.")
                            main()

                    turnos += 1
            else:
                print("Error: El tablero debe tener un número par de posiciones.")
        else:
            print("Error: El tamaño debe estar entre 2x2 y 6x5.")


def main():
    print("Bienvenido a la aplicación de las parejas")
    
    while True:
        print("\nEste es el menú de opciones:")
        print("1. Persona vs Persona")
        print("2. Persona vs Máquina")
        print("3. Máquina vs Máquina")
        print("4. Salir")
        
        menu = int(input("Elija una opción: "))
        
        if menu == 1:
            print("\n")
            print("Bienvenido a la opción Persona vs Persona")
            modo1()
            
        elif menu == 2:
            print("\n")
            print("Bienvenido a la opción Persona vs Máquina")
            modo2()
            
        elif menu == 3:
            print("\n")
            print("Bienvenido a la opción Máquina vs Máquina")
            modo3()
            
            
        elif menu == 4:
            print("Gracias por jugar")
            cerrar_programa()
            
        else:
            print("Opción no válida, por favor intente nuevamente")

main()

