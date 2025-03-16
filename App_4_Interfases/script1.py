from tkinter import *

window = Tk()  #Se usa para crear la ventana principal

b1 = Button(window, text= "Execute")
# b1.pack()  #Es para que el botón se muestre en la ventana
#Otra forma de hacerlo es mediante cuadricula 
b1.grid(row= 0, column= 0)

e1 = Entry(window)
e1.grid(row= 0, column= 1)

t1 = Text(window, height=1, width= 20)
t1.grid(row= 0, column= 2)





window.mainloop()  #Se usa para que la ventana se muestre en pantalla siempre hasta que se cierre