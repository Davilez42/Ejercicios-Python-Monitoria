def suma(num1,num2):
    return num1+num2

def multiplicacion(num1,num2):
    return num1*num2

def resta(num1,num2):
    return num1-num2


def division(num1,num2):
    return num1/num2


def menu():
    n1 =  int(input("Ingrese el numero1"))
    n2 =  int(input("Ingrese el numero1"))
    print("Escoga la operacion")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")
    opcion =  int(input("Ingrese la opcion: "))

    if opcion ==1:
        print("El resultado de la suma es: " ,suma(n1,n2))
    elif opcion ==2:
        print("El resultado de la Resta es: " ,resta(n1,n2))
    elif opcion ==3:
        print("El resultado de la Multiplicacion es: " ,multiplicacion(n1,n2))    
    elif opcion ==4:
        print("El resultado de la Divison es: " ,division(n1,n2))
    else:
        print("opcion invalidad")


menu()







