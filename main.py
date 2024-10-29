import random

def tablero():
    while True:
        filas = int(input("Elige el número de filas (2-6): "))
        columnas = int(input("Elige el número de columnas (2-5): "))
        
        # Calcular el total de posiciones
        total_posiciones = filas * columnas

        # Verificar que el tamaño del tablero sea válido y par
        if 2 <= filas <= 6 and 2 <= columnas <= 5:
            if total_posiciones % 2 == 0:
                print("Mostrando tablero...")

                # Crear tablero inicial con interrogaciones
                tablero = []
                for _ in range(filas): 
                    fila = ['❓'] * columnas  
                    tablero.append(fila)  
                
                # Imprimir el tablero inicial
                for fila in tablero:
                    print(" ".join(fila))

                # Lista de emojis para las cartas
                emojis = ["🍕", "🍔", "🍟", "🍣", "🍩", "🍪", "🍿", "🍎", "🍇", "🍉", "🍒", "🔞", "📷", "⚽", "💩"]

                # Asegurarse de tener suficientes pares de cartas
                num_pares = total_posiciones // 2
                cartas = (emojis[:num_pares] * 2)[:total_posiciones]  # Crear pares exactos y recortar
                random.shuffle(cartas)  # Mezclar las cartas

                # Asignar cartas al tablero
                n = 0
                for i in range(filas):
                    for j in range(columnas):
                        tablero[i][j] = cartas[n]
                        n += 1

                # Mostrar el tablero con las cartas asignadas
                print("\nTablero oculto con las cartas:")
                for fila in tablero:
                    print(" ".join(fila))

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
            print("Tablero:")
            tablero()
            
        elif menu == 2:
            print("Bienvenido a la opción Persona vs Máquina")
            tablero()
            
        elif menu == 3:
            print("Bienvenido a la opción Máquina vs Máquina")
            tablero()
            
        elif menu == 4:
            print("Gracias por jugar")
            break
            
        else:
            print("Opción no válida, por favor intente nuevamente")

main()
