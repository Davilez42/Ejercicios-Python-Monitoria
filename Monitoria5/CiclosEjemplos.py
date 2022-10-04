'''
opcion = 0
while opcion!=3:
    print("1.-------")
    print("2.-------")
    print("3.Salir")
    opcion = int(input("Ingrese una opcion:"))
    if opcion!=3 and opcion!=2 and opcion!=1:
        print("Opcion invalida")
        break
'''
from functools import partial
from tkinter import END


nombre = "JoseDavid"
for i in nombre:
    print(i)



lista1 = ["Tomate","CilantroSalvaje","Peperoni"]
lista1.insert(0,"jaja")
print(lista1[0])
print(lista1)
print("Tomate" in lista1)

#Dado la palabra "Bienvenidos" extraer las vocales
# y guardarlas en una lista o una cadena" 
'''
vocales = ["a","e","i","o","u"]
vocales_extraidas = []
for letra in "Bienvenidos":
    if letra in vocales:
        vocales_extraidas.append(letra)
print(vocales_extraidas)
'''   
'''       
vocales = ""
i = 1
for letra in "Bienvenidos":
    i+=1
    if i<len("Bienvenidos"):
        if letra in "aeiou":
            vocales+= letra+","
    else:
        if letra in "aeiou":
            vocales+= letra

        
print(vocales)

#crea un programa que dado un numero imprima 
#en pantalla un "*" dependiendo del 
# numero ingresado

#n = int(input("ingrese n:"))

for i in range(0,n):
    for i in range(n):
        print("*",end=" ")
    print()    

print("///////////////////////////////////")
for i in range(n):#Superior
    print("*",end=" ")   

print()
for i in range(0,n-2):#filas
    for i in range(0,n):#columnas
        if i==0 or i==n-1:
            print("*",end=" ")
        else:
             print(" ",end=" ")   
    print()   

for i in range(n):#Inferior
    print("*",end=" ")



#crear una funcion que dada un numero
#genere un cuenta regresiva y cuando llegue a 
#cero imprima "BOOM!!"
'''  
def cuenta_Regresiva_while(n):
    indice = n
    while indice>0:
        print(indice)
        indice-=1
        if indice ==0:
            print("BOOOM!!")
        


#cuenta_Regresiva_while(10)

def cuenta_regresiva_for(n):
    print("|",end="")
    for i in range(n,0,-1):
        print(i,end="|")
        if (i-1)==0:
            print("BOOOM!|")

cuenta_regresiva_for(10) 


def calcular_Palindromo(palabra):
    tamaño = len(palabra)
    for i in range(0,tamaño):
        if not palabra[i]== palabra[(tamaño-1)-i]:
            return "No es un palindromo"
    return "Es un palindromo"

print(calcular_Palindromo("reconocer"))