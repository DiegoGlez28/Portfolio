#Autor: Diego Arturo González Juárez (IDM)
#grafica contagios por día en México

import csv
import matplotlib.pyplot as plt


def graficar_contagios(datos):
    """grafica el número de contagios registrados por día en México, recibe como parámetro los datos en forma de
    Matriz"""
    contagios = []
    
    for renglon in datos:
        if (renglon[0] == "MEX") and (renglon[3].startswith("2021")):
            contagios.append(int(renglon[5]))
    
    plt.plot(contagios, "r")
    plt.title("Contagios por día en México")
    plt.xlabel("Número de día en 2021")
    plt.ylabel("Contagios")
    plt.show()
    
    
def calcular_max_contagios(datos):
    """calcula el máximo de contagios en México en 2021, recibe los datos como parámetro"""
    contagios = []
    
    for renglon in datos:
        if (renglon[0] == "MEX") and (renglon[3].startswith("2021")):
            contagios.append(int(renglon[5]))
    
    maximo = max(contagios)
    return maximo


def calcular_min_contagios(datos):
    """calcula el mínimo de contagios en México en 2021, recibe los datos como parámetro"""
    contagios = []
    
    for renglon in datos:
        if (renglon[0] == "MEX") and (renglon[3].startswith("2021")):
            contagios.append(int(renglon[5]))
    
    minimo = min(contagios)
    return minimo


def calcular_promedio(datos):
    """calcula el promedio de contagios en México en 2021, recibe los datos como parámetro"""
    contagios = []
    
    for renglon in datos:
        if (renglon[0] == "MEX") and (renglon[3].startswith("2021")):
            contagios.append(int(renglon[5]))
    
    promedio = sum(contagios)/len(contagios)
    return promedio


if __name__ == '__main__':
    archivo = open("datos_covid.csv")
    entrada = csv.reader(archivo)
    datos = list(entrada)[1:]
    graficar_contagios(datos)
    maximo = calcular_max_contagios(datos)
    print("Valor mayor de contagios en 2021:", maximo)
    minimo = calcular_min_contagios(datos)
    print("Valor menor de contagios en 2021:", minimo)
    promedio = calcular_promedio(datos)
    print("Promedio de contagios diarios en 2021: %0.2f" % promedio)

