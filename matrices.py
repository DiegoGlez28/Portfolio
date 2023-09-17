# Diego Arturo González Juárez
# pruebas listas y matrices

import random


def crear_matriz(y, x):
    matriz = []
    for j in range(y):
        matriz.append([])
        for i in range(x):
            num = random.randint(-100, 100)
            matriz[j].append(num)
    return matriz


def imprimir_matriz(matriz):
    for y in matriz:
        for x in y:
            print(x, "\t", end = "")
        print()
    print()


def suma_matrices(a, b):
    resultado = []
    for j in range(len(a)):
        resultado.append([])
        for i in range(len(b)):
            resultado[j].append(a[j][i] + b[j][i])
    return resultado


def suma_columnas(matriz):
    y = len(matriz)
    x = len(matriz[0])
    total = []
    for i in range(x):
        suma = 0
        for j in range(y):
            suma = suma + matriz[j][i]
        total.append(suma)
    return total


if __name__ == '__main__':
    matriz1 = crear_matriz(2, 2)
    imprimir_matriz(matriz1)
    imprimir_matriz(suma_columnas(matriz1))

