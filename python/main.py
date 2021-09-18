from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter.font import Font
import easygui
from AnalizadorLexico import *
from Funciones import *
AnchoCelda=0.0
AltoCelda=0.0
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
    AnalizadorLexico.Celdas.clear()
    scanner.analizar(cadena)
    # scanner.impTokens()
    # scanner.impErrores()
    # print(AnalizadorLexico.Celdas)
    # print(len(AnalizadorLexico.Celdas))
    for c3 in range(len(AnalizadorLexico.Celdas)):
        Fila=AnalizadorLexico.Celdas[c3][0]
        Columna=AnalizadorLexico.Celdas[c3][1]
        Celda = Fila+Columna
        
    

    
def HTML():
    global AnchoCelda, AltoCelda
    # print(int(AnalizadorLexico.vcolumnas))
    AnchoCelda=int(AnalizadorLexico.vancho)/int(AnalizadorLexico.vcolumnas)
    AltoCelda=int(AnalizadorLexico.valto)/int(AnalizadorLexico.vfilas)
    # print(AnchoCelda)
    # print(AltoCelda)


    reporte = open('img.html', 'w')
    reporte.write('<html>')
    reporte.write('     <head>')
    reporte.write('<style type="text/css">')
    reporte.write('table, th, td {')

    reporte.write('border: 1px solid black;')
    reporte.write('border-collapse: collapse;;')
    reporte.write('}')
    reporte.write('</style>')

    reporte.write('<title>''REPORTE''</title>')
    reporte.write('<body>')

    reporte.write('<h1 style="text-align: center;">' 'IMGAGEN 1 ' '</h1>')
    
    reporte.write(f'<table style="margin: 0 auto;">')
    
    # reporte.write(`<table style="margin: 0 auto; width: ">`)
    
    PosicionFila=0
    PosicionColumna=0
    for c in range(int(AnalizadorLexico.vfilas)):
        reporte.write('<tr>')
        for c2 in range(int(AnalizadorLexico.vcolumnas)):
            pintado=False
            PosicionCelda = str(PosicionColumna)+str(PosicionFila)
            
            for c3 in range(len(AnalizadorLexico.Celdas)):
                Fila=AnalizadorLexico.Celdas[c3][0]
                Columna=AnalizadorLexico.Celdas[c3][1]
                Boolean=AnalizadorLexico.Celdas[c3][2]
                Color=AnalizadorLexico.Celdas[c3][3]
                Celda = Columna+Fila
                
                if Celda==PosicionCelda and Boolean=='TRUE':
                    
                
                    reporte.write(f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px" style="background-color: {Color};">'  '</td>')
                    pintado=True
                    break
            if pintado==False:   
                reporte.write(f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px">'  '</td>')

            PosicionFila+=1
        reporte.write('</tr>')
        PosicionColumna+=1
        PosicionFila=0
    reporte.write('</table>')



    reporte.write('<h1 style="text-align: center;">' 'MIRROR X' '</h1>')
    
    reporte.write(f'<table style="margin: 0 auto;">')


    PosicionFila= int(AnalizadorLexico.vfilas)-1
    PosicionColumna=0
    print(len(AnalizadorLexico.Celdas))

    for c in range(int(AnalizadorLexico.vfilas)):
        reporte.write('<tr>')
        for c2 in range(int(AnalizadorLexico.vcolumnas)):
            pintado=False
            PosicionCelda = str(PosicionColumna)+str(PosicionFila)
            
            for c3 in range(len(AnalizadorLexico.Celdas)):
                Fila=AnalizadorLexico.Celdas[c3][0]
                Columna=AnalizadorLexico.Celdas[c3][1]
                Boolean=AnalizadorLexico.Celdas[c3][2]
                Color=AnalizadorLexico.Celdas[c3][3]
                Celda = Columna+Fila
                if Celda==PosicionCelda and Boolean=='TRUE':
                    
                
                    reporte.write(f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px" style="background-color: {Color};">'  '</td>')
                    pintado=True
                    break
            if pintado==False:   
                reporte.write(f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px">'  '</td>')

            PosicionFila-=1
        reporte.write('</tr>')
        PosicionColumna+=1
        PosicionFila=int(AnalizadorLexico.vfilas)-1
    

    reporte.write('</table>')




    reporte.write('<h1 style="text-align: center;">' 'MIRROR Y' '</h1>')
    
    reporte.write(f'<table style="margin: 0 auto;">')

    PosicionFila= 0
    PosicionColumna=int(AnalizadorLexico.vcolumnas)-1
    print(len(AnalizadorLexico.Celdas))

    for c in range(int(AnalizadorLexico.vfilas)):
        reporte.write('<tr>')
        for c2 in range(int(AnalizadorLexico.vcolumnas)):
            pintado=False
            PosicionCelda = str(PosicionColumna)+str(PosicionFila)
            
            for c3 in range(len(AnalizadorLexico.Celdas)):
                Fila=AnalizadorLexico.Celdas[c3][0]
                Columna=AnalizadorLexico.Celdas[c3][1]
                Boolean=AnalizadorLexico.Celdas[c3][2]
                Color=AnalizadorLexico.Celdas[c3][3]
                Celda = Columna+Fila
                if Celda==PosicionCelda and Boolean=='TRUE':
                    
                
                    reporte.write(f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px" style="background-color: {Color};">'  '</td>')
                    pintado=True
                    break
            if pintado==False:   
                reporte.write(f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px">'  '</td>')

            PosicionFila+=1
        reporte.write('</tr>')
        PosicionColumna-=1
        PosicionFila=0
    
    reporte.write('</table>')


    reporte.write('<h1 style="text-align: center;">' 'DOUBLE MIRROR' '</h1>')
    
    reporte.write(f'<table style="margin: 0 auto;">')

    PosicionFila= int(AnalizadorLexico.vfilas)-1
    PosicionColumna=int(AnalizadorLexico.vcolumnas)-1
    print(len(AnalizadorLexico.Celdas))

    for c in range(int(AnalizadorLexico.vfilas)):
        reporte.write('<tr>')
        for c2 in range(int(AnalizadorLexico.vcolumnas)):
            pintado=False
            PosicionCelda = str(PosicionColumna)+str(PosicionFila)
            
            for c3 in range(len(AnalizadorLexico.Celdas)):
                Fila=AnalizadorLexico.Celdas[c3][0]
                Columna=AnalizadorLexico.Celdas[c3][1]
                Boolean=AnalizadorLexico.Celdas[c3][2]
                Color=AnalizadorLexico.Celdas[c3][3]
                Celda = Columna+Fila
                if Celda==PosicionCelda and Boolean=='TRUE':
                    
                
                    reporte.write(f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px" style="background-color: {Color};">'  '</td>')
                    pintado=True
                    break
            if pintado==False:   
                reporte.write(f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px">'  '</td>')

            PosicionFila-=1
        reporte.write('</tr>')
        PosicionColumna-=1
        PosicionFila=int(AnalizadorLexico.vfilas)-1
    

    reporte.write('</table>')

    reporte.write('</head>')
    reporte.write('</body>')
    reporte.write('</html>')


# global valto
# global vfilas, vcolumnas
    

            



                        
                    
                

raiz = tk.Tk()
raiz.title("Bitxelart")
raiz.geometry("1250x750+150+10")

BCargar = tk.Button(raiz, text="Cargar Archivo", command=Cargar, height=2, width=15, bg="midnightblue", fg="white", activebackground="powderblue") #activebackground para que cambie de color al presionarlo, activeforeground para que cambie de color el texto
BCargar.pack()
BCargar.place(x=10, y=10)

BAnalizar = tk.Button(raiz, text="Analizar", command=Analizar, height=2, width=15, bg="darkgreen", fg="white", activebackground="powderblue")
BAnalizar.pack()
BAnalizar.place(x=122, y=10)

BReportes = tk.Button(raiz, text="Reportes", command=HTML, height=2, width=15, bg="indigo", fg="white", activebackground="powderblue")
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