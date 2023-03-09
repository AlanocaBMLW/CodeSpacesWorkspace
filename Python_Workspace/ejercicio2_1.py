#Ejercicio 2.1
#Genere aleatoriamente un array bidimensional solicitando el numero de filas y columnas, y el rango mínimo y máximo de los
# valores enteros generados. Extraiga y muestre las filas y las columnas que contengan todos los elementos diferentes.
import numpy as np
class ejercicio2_1:
  def __init__(self) -> None:
        pass
  def generarArray(self):
    filas=input("Ingrese el numero de filas")
    columnas=input("Ingrese el numero de columnas")
    minimo=input("Ingrese el rango minimo")
    maximo=input("Ingrese el rango maximo")
    generado = np.random.randint(minimo,maximo,(filas,columnas))
    i = 0
    lenght=len(generado)
    while i<lenght:
       



