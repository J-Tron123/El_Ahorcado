from random import randint
import os

palabras = ["programar", "data", "science", "python", "machine", "learning"]

palabra = palabras[randint(0, len(palabras)-1)].upper()
vidas = 6
print("\nEste es el juego del ahoracado, sigue las intrucciones que te doy, si te equivocas 6 veces pierdes\n")
print("_ " * len(palabra))

restantes = list(palabra)
acertadas = []

while vidas > 0:
    if len(restantes) == 0:
        os.system("cls")
        print(f"Ganaste, la palabra era '{palabra}' y la adivinaste")
        break
    else:
        letra = input("Introduce una letra: ").upper()
        if letra in restantes:
            os.system("cls")
            print("Acertaste\n")
            acertadas.append(letra)
            while letra in restantes:
                restantes.pop(restantes.index(letra))
            for i in palabra:
                if i in acertadas:
                    print(i, end=" ")
                else:
                    print("_", end=" ")
            print("")
            continue
        else:
            os.system("cls")
            vidas -= 1
            print(f"Inténtalo de nuevo, te quedan {vidas} vidas")
            for i in palabra:
                if i in acertadas:
                    print(i, end=" ")
                else:
                    print("_", end=" ")
            print("")

if vidas == 0:
    os.system("cls")
    print(f"Perdiste, la palabra era '{palabra}' y no la adivinaste")