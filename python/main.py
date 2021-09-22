from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter.font import Font
import easygui
from AnalizadorLexico import *
from Funciones import *
from tkinter import messagebox as MessageBox
from PIL import ImageTk, Image
from tkinter import ttk
import time
AnchoCelda = 0.0
AltoCelda = 0.0
archivo = ''
Ruta = ''
label = Label
raiz = tk.Tk()
ListaTitulos = []
texto=StringVar
combo = ttk.Combobox()


def MIRRORY():
    global raiz
    global label
    global combo
    global ListaTitulos
    # print(combo.get())
    if combo.get()!='':
        for i in range(len(ListaTitulos)):
            if combo.get()==ListaTitulos[i]:
                ruta=f'C:\\Users\\16-a0001la\\OneDrive\\Desktop\\2do.Semestre2021\\LENGUAJESFORMALES\\Lab\\Proyecto1\\{ListaTitulos[i]}MIRRORY.jpg'
    
    
        imagen = ImageTk.PhotoImage(Image.open(ruta))
        
        label.configure(image=imagen)
        label.image=imagen

    # ventana(f'C:\\Users\\16-a0001la\\OneDrive\\Desktop\\2do.Semestre2021\\LENGUAJESFORMALES\\Lab\\Proyecto1\\PokeballMIRRORY.jpg')


def MIRRORX():
    global raiz
    global label
    global combo
    global ListaTitulos
    print(combo.get())
    try:
        if combo.get()!='':
            for i in range(len(ListaTitulos)):
                if combo.get()==ListaTitulos[i]:
                    ruta=f'C:\\Users\\16-a0001la\\OneDrive\\Desktop\\2do.Semestre2021\\LENGUAJESFORMALES\\Lab\\Proyecto1\\{ListaTitulos[i]}MIRRORX.jpg'
        
        
            imagen = ImageTk.PhotoImage(Image.open(ruta))
            
            label.configure(image=imagen)
            label.image=imagen
    except:
        MessageBox.showinfo('IMAGEN', 'NO SE PUDO CARGAR LA IMAGEN')

def original():
    global raiz
    global label
    global combo
    global ListaTitulos
    print(combo.get())
    try:
        if combo.get()!='':
            for i in range(len(ListaTitulos)):
                if combo.get()==ListaTitulos[i]:
                    ruta=f'C:\\Users\\16-a0001la\\OneDrive\\Desktop\\2do.Semestre2021\\LENGUAJESFORMALES\\Lab\\Proyecto1\\{ListaTitulos[i]}original.jpg'
        
        
            imagen = ImageTk.PhotoImage(Image.open(ruta))
            
            label.configure(image=imagen)
            label.image=imagen
            MessageBox.showinfo('MENSAJE', 'IMAGEN CARGADA CON EXITO')
    except:
        MessageBox.showinfo('MENSAJE', 'OCURRIÓ UN ERROR AL MOSTRAR LA IMAGEN')

def DOUBLEMIRROR():
    global raiz
    global label
    global combo
    global ListaTitulos
    print(combo.get())
    if combo.get()!='':
        for i in range(len(ListaTitulos)):
            if combo.get()==ListaTitulos[i]:
                ruta=f'C:\\Users\\16-a0001la\\OneDrive\\Desktop\\2do.Semestre2021\\LENGUAJESFORMALES\\Lab\\Proyecto1\\{ListaTitulos[i]}DOUBLEMIRROR.jpg'
    
    
        imagen = ImageTk.PhotoImage(Image.open(ruta))
        
        label.configure(image=imagen)
        label.image=imagen
def Cargar():
    global Ruta
    try:
        Ruta = easygui.fileopenbox()  # Esto nos poermite guardar ka ruta del archivo
        MessageBox.showinfo('CARGAR ARCHIVO', 'EL ARCHIVO FUE CARGADO')
    except:
        MessageBox.showinfo('CARGAR ARCHIVO', 'OCURRIO UN ERROR AL CARGAR EL ARCHIVO')

