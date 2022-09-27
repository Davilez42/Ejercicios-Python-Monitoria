'''
Ejercicio 4
Escribir una función que calcule el área 
de un círculo y otra que calcule el volumen de un
 cilindro usando la primera función.
'''
'''
import math

def area(radio):
    return math.pi*radio**2 

def volumen(r,h):
    return area(r)*h    

radio = float(input("ingrese el radio:"))
h = float(input("ingrese la altura:"))

resultado_volumen = volumen(radio,h)

print(volumen)


'''



def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)



def cuentaRegresiva(n):
    if n== 1:
        return "BOOOM!"
    if n!=1:
        print(n)
        return cuentaRegresiva(n-1) 

def elevar(base ,exponente):
    if exponente ==1:
        return base 
    else :
        return base * elevar(base,exponente-1)               


def fibonacci(n):
    if n==0:
        return 1
    elif n==1:
        return 1

    else :
        return fibonacci(n-1) + fibonacci(n-2)      

#hacer una funcion recursiva que dado un numero me calcule si es par
# o no es par

def calcularPar(n):
    if n==2:
        return True
    elif n>2:
        return calcularPar(n-2)
    else :
        False         


def saberSisPar(n):
    if calcularPar(n):
        return "Es par"
    else:
        return "Es impar"    


print(saberSisPar(257))

#calcular recursivamente si un numero es multiplo de 5
'''
def calcularMultiplo(n):
    if n==0:
        return True   
    elif n
        return calcularMultiplo(n/5)      
    else:
        False$
'''        
#print(calcularMultiplo(8))        


