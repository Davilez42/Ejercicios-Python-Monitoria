
import numpy as np


def calcularDefinitiva(parcial, tarea1, tarea2, parFinal, participacion):
    return parcial*0.2 + tarea1*0.2 + tarea2*0.2 + parFinal*0.4 + participacion*0.2


def clasificacion(nombre, asignatura, pacial, taea1, taea2, paFinal, paticipacion):
    nota_definitiva = calcularDefinitiva(
        pacial, taea1, taea2, paFinal, paticipacion)
    clasificacion = ""
    print(nota_definitiva)
    if (asignatura == "Fundamentos" or asignatura == "Calculo"):
        if nota_definitiva >= 0.0 and nota_definitiva < 2.0:
            clasificacion = "Malo"
        elif nota_definitiva >= 2.0 and nota_definitiva < 3.0:
            clasificacion = "Deficiente"
        elif nota_definitiva >= 3.0 and nota_definitiva < 3.8 and asignatura == "Fundamentos":
            clasificacion = "Regular"
        elif nota_definitiva >= 3.0 and nota_definitiva < 3.5 and asignatura == "Calculo":
            clasificacion = "Regular"
        elif nota_definitiva >= 3.8 and nota_definitiva < 4.5 and asignatura == "Fundamentos":
            clasificacion = "Bueno"
        elif nota_definitiva >= 3.5 and nota_definitiva < 4.5 and asignatura == "Calculo":
            clasificacion = "Bueno"
        elif nota_definitiva >= 4.5 and nota_definitiva <= 5.0:
            clasificacion = "Excelente"
    if (asignatura == "Deporte" or asignatura == "InglesI"):
        if nota_definitiva >= 0.0 and nota_definitiva < 3.0 and asignatura == "InglesI":
            clasificacion = "Deficiente"
        if nota_definitiva >= 0.0 and nota_definitiva < 3.0 and asignatura == "Deporte":
            clasificacion = "Malo"
        if nota_definitiva >= 3.0 and nota_definitiva < 4.0:
            clasificacion = "Regular"
        if nota_definitiva >= 4.0 and nota_definitiva < 4.5 and asignatura == "InglesI":
            clasificacion = "Bueno"
        if nota_definitiva >= 4.5 and nota_definitiva <= 5 and asignatura == "InglesI":
            clasificacion = "Excelente"
        if nota_definitiva >= 4.0 and nota_definitiva <= 5 and asignatura == "Deporte":
            clasificacion = "Bueno"
    print(f'''Nombre del alumno: {nombre}\n 
              Nombre de la asignatura: {asignatura}\n
              Clasificacion: {clasificacion}
            ''' )

clasificacion("David","Fundamentos",4.1,3.0,4.2,4.6,3.6)
