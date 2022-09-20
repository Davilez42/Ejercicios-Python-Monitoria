

#hacer un programa que reciba 3 notas
#con su porcentaje correspondiente y calcule la calificacion 
#Final


n1 =  float(input("Ingrese la nota 1:"))
porcentaje1 = float(input("Ingrese el porcenta de la nota: "))
n2 =  float(input("Ingrese la nota 2:"))
porcentaje2 = float(input("Ingrese el porcenta de la nota: "))
n3 =  float(input("Ingrese la nota 3:"))
porcentaje3 = float(input("Ingrese el porcenta de la nota: "))




def calcularNotaFinal(nota1,porcent1,nota2,porcent2,nota3,porcent3):
    return nota1*porcent1 + nota2*porcent2 + nota3*porcent3

print(f"La nota final es:{calcularNotaFinal(n1,porcentaje1,n2,porcentaje2,n3,porcentaje3)}")

'''
Ejercicio 4
Escribir una función que calcule el área 
de un círculo y otra que calcule el volumen de un
 cilindro usando la primera función.
'''