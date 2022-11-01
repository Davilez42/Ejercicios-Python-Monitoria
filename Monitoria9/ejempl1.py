
# n = 0
# while n<10:

#     print(n)
#     n = n +1

# for i in "HolaMundo":
#     print(i,end="*")

# for n in range(0,11):
#     print(n)

# nombres = ["jose","daniel","nicolas"]
# print()

# def convertiraBinario(numero):
#     if(numero==0):
#         return ""
#     if(numero%2==0):
#         return  convertiraBinario((numero/2)) +"0"
#     else:
#         return convertiraBinario(int(numero/2))+ "1"

# print(convertiraBinario(8))


# calcular el tamaño de una lista dada, e
# ejemplos lista1 = ["hola",1,2,3,4,4,5,6,6,6,6]
# retorna 11

# lista1 = [1,2,3,4,"como estas","dasdaf"]
# tamaño = 0
# for x in lista1:
#     tamaño+=1
# # print(tamaño)


# # Calcular la suma de los elementos de una lista
# # ejemplo h = [1,2,3] retorna 6
# # ejemlo k = [5,5,10] retorna 20
# # ejemplo l = [8,8,2] retorna 18

# h = [1, 2, 3]
# k = [5, 5, 10]
# l = [8, 8, 2]


# def sumar_elementos(lista):
#     n = 0
#     for i in lista:
#         n = n + i
#     return


# print(sumar_elementos(h))
# print(sumar_elementos(k))
# print(sumar_elementos(l))


# # calcular el numero mayor de una lista
# # ejemplo [1,2,3,4,5,6,7,78,56,4,3,4,5] retorna 78
# #max() min()
# # ejemplo[ 75,6,7,8,997] retorna 997
# m =[1,2,3,4,5,6,7,78,56,4,3,4,5]


# def calcular_mayor(lista:list):
#     numero_maximo = lista[0]
#     for i in lista:
#         if i>numero_maximo:
#             numero_maximo = i

#     return numero_maximo

# print(calcular_mayor(m))
tiempos_registrados = ["Menos de 6 horas","Entre 6 y 9 horas","mas de 9"]

def calcular_horas(horas):
    if horas<6:
        return 1
    elif horas>=6 and horas<9:
        return 2
    elif horas>9:
        return 3        


def punto5(n):
    actividad_principal = ["Leer","Ver television","Hacer deporte","Dormir"]
    registros = []
    for i in range(n):
        horas = int(input("Ingrese las horas semanal:"))
        codigo_actividad = int(input("Ingrese el codigo de la actividad"))
        registros.append([calcular_horas(horas),(codigo_actividad-1)])
    
    cantidad_leer_69 = 0
    for l in registros:
        for k in l:
            if k[0]==2  and k[1]==1:
                cantidad_leer_69+=1

punto5(3)        
        








