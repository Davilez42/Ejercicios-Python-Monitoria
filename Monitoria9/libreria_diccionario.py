diccionario_ingles_español = {
    "dog": "perro",
    "house": "casa",
    "car": "carro",
    "friend": "amigue",
    "family": "familia",
    "chicken": "pollo"
}
#crea una funcion que recibe una palabra en ingles y devuelve la
#traduccion al español

def traducir(palabra):
    for clave in diccionario_ingles_español:
        if clave == palabra:
            return diccionario_ingles_español[clave]


##agregar una funcion a la libreria la cual recibe
#una palabra en ingles y su significado y la agrega al 
#diccionario 


def insertar_palabra(palabra_ing,significado):
    keys = diccionario_ingles_español.keys()
    if palabra_ing in keys:
        return "error:la palabra ya existe"
    else:
        diccionario_ingles_español[palabra_ing] = significado  
        return "palabra agregada exitosamente"  



    
  
