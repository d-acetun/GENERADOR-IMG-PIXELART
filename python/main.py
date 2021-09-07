from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter.font import Font
import easygui
from AnalizadorLexico import *


archivo=''
Ruta=''
def funcion():
    
    lst = list(range(1,10))
    lst.append('#')
    for a in range(65,71):
        lst.append(chr(a))
    print(lst)

    p='T'
    if p in lst:
        print('si')
    
    # raiz.destroy()

def Cargar():
    global Ruta
    Ruta = easygui.fileopenbox() #Esto nos poermite guardar ka ruta del archivo

def Leer():
    global archivo
    global Ruta
    archivo = open(Ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido
    
    

def Analizar():
    global archivo

    scanner = AnalizadorLexico()
    cadena = Leer()
    scanner.analizar(cadena)
    scanner.impTokens()
    scanner.impErrores()
            



                        
                    
                

raiz = tk.Tk()
raiz.title("Bitxelart")
raiz.geometry("1250x750+150+10")

BCargar = tk.Button(raiz, text="Cargar Archivo", command=Cargar, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue") #activebackground para que cambie de color al presionarlo, activeforeground para que cambie de color el texto
BCargar.pack()
BCargar.place(x=10, y=10)

BAnalizar = tk.Button(raiz, text="Analizar", command=Analizar, height=2, width=15, bg="darkgreen", fg="white", activebackground="powderblue")
BAnalizar.pack()
BAnalizar.place(x=122, y=10)

BReportes = tk.Button(raiz, text="Reportes", command=funcion, height=2, width=15, bg="indigo", fg="white", activebackground="powderblue")
BReportes.pack()
BReportes.place(x=232, y=10)

BSalir = tk.Button(raiz, text="Salir", command=funcion, height=2, width=15, bg="orange red", fg="white", activebackground="powderblue")
BSalir.pack()
BSalir.place(x=342, y=10)

BOriginal = tk.Button(raiz, text="Original", command=funcion, height=2, width=15, bg="lightyellow", fg="black", activebackground="powderblue")
BOriginal.pack()
BOriginal.place(x=40, y=200)

BMirrorX = tk.Button(raiz, text="Mirror X", command=funcion, height=2, width=15, bg="violet", fg="white", activebackground="powderblue")
BMirrorX.pack()
BMirrorX.place(x=40, y=270)

BMirrorY = tk.Button(raiz, text="Mirror Y", command=funcion, height=2, width=15, bg="maroon", fg="white", activebackground="powderblue") 
BMirrorY.pack()
BMirrorY.place(x=40, y=340)

BDoubleMirror = tk.Button(raiz, text="Double Mirror", command=funcion, height=2, width=15, bg="crimson", fg="white", activebackground="powderblue")
BDoubleMirror.pack()
BDoubleMirror.place(x=40, y=410)

raiz.mainloop()