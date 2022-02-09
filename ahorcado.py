from random import randint
import os

def intento(letra, vidas):
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
    else:
        os.system("cls")
        print("Inténtalo de nuevo")
        for i in palabra:
            if i in acertadas:
                print(i, end=" ")
            else:
                print("_", end=" ")
        vidas -= 1

palabras = ["programar", "data", "science", "python", "machine", "learning"]

palabra = palabras[randint(0, 5)]
vidas = 6
print("\nEste es el juego del ahoracado, sigue las intrucciones que te doy, si te equivocas 6 veces pierdes\n")
print("_ " * len(palabra))

restantes = list(palabra)
acertadas = []

while vidas > 0:
    if len(restantes) == 0:
        os.system("cls")
        print(f"\nGanaste, la palabra era '{palabra}' y la adivinaste")
        break
    else:
        letra = input("Introduce una letra: ").lower()
        intento(letra, vidas)


if vidas == 0:
    os.system("cls")
    print(f"\nPerdiste, la palabra era '{palabra}' y no la adivinaste")