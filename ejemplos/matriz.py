
import random as t
import numpy as np
def  crearMatriz(n,m,valor):
    frecuencia = 0
    matriz = []
    for i in range(n):
        filas = []
        for j in range(m):
            filas.append(t.randint(0,50))
        matriz.append(filas)            
    frecuencia =  calc_fre(matriz,valor)
    matriz = np.array(matriz)
    print(matriz)

    return frecuencia

def calc_fre(m,v):
    total = 0
    for i in m:
        for k in i:
            if k == v:
                total +=1

    return total            
            

