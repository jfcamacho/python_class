# from controlador.ctrlGrapher import ctrlGrapher
from tkinter import *
from controlador.ctrlGrapher import ctrlGrapher
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class frmGrapher(ctrlGrapher):
    
    def __init__(self):
        super().__init__()
        
        
    ################################################################  
    def generatePlotGraph(self, frame2):
        self.generateGraph()
        parameters = {"xtick.labelsize": 5, "ytick.labelsize": 5, "axes.titlesize": 5}
        plt.rcParams.update(parameters)
        fig, axs = plt.subplots(figsize=(2,1.5), dpi=100)
        axs.bar(super().graphValues['x'],super().graphValues['y'], linewidth=0.2)
        data = FigureCanvasTkAgg(fig, master=frame2)
        data.draw()
        data.get_tk_widget().grid(column=0, row=0)
        
    ################################################################  
    def generateFrame(self):
        
        root = super().root
        root.geometry("800x300")
        root.title("Este es mi proyecto completo")
        
        frame1 = Frame(root, bg='coral' )
        frame1.config(width=200, height=200)
        frame1.grid(row=0, column=0, padx=50, pady=50)
        
        frame2 = Frame(root, bg='coral', width=200, height=200)
        frame2.grid(row=0, column=1, padx=50, pady=50)
        
        label1 = Label(frame1, text="Nombre.: ", font="Verdana, 15", bg='coral')
        label1.grid(row=0, column=0, padx=10, pady=10)
        label2 = Label(frame1, text="Mensaje.: ", font="Verdana, 15", bg='coral')
        label2.grid(row=0, column=0, padx=10, pady=10)
        
        entry1 = Entry(frame1, text="Nombre.: ", font="Verdana, 15", textvariable=super().graphic)
        entry1.grid(row=0, column=1, padx=10, pady=10)
        
        super().menu.set("Seleccionar Mensaje")
        
        cmbBox = OptionMenu(frame1, super().menu, *super().opciones, command=super().mostrarMensaje)
        cmbBox.config(width=30, bg='coral')
        cmbBox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        # button1 = Button(frame1, text="Ejecutar", padx=5, pady=5, command=super().mostrarMensaje)
        # button1.grid(row=2, column=0, padx=10, pady=10)
        button2 = Button(frame1, text="Ejecutar", padx=5, pady=5, command=lambda:self.generatePlotGraph(frame2))
        button2.grid(row=2, column=1, padx=10, pady=10)
        
        root.mainloop()
        