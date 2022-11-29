import tkinter as t
from random import randint
ventana =  t.Tk()
ventana.configure(bg="#A665E6")
ventana.geometry("500x500")
ventana.title("Mi primera ventana")
#ventana.iconwindow("R.png")
etiqueta_resultado = t.Label(ventana)
etiqueta_resultado.pack()



def generarContraseña():
    resultado = ""
    letras = ["1","2","3","a","b","c","d","e","?","!","¡"]
    for i in range(10):
        resultado += letras[randint(0,len(letras)-1)]
    etiqueta_resultado.configure(text=resultado)


def saludar(nombre):
    print("hola "+ nombre)  

etiqueta1 =  t.Label(ventana,text="Hola Mundo")
etiqueta1.pack()

etiqueta2 =  t.Label(ventana,text="dasda",foreground="#A4EF24")
etiqueta2.place(relx=0.7,rely=0.9,relheight=0.1,relwidth=0.1)

boton1 = t.Button(ventana,text="oprimeme",background="#9898F0",command=generarContraseña)
boton1.place(relx=0.1,rely=0.2,relheight=0.2,relwidth=0.2)
boton1 = t.Button(ventana,text="oprimeme",background="#9898F0",command=lambda:saludar(cajatexto.get()))
boton1.pack()

cajatexto = t.Entry(ventana)
cajatexto.configure(background="#9898F0")
cajatexto.pack()

ventana.mainloop()

