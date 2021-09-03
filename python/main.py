from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter.font import Font
import easygui
def funcion():
    raiz.destroy()

def Cargar():
    NombreArchivo = easygui.fileopenbox()
    archivo = open(NombreArchivo, 'r')
    linea = archivo.readline()
    linea = linea.strip()

    while linea:
        linea = linea.strip()
        if linea != '':
            print(linea)
        linea = archivo.readline() 



                        
                    
                

raiz = tk.Tk()
raiz.title("Bitxelart")
raiz.geometry("1250x750+150+10")

BCargar = tk.Button(raiz, text="Cargar Archivo", command=Cargar, height=2, width=15, bg="midnightblue", fg="white")
BCargar.pack()
BCargar.place(x=10, y=10)

BAnalizar = tk.Button(raiz, text="Analizar", command=funcion, height=2, width=15, bg="darkgreen", fg="white")
BAnalizar.pack()
BAnalizar.place(x=122, y=10)

BReportes = tk.Button(raiz, text="Reportes", command=funcion, height=2, width=15, bg="indigo", fg="white")
BReportes.pack()
BReportes.place(x=232, y=10)

BSalir = tk.Button(raiz, text="Salir", command=funcion, height=2, width=15, bg="orange red", fg="white")
BSalir.pack()
BSalir.place(x=342, y=10)

BOriginal = tk.Button(raiz, text="Original", command=funcion, height=2, width=15, bg="lightyellow", fg="black")
BOriginal.pack()
BOriginal.place(x=40, y=200)

BMirrorX = tk.Button(raiz, text="Mirror X", command=funcion, height=2, width=15, bg="steelblue", fg="white")
BMirrorX.pack()
BMirrorX.place(x=40, y=270)

BMirrorY = tk.Button(raiz, text="Mirror Y", command=funcion, height=2, width=15, bg="maroon", fg="white")
BMirrorY.pack()
BMirrorY.place(x=40, y=340)

BDoubleMirror = tk.Button(raiz, text="Double Mirror", command=funcion, height=2, width=15, bg="crimson", fg="white")
BDoubleMirror.pack()
BDoubleMirror.place(x=40, y=410)

raiz.mainloop()