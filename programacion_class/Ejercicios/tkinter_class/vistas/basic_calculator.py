
from tkinter import *
from tkinter import messagebox as Messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
root = Tk()
from controlador.suma_class import suma
val_suma = suma()

class basic_frm():

    root.config(bg='steelblue')
    root.geometry('1300x550')
    root.title('Basic Calculator')
    val_suma.center_window(root)
    
    frame1 = Frame(root,borderwidth=2, bg='steelblue',width=500,height=300, relief="sunken")
    frame1.grid(row=0,column=0, padx=50, pady=50)
    
    frame2 = Frame(root,borderwidth=2, bg='steelblue',width=500,height=300, relief="sunken")
    frame2.grid(row=0,column=1, padx=50, pady=50, sticky="nsew")
    
    
    parameters = {"xtick.labelsize": 5, "ytick.labelsize": 5, "axes.titlesize": 5}
    plt.rcParams.update(parameters)
    
    fig, axs = plt.subplots()
    fig.set_figheight(1.5)
    fig.set_figwidth(2.5)
    
    axs.bar([1,2,3,23,24], [4,5,3,16,23])
    axs.grid()
    plt.title("Gráfica de barras")
    
    canvas = FigureCanvasTkAgg(fig, master=frame2)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=0)
    
    label1 = Label(frame1, text="Valor A.:   ", bg="steelblue", fg="White", font="Verdana, 15")
    label1.grid(row=0,column=0, padx=50, pady=10)
    label2 = Label(frame1, text="Valor B.:   ", bg="steelblue", fg="White", font="Verdana, 15")
    label2.grid(row=1,column=0, padx=50, pady=10)
    label3 = Label(frame1, text="Respuesta.: ", bg="steelblue", fg="White", font="Verdana, 15")
    label3.grid(row=2,column=0, padx=50, pady=10)
    
    entry1 = Entry(frame1, justify=LEFT, borderwidth=2, textvariable=val_suma.valorA)
    entry1.grid(row=0,column=1, padx=10)
    entry2 = Entry(frame1, justify=LEFT, borderwidth=2, textvariable=val_suma.valorB)
    entry2.grid(row=1,column=1, padx=10)
    entry3 = Entry(frame1, justify=LEFT, borderwidth=2, textvariable=val_suma.respuesta)
    entry3.grid(row=2,column=1, padx=10)
    
    button1 = Button(frame1, text="Ejecutar", font="Verdana, 15", command=val_suma.operar)
    button1.config(bg="steelblue")
    button1.grid(row=3, column=1, padx=10, pady=50)
    
    
    options = ["Suma", "Resta", "Multiplicación", "División"]
    val_suma.operacion.set("Seleccione una opción")
    
    def advertencia(self):
        Messagebox.showinfo("Operación seleccionada...!", "Ha seleccionada la "+ val_suma.operacion.get())
    
    btk = OptionMenu(frame1, val_suma.operacion, *options)
    btk.config(width=15, bg="steelblue")
    btk.grid(row=3, column=0, padx=50)
    
    
    def start():
        print('System started')
        root.mainloop()