from modelo.grapher import grapher
from tkinter import messagebox as MsgBox
import numpy as np
import math
    
class ctrlGrapher(grapher):
    
    def __init__(self):
        super().__init__()
    
    def mostrarMensaje(self, __):
        if self.menu.get() == "Libre":
            self.graphValues["x"] = list(range(10))
            self.graphValues["y"] = np.random.randint(1,10,10).tolist()
        if self.menu.get() == "Seno":
            self.graphValues["x"] = list(range(10))
            self.graphValues["y"] = np.sin(list(range(10)))
        if self.menu.get() == "Coseno":
            self.graphValues["x"] = list(range(10))
            self.graphValues["y"] = np.cos(list(range(10)))
        MsgBox.showinfo("Perfecto...!", "Gráfica seleccionada.: " + self.menu.get())
    
    # def printImage(self):
    
    # def generateGraph(self):
    #     print(self.graphValues)
    #     print(self.graphValues['x'])