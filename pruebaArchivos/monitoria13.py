
matriz = [[1,2,0],
          [3,4,7],
          [3,4,7],
          [3,4,7]]

for i in matriz:
    for k in i:
        print(k,end=" ")
    print("")

#cree una matriz la cual va ser n x m donde n y m son datos que ingresas el usuario,
#  la matriz se llena con numeros aleatorios

import random as r
n = int(input("Ingrese las filas:"))
m =  int(input("Ingrese las columnas:"))

matriz2 = []

for i in range(n):
    fila = []
    for k in range(m):
        fila.append(r.randint(0,9))
    matriz.append(fila)    

for i in matriz:
    for k in i:
        print(k,end=" ")
    print("")
