from tkinter import *

window = Tk()  #Se usa para crear la ventana principal

def km_to_miles():
    miles = round(float(e1_value.get()) * 1.6, 2)
    t1.insert(END, miles)

b1 = Button(window, text= "Execute", command= km_to_miles)
# b1.pack()  #Es para que el botón se muestre en la ventana
#Otra forma de hacerlo es mediante cuadricula 
b1.grid(row= 0, column= 0)

e1_value = StringVar()
e1 = Entry(window, textvariable= e1_value)
e1.grid(row= 0, column= 1)

t1 = Text(window, height=1, width= 20)
t1.grid(row= 0, column= 2)





window.mainloop()  #Se usa para que la ventana se muestre en pantalla siempre hasta que se cierre