from tkinter import *

root = Tk()


def reset():
    opcion.set(str(None))
    label.config(text='')


def seleccionar():
    label.config(text="{}".format(opcion.get()))


opcion = StringVar()
Radiobutton(root, text="Opción 1", variable=opcion, value=1, command=seleccionar).pack()
Radiobutton(root, text="Opción 2", variable=opcion, value=2, command=seleccionar).pack()
Radiobutton(root, text="Opción 3", variable=opcion, value=3, command=seleccionar).pack()
Button(root, text="Reiniciar", command=reset).pack()

label = Label(root)
label.pack()

root.mainloop()
