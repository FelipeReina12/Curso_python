from tkinter import *

window = Tk()  # Se usa para crear la ventana principal

def kg_to_grams():
    miles = round(float(e1_value.get()) * 1000, 2)
    t1.delete(1.0, END)  # Limpiar el contenido anterior
    t1.insert(END, miles)

def kg_to_pound():
    pounds = round(float(e1_value.get()) * 2.20462, 2)
    t2.delete(1.0, END)  # Limpiar el contenido anterior
    t2.insert(END, pounds)

def kg_to_ounces():
    ounces = round(float(e1_value.get()) * 35.274, 2)  # Corregido el paréntesis
    t3.delete(1.0, END)  # Limpiar el contenido anterior
    t3.insert(END, ounces)

def convert():
    kg_to_grams()
    kg_to_pound()
    kg_to_ounces()

"""
BOTON DE CONVERTIR
"""
b1 = Button(window, text="Convert", command=convert)
b1.grid(row=0, column=3)

"""
VARIABLE
"""
e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=2)

"""
TEXTO DE SALIDA
"""
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=1)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=2)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=3)

l1 = Label(window, text="Kg")
l1.grid(row=0, column=1)

window.mainloop()  # Se usa para que la ventana se muestre en pantalla siempre hasta que se cierre