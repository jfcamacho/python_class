
from tkinter import *
from tkinter import messagebox as Messagebox
root = Tk()
from controlador.suma_class import suma
val_suma = suma()

class basic_frm():

    root.config(bg='steelblue')
    root.geometry('600x400')
    val_suma.center_window(root)
    
    label1 = Label(root, text="Valor A.:   ", bg="steelblue", fg="White", font="Verdana, 15")
    label1.grid(row=0,column=0, padx=50, pady=10)
    label2 = Label(root, text="Valor B.:   ", bg="steelblue", fg="White", font="Verdana, 15")
    label2.grid(row=1,column=0, padx=50, pady=10)
    label3 = Label(root, text="Respuesta.: ", bg="steelblue", fg="White", font="Verdana, 15")
    label3.grid(row=2,column=0, padx=50, pady=10)
    
    entry1 = Entry(root, justify=LEFT, borderwidth=2, textvariable=val_suma.valorA)
    entry1.grid(row=0,column=1, padx=10)
    entry2 = Entry(root, justify=LEFT, borderwidth=2, textvariable=val_suma.valorB)
    entry2.grid(row=1,column=1, padx=10)
    entry3 = Entry(root, justify=LEFT, borderwidth=2, textvariable=val_suma.respuesta)
    entry3.grid(row=2,column=1, padx=10)
    
    button1 = Button(root, text="Ejecutar", font="Verdana, 15", command=val_suma.operar)
    button1.config(bg="steelblue")
    button1.grid(row=3, column=1, padx=10, pady=50)
    
    
    options = ["Suma", "Resta", "Multiplicación", "División"]
    val_suma.operacion.set("Seleccione una opción")
    
    def advertencia(self):
        Messagebox.showinfo("Operación seleccionada...!", "Ha seleccionada la "+ val_suma.operacion.get())
    
    btk = OptionMenu(root, val_suma.operacion, *options, command=advertencia)
    btk.config(width=15, bg="steelblue")
    btk.grid(row=3, column=0, padx=50)
    
    
    def start():
        print('System started')
        root.mainloop()