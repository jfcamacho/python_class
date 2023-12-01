from tkinter import *

class grapher():
    root = Tk()
    graphic = StringVar()
    menu = StringVar()
    opciones = [
        "Libre",
        "Seno",
        "Coseno"
    ]
    graphValues = {
        "x": [],
        "y": []
    }
    