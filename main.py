import random;

def tablero():
#Aqui se solicita al juador que elija el tamañao del tablero
    while True:
            filas = int(input("Elige el número de filas (2-6): "))
            columnas = int(input("Elige el número de columnas (2-5): "))
            
            #Se multiplica las filas para saber si el total de posiciones es par o impar
            totalposiciones = filas*columnas

            if 2<=filas<=6 and 2<=columnas<=5:
                if totalposiciones%2==0:
                    break
                else:
                    print("El tamaño del tablero no es válido , debe tener un numero ")
            else:
                print("El tamaño tiene que estar entre 2x2 o 6x5")

    #Aqui va un for con el simbolo para formar el tablero
                


        


def main():
    print("Bienvenido a la aplicación de las parejas");
    print("Este es el menú de las opciones ...");
    print("1. Persona vs Persona");
    print("2. Persona vs Maquina");
    print("3. Maquina vs Maquina");
    print("4. Salir");
    menu=int(input("Elija una opción: "));
    if menu==1:
        print("Bienvenido a la opción Perosna vs Persona");
        print("1. Jugador 1");
        nombre1=input("Ingrese el nombre del jugador 1: ");
        print("2. Jugador 2");
        nombre2=input("Ingrese el nombre del jugador 2: ");
        print("Tablero:" + tablero);
        tablero();
    elif menu==2:
        print("Bienvenido a la opción Perosna vs Maquina");
        tablero();
    elif menu==3:
        print("Bienvenido a la opción Maquina vs Maquina");
        tablero();
    else :
        print("Gracias por jugar");
        exit();