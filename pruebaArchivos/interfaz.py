import tkinter as t

ventana  = t.Tk()
ventana.geometry("500x400")
ventana.config(bg="#E220F7")

etiqueta1 = t.Label(ventana,text="Hola mudno",font="arial",fg="white")
etiqueta1.config(bg="#A8FF24")
etiqueta1.pack()

etiqueta2 = t.Label(ventana,text="Hola amigos",font="arial")
etiqueta2.config(bg="#A8FF24")
etiqueta2.pack()


def saludar(nombre):
   etiqueta3.config(text=f"Hola {nombre}")


boton1 = t.Button(ventana,text="pulsame",command= lambda:saludar(caja_texto.get()))
boton1.config(background= "#0A2FE8")
boton1.pack()

caja_texto = t.Entry(ventana)
caja_texto.pack()

etiqueta3 = t.Label(ventana,font="arial")
etiqueta3.config(bg="#A8FF24")
etiqueta3.pack()


ventana.mainloop()





