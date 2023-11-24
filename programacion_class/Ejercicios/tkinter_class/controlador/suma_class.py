from tkinter import StringVar

class suma():
    def __init__(self, operacion = StringVar(),  valorA = StringVar(), valorB = StringVar(), respuesta = StringVar()):
        self.operacion = operacion
        self.valorA = valorA
        self.valorB = valorB
        self.respuesta = respuesta
        
    def sumar(self):
        self.respuesta.set(float(self.valorA.get()) + float(self.valorB.get()))
    
    def restar(self):
        self.respuesta.set(float(self.valorA.get()) - float(self.valorB.get()))
    
    def multiplicar(self):
        self.respuesta.set(float(self.valorA.get()) * float(self.valorB.get()))
    
    def dividir(self):
        self.respuesta.set(float(self.valorA.get()) / float(self.valorB.get()))
    
    def operar(self):
        if self.operacion.get() == "Suma":
            self.sumar()
        if self.operacion.get() == "Resta":
            self.restar()
        if self.operacion.get() == "Multiplicación":
            self.multiplicar()
        if self.operacion.get() == "División":
            self.dividir()
    
    def center_window(self, window):
        """
        Basado en https://stackoverflow.com/a/10018670.
        """
        window.update_idletasks()
        width = window.winfo_width()
        frm_width = window.winfo_rootx() - window.winfo_x()
        win_width = width + 2*frm_width
        height = window.winfo_height()
        titlebar_height = window.winfo_rooty() - window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = window.winfo_screenwidth()//2 - win_width//2
        y = window.winfo_screenheight()//2 - win_height//2
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.deiconify()