def Leer():
    global archivo
    global Ruta
    archivo = open(Ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido


def Analizar():
    global archivo
    global ListaTitulos
    global combo
    # MessageBox.showinfo("Hola!", "Hola mundo")
    # try:
    scanner = AnalizadorLexico()
    cadena = Leer()
    scanner.analizar(cadena)
    NumeroImagenes=AnalizadorLexico.NImg
    AnalizadorLexico.IndiceCadena=0
    AnalizadorLexico.CambiarImg=False
    AnalizadorLexico.MultipleImg=False
    AnalizadorLexico.Contador=0
    AnalizadorLexico.titulo=''
    AnalizadorLexico.Celdas.clear()

    for i in range(NumeroImagenes):
        print(AnalizadorLexico.NImg+1)
        AnalizadorLexico.Celdas.clear()
        scanner = AnalizadorLexico()
        cadena = Leer()
        scanner.analizar(cadena)
        ListaTitulos.append(AnalizadorLexico.titulo.replace('"',''))
        GenerarHtml()
        combo.configure(values=tuple(ListaTitulos))
    # MessageBox.showinfo('MENSAJE', 'ARCHIVO ANALIZADO CON EXITO')
# except:
    # MessageBox.showinfo('ANALIZAR ARCHIVO', 'ERROR AL ANALIZAR EL ARCHIVO')
# scanner.impTokens()
# scanner.impErrores()
# print(AnalizadorLexico.Celdas)
# print(len(AnalizadorLexico.Celdas))

# scanner.RTokens()
# scanner.Rerrores()

    
    # ventana(f'C:\\Users\\16-a0001la\\OneDrive\\Desktop\\2do.Semestre2021\\LENGUAJESFORMALES\\Lab\\Proyecto1\\blanco.jpg')


def GenerarHtml():
    
    global AnchoCelda, AltoCelda
    # print(int(AnalizadorLexico.vcolumnas))
    AnchoCelda = int(AnalizadorLexico.vancho)/int(AnalizadorLexico.vcolumnas)
    AltoCelda = int(AnalizadorLexico.valto)/int(AnalizadorLexico.vfilas)
    # print(AnchoCelda)
    # print(AltoCelda)
    try:
        titulo = AnalizadorLexico.titulo.replace('"', '')
        img = titulo+'original.jpg'
        titulo = '_'+titulo+' original.html'
        reporte = open(titulo, 'w')
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

        reporte.write('<h1 style="text-align: center;">' +
                    AnalizadorLexico.titulo + '</h1>')

        reporte.write(f'<table style="margin: 0 auto;">')

        # reporte.write(`<table style="margin: 0 auto; width: ">`)

        PosicionFila = 0
        PosicionColumna = 0
        a=0
        for c in range(int(AnalizadorLexico.vfilas)):
            reporte.write('<tr>')
            for c2 in range(int(AnalizadorLexico.vcolumnas)):
                pintado = False
                PosicionCelda = str(PosicionColumna)+str(PosicionFila)

                for c3 in range(len(AnalizadorLexico.Celdas)):
                    Fila = AnalizadorLexico.Celdas[c3][0]
                    Columna = AnalizadorLexico.Celdas[c3][1]
                    Boolean = AnalizadorLexico.Celdas[c3][2]
                    Color = AnalizadorLexico.Celdas[c3][3]
                    if AnalizadorLexico.CambiarImg==True and a==0:
                        print(Fila)
                        
                    Celda = Columna+Fila

                    if Celda == PosicionCelda and Boolean == 'TRUE':

                        reporte.write(
                            f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px" style="background-color: {Color};">'  '</td>')
                        pintado = True
                        break
                a=1
                if pintado == False:
                    reporte.write(
                        f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px">'  '</td>')

                PosicionFila += 1
            reporte.write('</tr>')
            PosicionColumna += 1
            PosicionFila = 0
        reporte.write('</table>')

        reporte.write('</body>')
        reporte.write('</html>')

        titulo = AnalizadorLexico.titulo.replace('"', '')
        img = titulo+'MIRRORX.jpg'
        titulo = '_'+titulo+' MIRRORX.html'
        reporte = open(titulo, 'w')
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
        reporte.write('<h1 style="text-align: center;">' 'MIRROR X' '</h1>')

        reporte.write(f'<table style="margin: 0 auto;">')

        PosicionFila = int(AnalizadorLexico.vfilas)-1
        PosicionColumna = 0
        # print(len(AnalizadorLexico.Celdas))

        for c in range(int(AnalizadorLexico.vfilas)):
            reporte.write('<tr>')
            for c2 in range(int(AnalizadorLexico.vcolumnas)):
                pintado = False
                PosicionCelda = str(PosicionColumna)+str(PosicionFila)

                for c3 in range(len(AnalizadorLexico.Celdas)):
                    Fila = AnalizadorLexico.Celdas[c3][0]
                    Columna = AnalizadorLexico.Celdas[c3][1]
                    Boolean = AnalizadorLexico.Celdas[c3][2]
                    Color = AnalizadorLexico.Celdas[c3][3]
                    Celda = Columna+Fila
                    if Celda == PosicionCelda and Boolean == 'TRUE':

                        reporte.write(
                            f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px" style="background-color: {Color};">'  '</td>')
                        pintado = True
                        break
                if pintado == False:
                    reporte.write(
                        f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px">'  '</td>')

                PosicionFila -= 1
            reporte.write('</tr>')
            PosicionColumna += 1
            PosicionFila = int(AnalizadorLexico.vfilas)-1

        reporte.write('</table>')

        reporte.write('</head>')
        reporte.write('</body>')
        reporte.write('</html>')

        titulo = AnalizadorLexico.titulo.replace('"', '')
        img = titulo+'MIRRORY.jpg'
        titulo = '_'+titulo+' MIRRORY.html'
        reporte = open(titulo, 'w')
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
        reporte.write('<h1 style="text-align: center;">' 'MIRROR Y' '</h1>')

        reporte.write(f'<table style="margin: 0 auto;">')

        PosicionFila = 0
        PosicionColumna = int(AnalizadorLexico.vcolumnas)-1
        # print(len(AnalizadorLexico.Celdas))

        for c in range(int(AnalizadorLexico.vfilas)):
            reporte.write('<tr>')
            for c2 in range(int(AnalizadorLexico.vcolumnas)):
                pintado = False
                PosicionCelda = str(PosicionColumna)+str(PosicionFila)

                for c3 in range(len(AnalizadorLexico.Celdas)):
                    Fila = AnalizadorLexico.Celdas[c3][0]
                    Columna = AnalizadorLexico.Celdas[c3][1]
                    Boolean = AnalizadorLexico.Celdas[c3][2]
                    Color = AnalizadorLexico.Celdas[c3][3]
                    Celda = Columna+Fila
                    if Celda == PosicionCelda and Boolean == 'TRUE':

                        reporte.write(
                            f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px" style="background-color: {Color};">'  '</td>')
                        pintado = True
                        break
                if pintado == False:
                    reporte.write(
                        f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px">'  '</td>')

                PosicionFila += 1
            reporte.write('</tr>')
            PosicionColumna -= 1
            PosicionFila = 0

        reporte.write('</table>')
        reporte.write('</head>')
        reporte.write('</body>')
        reporte.write('</html>')

        titulo = AnalizadorLexico.titulo.replace('"', '')
        img = titulo+'DOUBLEMIRROR.jpg'
        titulo = '_'+titulo+' DOUBLEMIRROR.html'
        reporte = open(titulo, 'w')
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
        reporte.write('<h1 style="text-align: center;">' 'DOUBLE MIRROR' '</h1>')

        reporte.write(f'<table style="margin: 0 auto;">')

        PosicionFila = int(AnalizadorLexico.vfilas)-1
        PosicionColumna = int(AnalizadorLexico.vcolumnas)-1
        # print(len(AnalizadorLexico.Celdas))

        for c in range(int(AnalizadorLexico.vfilas)):
            reporte.write('<tr>')
            for c2 in range(int(AnalizadorLexico.vcolumnas)):
                pintado = False
                PosicionCelda = str(PosicionColumna)+str(PosicionFila)

                for c3 in range(len(AnalizadorLexico.Celdas)):
                    Fila = AnalizadorLexico.Celdas[c3][0]
                    Columna = AnalizadorLexico.Celdas[c3][1]
                    Boolean = AnalizadorLexico.Celdas[c3][2]
                    Color = AnalizadorLexico.Celdas[c3][3]
                    Celda = Columna+Fila
                    if Celda == PosicionCelda and Boolean == 'TRUE':

                        reporte.write(
                            f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px" style="background-color: {Color};">'  '</td>')
                        pintado = True
                        break
                if pintado == False:
                    reporte.write(
                        f'<td id={PosicionCelda} width="{AnchoCelda}px" height="{AltoCelda}px">'  '</td>')

                PosicionFila -= 1
            reporte.write('</tr>')
            PosicionColumna -= 1
            PosicionFila = int(AnalizadorLexico.vfilas)-1

        reporte.write('</table>')

        reporte.write('</head>')
        reporte.write('</body>')
        reporte.write('</html>')
    except:
        MessageBox.showinfo('HTML IMAGENES', 'ERROR AL GENERAR HTML')


def HTML():
    import imgkit
    titulo = AnalizadorLexico.titulo.replace('"', '')
    img = titulo+'original.jpg'
    titulo = '_'+titulo+' original.html'
    opciones = {'width': int(AnalizadorLexico.vancho) +
                150, 'height': int(AnalizadorLexico.valto)+150}
    config = imgkit.config(
        wkhtmltoimage=f'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')
    imgkit.from_file(titulo, img, config=config, options=opciones)

    titulo = AnalizadorLexico.titulo.replace('"', '')
    img = titulo+'MIRRORX.jpg'
    titulo = '_'+titulo+' MIRRORX.html'
    import imgkit
    opciones = {'width': int(AnalizadorLexico.vancho) +
                150, 'height': int(AnalizadorLexico.valto)+150}
    config = imgkit.config(
        wkhtmltoimage=f'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')
    imgkit.from_file(titulo, img, config=config, options=opciones)

    titulo = AnalizadorLexico.titulo.replace('"', '')
    img = titulo+'MIRRORY.jpg'
    titulo = '_'+titulo+' MIRRORY.html'
    import imgkit
    opciones = {'width': int(AnalizadorLexico.vancho) +
                150, 'height': int(AnalizadorLexico.valto)+150}
    config = imgkit.config(
        wkhtmltoimage=f'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')
    imgkit.from_file(titulo, img, config=config, options=opciones)

    titulo = AnalizadorLexico.titulo.replace('"', '')
    img = titulo+'DOUBLEMIRROR.jpg'
    titulo = '_'+titulo+' DOUBLEMIRROR.html'
    import imgkit
    opciones = {'width': int(AnalizadorLexico.vancho) +
                150, 'height': int(AnalizadorLexico.valto)+150}
    config = imgkit.config(
        wkhtmltoimage=f'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltoimage.exe')
    imgkit.from_file(titulo, img, config=config, options=opciones)


def ventana(img):
    global ListaTitulos
    global raiz
    global combo
    global label
    raiz.title("Bitxelart")
    raiz.geometry("1250x750+150+10")
    imagen = ImageTk.PhotoImage(Image.open('C:\\Users\\16-a0001la\\OneDrive\\Desktop\\2do.Semestre2021\\LENGUAJESFORMALES\\Lab\\Proyecto1\\blanco.jpg'))
    label = Label(raiz,image=imagen)
    label.pack()
    label.place(x=500, y=140)

    LabelCbox = Label(text='IMAGENES DISPONIBLES')
    LabelCbox.pack()
    LabelCbox.place(x=40, y=500)
    combo = ttk.Combobox(raiz)
    combo.place(x=40, y=530)
    combo['values'] = tuple(ListaTitulos)
    
    # activebackground para que cambie de color al presionarlo, activeforeground para que cambie de color el texto
    BCargar = tk.Button(raiz, text="Cargar Archivo", command=Cargar, height=2,
                        width=15, bg="midnightblue", fg="white", activebackground="powderblue")
    BCargar.pack()
    BCargar.place(x=10, y=10)

    BAnalizar = tk.Button(raiz, text="Analizar", command=Analizar, height=2,
                          width=15, bg="darkgreen", fg="white", activebackground="powderblue")
    BAnalizar.pack()
    BAnalizar.place(x=122, y=10)

    BReportes = tk.Button(raiz, text="Reportes", command=HTML, height=2,
                          width=15, bg="indigo", fg="white", activebackground="powderblue")
    BReportes.pack()
    BReportes.place(x=232, y=10)

    BSalir = tk.Button(raiz, text="Salir", command=raiz.destroy, height=2,
                       width=15, bg="orange red", fg="white", activebackground="powderblue")
    BSalir.pack()
    BSalir.place(x=342, y=10)

    BOriginal = tk.Button(raiz, text="Original", command=original, height=2,
                          width=15, bg="lightyellow", fg="black", activebackground="powderblue")
    BOriginal.pack()
    BOriginal.place(x=40, y=200)

    BMirrorX = tk.Button(raiz, text="Mirror X", command=MIRRORX, height=2,
                         width=15, bg="violet", fg="white", activebackground="powderblue")
    BMirrorX.pack()
    BMirrorX.place(x=40, y=270)

    BMirrorY = tk.Button(raiz, text="Mirror Y", command=MIRRORY, height=2,
                         width=15, bg="maroon", fg="white", activebackground="powderblue")
    BMirrorY.pack()
    BMirrorY.place(x=40, y=340)

    BDoubleMirror = tk.Button(raiz, text="Double Mirror", command=DOUBLEMIRROR, height=2,
                              width=15, bg="crimson", fg="white", activebackground="powderblue")
    BDoubleMirror.pack()
    BDoubleMirror.place(x=40, y=410)

    raiz.mainloop()


ventana(f'C:\\Users\\16-a0001la\\OneDrive\\Desktop\\2do.Semestre2021\\LENGUAJESFORMALES\\Lab\\Proyecto1\\blanco.jpg')
