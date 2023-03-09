""""
Escriba un programa en Python usando Numpy que devuelva la letra o letras que faltan de un array de letras crecientes (superiores o inferiores). Suponga que siempre faltará al menos una letra en el array.

Ejemplo 1:

Ingrese los elementos de su array unidimensional separado por comas:

Entrada: q, t, u, v, w

Salida: r, s
"""
# Ejercicio 1.4
import numpy as np


class ejercicio1_4:
    
    faltantes = []
    entrada = ""
    def __init__(self) -> None:
        pass

    def leerArray(self):
        abecedario = np.array(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                          "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"])
        print("Ingrese el elemento de entrada\f")
        entrada = input("Separados entre comas : ")
        entrada=entrada.split(",")#se vuelve una lista entrada
        length = len(abecedario)
        i = 1
        j = 1
        inicial=entrada[0]
        final=entrada[-1]
        valoresFaltantes=[]
        while i<length:#encuentras el valor inicial
            if abecedario[i]==inicial:
                break
# 1 A=A entra
# 2 B=C++
# 3 C=C
# 4 D=E++
# 5 E=E sale
        
        while i<length:# se vuelve a recorrer lalista con le nuevo valor
            print(abecedario[i])
            if(abecedario[i]!=entrada[j]):#si el valor i de abe no es como el valor j de entrada se añade el valor
                valoresFaltantes.append(abecedario[i])
                print(abecedario[i])
                j-=1
            if(abecedario[i]==final):#Si encuentra el valor final se sale del while
                print(abecedario[i])
                break
            i+=1
            j+=1
    
        print(valoresFaltantes)
eje4=ejercicio1_4()
eje4.leerArray()
