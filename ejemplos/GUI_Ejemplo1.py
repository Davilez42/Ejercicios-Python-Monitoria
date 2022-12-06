from matriz import *
import tkinter as t


root =  t.Tk()
root.geometry("200x200")
root.resizable(width=False,height=False)

#ETIQUETAS
label_input_col = t.Label(root,text="Ingrese las columnas:")
label_input_row = t.Label(root,text="Ingrese las filas:")
label_input_val = t.Label(root,text="Ingrese el valor:")
resultado = t.Label(root,text="Frecuencia:")

#CAJATEXTOS
box_input_col = t.Entry(root)
box_input_row = t.Entry(root)
valor = t.Entry(root)

#BOTON
calcular = t.Button(root,text="Calcular",command=lambda:aux1(box_input_col.get(),box_input_row.get(),valor.get()))
#LOGICA BOTON
def aux1(col=0,fila=0,val=0):
    
    frecuencia = crearMatriz(int(fila),int(col),int(val))
    resultado.configure(text=f"Frecuencia:{frecuencia}")
    box_input_col.delete(0,10)
    box_input_row.delete(0,10)
    valor.delete(0,10)

    

    
    
    
#---------------------------------------------POSICIONAMIENTO---------------------------------------------------------
label_input_col.place(relx=0.0,rely=0.1)
box_input_col.place(relx=0.6,rely=0.1,relwidth=0.2)

label_input_row.place(relx=0.0,rely=0.3)
box_input_row.place(relx=0.5,rely=0.3,relwidth=0.2)

label_input_val.place(relx=0.0,rely=0.5)
valor.place(relx=0.5,rely=0.5,relwidth=0.2)


resultado.place(relx=0.0,rely=0.7,relwidth=0.4)
calcular.place(relx=0.6,rely=0.7)





root.mainloop()