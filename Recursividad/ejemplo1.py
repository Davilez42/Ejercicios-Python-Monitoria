

from unittest import result


def factorial(n):
    print(n)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)    
#print(factorial(10))

'''
opcion  = 0
while opcion!=3 and opcion<10:
    
    print("1.-------")
    print("2.-------")
    print("3.Salir")
    
    opcion =  int(input("Ingrese una opcion: "))
    if opcion!=1 and opcion!=2 and opcion!=3:    
        print("Opcion Invalidad")
        break       

'''   
'''  
lsita = [1,2,3,4,5,6,6,7,7,8.10] 

for numero in lsita:
    print(numero)
    if numero == 4:
        print("ENCONTRADO")
        break
        
'''        
   

#n = 5
''' 
n = int(input("Ingrese el numero:"))
def factorial2(n): 
    i=1
    resultado = 1
    while i<=n:  
        resultado = resultado*i    
        i+=1
    return resultado
          
print(factorial2(n))
''' 

for k in range(0,10):
    for i in range(0,10):
        print("*",end=" ")
    print() 
    
    
print("////////////////////////////")       

for i in range(0,10):#parte superior
        print("*",end=" ")   
print()        
        
for i in range(0,8):
    for i in range(0,10) :
        if i ==0 or i==9:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
                          
for i in range(0,10):#parte superior
        print("*",end=" ")   
           