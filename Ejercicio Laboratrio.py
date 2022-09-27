
def  calcularDefinitiva(pacial,taea1,taea2,paFinal,paticipacion):
     return pacial*0.2 + (taea1 +taea2)*0.01 + paFinal*0.4 + paticipacion*0.2


def clasificacion(nombre,asignatura,parcial,tarea1,tarea2,parFinal,participacion):
    nota_definitiva =  calcularDefinitiva(parcial,tarea1,tarea2,parFinal,participacion)
    if asignatura == "Fundamentos":
        print("Entra aqui Nota definita es:" , nota_definitiva)
        if nota_definitiva >= 0.0  and nota_definitiva<2.0:
            return "Malo"
        elif nota_definitiva > 2.0  and nota_definitiva<=3.0:
            return "Deficiente"
        elif nota_definitiva > 3.0  and nota_definitiva<=3.8:
            return "Regular" 
        elif nota_definitiva > 4.5  and nota_definitiva<=5.0:
            return "Excelente"


print(clasificacion("Jose","Fundamentos",4.1,4.1,3.3,4.5,3))