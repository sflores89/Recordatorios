from tkinter import *

mainApp = Tk()

#Tamaño de la ventana
mainApp.geometry("900x500")
mainApp.title("Login")

#Imprimir variable de texto en base a una cadena de datos en BD
i = 1
while i < 6:
    Label(mainApp, text=i).pack(anchor=NW)
    i += 1

mainApp.mainloop()
