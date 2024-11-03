import random

def modo1():
    while True:
        filas = int(input("Elige el número de filas (2-6): "))
        columnas = int(input("Elige el número de columnas (2-5): "))
        
        # Calcular el total de posiciones
        total_posiciones = filas * columnas

        # Verificar que el tamaño del tablero sea válido y par
        if 2 <= filas <= 6 and 2 <= columnas <= 5:
            if total_posiciones % 2 == 0:
                # Crear tablero inicial con interrogaciones
                tablero = [['❓' for _ in range(columnas)] for _ in range(filas)]

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
                
                # Bucle While para jugar hasta que se revelen todas las cartas
                jugador1_puntuacion = 0
                jugador2_puntuacion = 0
                turnos = 0  # Contador de turnos para alternar entre jugadores
                
                while True:
                    print("\nTablero actual:")
                    for fila in tablero:
                        print(" ".join(fila))

                    # Pedir al usuario las coordenadas de las cartas
                    fila_1 = int(input("\nJugador 1 , elige la fila de la carta: "))
                    col_1 = int(input("\nJugador 1 , elige la fila de la carta: "))
                    fila_2 = int(input("\nJugador 2 , elige la fila de la carta: "))
                    col_2 = int(input("\nJugador 2 , elige la fila de la carta: "))

                    # Verificar que las posiciones seleccionadas son diferentes
                    if 0 <= fila_1 < filas and 0 <= col_1 < columnas and 0 <= fila_2 < filas and 0 <= col_2 < columnas:
                        if (fila_1, col_1) != (fila_2, col_2):
                            # Mostrar las cartas seleccionadas temporalmente
                            tablero[fila_1][col_1] = tablero_invisible[fila_1][col_1]
                            tablero[fila_2][col_2] = tablero_invisible[fila_2][col_2]
                            
                            print("Tablero con las cartas visibles:")
                            for fila in tablero:
                                print(" ".join(fila))
                            
                            # Verificar si las cartas seleccionadas forman un par
                            if tablero[fila_1][col_1] == tablero[fila_2][col_2]:
                                print("¡Par encontrado!")
                                if turnos % 2 == 0: 
                                    jugador1_puntuacion += 5
                                else:  
                                    jugador2_puntuacion += 5
                            else:
                                print("No es un par. Intenta de nuevo.")
                                tablero[fila_1][col_1] = '❓' 
                                tablero[fila_2][col_2] = '❓' 
                            
                            # Se comprueba si el juego ha terminado , es decir , que no hay mas interrograciones en el tablero
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
                                    print("Jugador 1 es el ganador y ha ganado en " , turnos)
                                    main()
                                else:
                                    print("Jugador 2 es el ganador y ha ganado en " , turnos)
                                    main()
                                break
                            
                            
                            turnos += 1
                        else:
                            print("Las posiciones elegidas deben ser diferentes.")
                    else:
                        print("Error: Las coordenadas están fuera del rango del tablero.")
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
            print("Bienvenido a la opción Persona vs Persona")
            nombre1 = input("Ingrese el nombre del jugador 1: ")
            nombre2 = input("Ingrese el nombre del jugador 2: ")
            modo1()
            
        elif menu == 2:
            print("Bienvenido a la opción Persona vs Máquina")
            
            
        elif menu == 3:
            print("Bienvenido a la opción Máquina vs Máquina")
            
            
        elif menu == 4:
            print("Gracias por jugar")
            break
            
        else:
            print("Opción no válida, por favor intente nuevamente")

main()
