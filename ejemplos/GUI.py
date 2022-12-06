import tkinter as t
from PIL import Image,ImageTk
ventana = t.Tk()
ventana.geometry("500x500")


ventana.title("ventana")
ventana.iconbitmap("z.ico")


imagen = ImageTk.PhotoImage(Image.open("ojo.jpg").resize(size=(200,200)))


etiqueta  = t.Label(ventana,image=imagen)
etiqueta.pack()





ventana.mainloop()



