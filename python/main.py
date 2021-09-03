from tkinter import *
import tkinter
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



                        
                    
                

raiz = Tk()
raiz.title("Bitxelart")
raiz.geometry("1250x750+150+10")
BCargar = tkinter.Button(raiz, text="Cargar Archivo", command=Cargar, height=2, width=15)
BCargar.pack()
BCargar.place(x=10, y=10)

BAnalizar = tkinter.Button(raiz, text="Analizar", command=funcion, height=2, width=15)
BAnalizar.pack()
BAnalizar.place(x=122, y=10)

BReportes = tkinter.Button(raiz, text="Reportes", command=funcion, height=2, width=15)
BReportes.pack()
BReportes.place(x=232, y=10)

BSalir = tkinter.Button(raiz, text="Salir", command=funcion, height=2, width=15)
BSalir.pack()
BSalir.place(x=342, y=10)

BOriginal = tkinter.Button(raiz, text="Original", command=funcion, height=2, width=15)
BOriginal.pack()
BOriginal.place(x=40, y=200)

BMirrorX = tkinter.Button(raiz, text="Mirror X", command=funcion, height=2, width=15)
BMirrorX.pack()
BMirrorX.place(x=40, y=270)

BMirrorY = tkinter.Button(raiz, text="Mirror Y", command=funcion, height=2, width=15)
BMirrorY.pack()
BMirrorY.place(x=40, y=340)

BDoubleMirror = tkinter.Button(raiz, text="Double Mirror", command=funcion, height=2, width=15)
BDoubleMirror.pack()
BDoubleMirror.place(x=40, y=410)

raiz.mainloop()