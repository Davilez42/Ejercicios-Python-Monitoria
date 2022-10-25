# i =0
# while i%2== or i==1:
#     print("hola")
#     if i<10:
#         i+=1
#     else:
#         break 
# lista_carnes = ["pollo","pescado","res","cerdo"] 
# lista_verduras = ["Tomate","Cebolla","Pepino","Zanahoria"] 
# lista_verduras.append("Pollo")
# lista_verduras.extend(lista_carnes)
# lista_verduras.sort(reverse=False)

# numeros = [1,2,3,3,4,5,6,67,65,67,7]
# numeros.insert(0,"Jose")
# numeros.remove()
# print(numeros)

#hacer un programa que dado una lista elimine los elementos repetidos de una 
#lista

lista_ejemplo = [12,2,2,2,21,1,1,7]
resultado = []
for i in range(len(lista_ejemplo)):
    for k in range(len(lista_ejemplo)):
        if lista_ejemplo[i]==lista_ejemplo[k] and i!=k:
            lista_ejemplo[k]="*"

for i in lista_ejemplo:
    if i!="*":
        resultado.append(i)
print(resultado)




#hacer un programa que calcule cuantos elementos par y impar hay en una 
#lista y calcule el prodemio de la lista




#hacer un programa que le ayude a al usuario a guardar una lista de 
#productos con su correspondiente precio, por ultimo calcular
#el valor total de los productos

def insertarDatos():
    lista_resultado = list()
    while True:
        
        nombre = input("ingrese el nombre:")
        valor = int(input("ingrese el valor:"))
        lista_resultado.append([nombre,valor])
        opcion  =  int(input("ingrese 0 si desea salir"))
        if opcion==0:
            break

    return lista_resultado    

def calcularTotal(lsita):
    pass

def menu():
    lista_productos = list()
    while True:
        print("1.ingresar Producto:")
        print("2.Calcular Total:")
        print("3.Salir")
        opcion = int(input("Ingrese la opcion:"))
        if opcion == 1:
          x= insertarDatos()
        elif opcion == 2:
            calcularTotal(lista_productos) 
        elif opcion ==3:
            break       


menu()




