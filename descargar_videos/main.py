from tkinter import *
from backend import download_video  # Importa la función desde el backend

def descargar_video():
    link = descarga_text.get()  # Obtiene el enlace del campo de entrada
    download_video(link)  # Llama a la función del backend con el enlace

window = Tk()

window.wm_title("App video")

l1 = Label(window, text="Link del video")
l1.grid(row=0, column=0)

descarga_text = StringVar()
e1 = Entry(window, textvariable=descarga_text, width=50)
e1.grid(row=1, column=0)

b1 = Button(window, text= "Cerrar", width= 12, command= window.destroy)
b1.grid(row=3, column=0)

b2 = Button(window, text="Descargar", width=12, command=descargar_video)
b2.grid(row=1, column=1)

window.mainloop()
