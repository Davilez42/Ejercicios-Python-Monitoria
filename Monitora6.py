from pickle import TRUE
from unittest import result


lista_nombres = ["Jose","Davidd","Daniel","Nicolas","Luisa"]
lista_edades = [19,67,23,12,12]


lista_nombres.append(235)
lista_nombres.remove(235)
#print(lista_nombres.index("Luisa"))
lista_nombres.insert(3,"Hola como estas")
lista_edades.sort(reverse=False)
print(lista_nombres.pop(0))
print("/////////////////////////////")
'''

indice = 0Luisa
while indice<len(lista_nombres):
    print(lista_nombres[indice])
    indice+=1
'''
for i in lista_nombres:
    print(i)



#hacer una funcion que  ingrese una cadena y te vuelva la cadena
# con las letras intercaladas ejemplo ingresso "BienVenidos"
# y la funcion me devuelve bIENvENIDOS

#n = input("Ingrese un palabra: ")
def funcion_while(palabra:str)->str:
    palabra_aux = palabra.upper()
    resultado = ""
    indice = 0
    while indice<len(palabra):
        if palabra[indice] == palabra_aux[indice]:
            resultado += palabra[indice].lower()
        else:
             resultado += palabra[indice].upper() 
        indice+=1      
    return resultado
#print(funcion_while(n))


def funcion_for(palabra:str)->str:
    resultado = ""
    for letra in palabra:
        if letra == letra.upper():
            resultado+=letra.lower()
        else:
            resultado += letra.upper()
    return resultado
#print(funcion_for(n))

#hacer un programa que dado una palabra extraiga las vocales y las
#guarde en una lista 
n = input("Ingrese un palabra: ")
resultado = [x for x in n if x in "aeiouAEIOU"]
print(resultado)   


Lista_numeros = [x for x in range(0,10)]

import random as r
def contraseña_aleaotoria(n):
    carecteres = "aeious12345?%$#"
    contraseña = ""
    for i in range(0,n):
        x  = r.randint(0,13)
        contraseña += carecteres[x]
    return contraseña

for i in range(0,10):
    print(contraseña_aleaotoria(20))
import numpy as np

matriz = np.array( [[1,2,3],
           [4,5,6],
           [7,8,9]])

print(matriz)           











        