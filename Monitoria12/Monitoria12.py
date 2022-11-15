# conjunto1 = {1,2,3,4,54,3}
# conjunto2 = {1,3,49,9,10}

# conjunto =  set()
# lista = list()
# tupla = tuple()

# # print(conjunto1.intersection(conjunto2).difference(conjunto1))
# # print(conjunto1.union(conjunto2))

# matrizA = [[1,2,3],[4,5,6]]

# # print(matrizA[1][1])

# for i in matrizA:
    
#     for k in i:
#         print(k, end=" ")
#     print()    

# #hacer un program que le pida al usuario 
# #el numero de filas y el numero de columnas
# #y hacer una matriz con los valores dados (la ma
# # matriz se llena con numeros aleatorios)
# import random as r
# fil = int(input("ingrese el numero de filas:"))
# col = int(input("ingrese el numero de columnas:"))


# matriz = []
# for k in range(fil):
#     fila_aux = []
#     for i in range(col):
#         fila_aux.append(r.randint(0,100))
#     matriz.append(fila_aux)  



# for i in matriz:   
#     for k in i:
#         print(k, end=" ")
#     print()   


# #hacer una funcion que reciba una matriz y un valor 
# #a encontrar, esta funcion retorna verdadero si
# # el valor se encuentra en la matriz y falso si no
# # 
# def buscar(matriz,valor):
#     for i in matriz:
#         if valor in i:
#             return True
#     return False           

#hacer una funcion que reciba una matriz y retorne
#la suma de todos sus elementos
import numpy as np
from os import system
from random import randint
import time
matriz = np.array(
[["","","",""],["","","",""],["","","",""],["","","",""]]
)

# for i in range(16):
#      system("cls")
#      for k in range(4):   
#          for j in range(4):
#              matriz[k][j] = randint(0,10)
#      time.sleep(2)
#      print(matriz)         
for i in range(16):
     system("cls")
     filas = randint(0,3)
     col = randint(0,3)
     if matriz[filas][col]!=1:
         matriz[filas][col] = "*"    
     for i in matriz:
        for k in i:
            print(k,end=" ")
        print()    
     time.sleep(2)      











