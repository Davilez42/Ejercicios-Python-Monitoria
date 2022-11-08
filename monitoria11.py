# palabra = "Univalle"
# lista  = [1,2,3,4,5,6,7]
# print(palabra[0::3])

# def factorial(x):
#     resultado  = 1
#     for i in range(1,x+1):
#         resultado = resultado*i
#     return resultado

# print(factorial(5))


# def factorial_2(x):
#     if x ==0:
#         return 1
#     else:
#         return x*factorial_2(x-1)

# print(factorial_2(5))

def piramide(num):
    contador = 0 
    capa = 1
    while contador < num:
        print (capa)
        capa += 1
        contador += capa 

piramide(7)
tupla = (1,3)
palabra = "Towers es un buen. compañeros"

lista = [x for x in range(1,10) if x%2==0 ]
print(lista)
#hacer un programa que dada una palabra saque las vocales
# y las almacene en una lista 

#hacer un programa que que dado n, genere los primeros numeros pares
print(palabra.split("o"))
#hacer un diccionario que el cual guarde en la clave el nombre de una persona 
#y el valor sera una lista con todos sus datos






