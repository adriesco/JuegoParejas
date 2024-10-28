import random

def tablero():

    while True:
        filas = int(input("Elige el número de filas (2-6): "))
        columnas = int(input("Elige el número de columnas (2-5): "))
        
        # Calcular el total de posiciones
        total_posiciones = filas * columnas

        # Se comprueba el tamaño del tablero si es par se imprime el tablero si no se muestra un mensaje de error
        if 2 <= filas <= 6 and 2 <= columnas <= 5:
            if total_posiciones % 2 == 0:
                print("Mostrando tablero...")
                
                tablero = []  

                for _ in range(filas): 
                    fila = ['_'] * columnas  
                    tablero.append(fila)  

                for fila in tablero:
                    print(" ".join(fila))  # en este print se imprime cada fila del tablero
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
