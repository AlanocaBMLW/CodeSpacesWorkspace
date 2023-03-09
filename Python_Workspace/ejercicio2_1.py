#Ejercicio 2.1
#Genere aleatoriamente un array bidimensional solicitando el numero de filas y columnas, y el rango mínimo y máximo de los
# valores enteros generados. Extraiga y muestre las filas y las columnas que contengan todos los elementos diferentes.
import numpy as np
class ejercicio2_1:
    def __init__(self) -> None:
      pass
    def generarArray(self):
      filas=int(input("Ingrese el numero de filas"))
      columnas=int(input("Ingrese el numero de columnas"))
      minimo=int(input("Ingrese el rango minimo"))
      maximo=int(input("Ingrese el rango maximo"))
      generado = np.random.randint(minimo,maximo,(filas,columnas))
      print(generado)
      i = 0#fila
      j=0#columna recorrida
      lenght=len(generado)
      fila=[]
      flag=0
      while i<lenght:#agarramos elementos de la fila y i es el numero de fila
        fila=generado[i]#agarra la fila i y lo pone e la fila
        while j<len(fila):#recorre la columna j
          if fila[j]!=generado[i,j]:
            flag=1#flag es 1 solo si tiene un elemento diferente   
          j+=1
        i+=1
        j=0
        
      
      if flag==1:
        print(fila)
        

       
       



