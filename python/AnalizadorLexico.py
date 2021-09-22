from tkinter import Variable
from tkinter.constants import INSIDE, NO
from Token import Token
from Error import Error
from prettytable import PrettyTable
from Funciones import *
from tkinter import messagebox as MessageBox
token_color=[]
contador_color=0
btitulo = False
bancho = False
balto = False
bceldas = False
cel=0; col=0; boo=False; color=0 #cel representa filas
ContadorCol=0

for a in range(48,58):
    token_color.append(chr(a))
for a in range(65,71):
    token_color.append(chr(a))

class AnalizadorLexico:
    NImg=1
    IndiceCadena=0
    CambiarImg=False
    MultipleImg=False
    vancho=0
    valto=0
    vfilas=0
    vcolumnas=0
    Filtros=[]
    Celdas=[]
    Contador=0; titulo =''
    def __init__(self):
        AnalizadorLexico.vancho=0
        AnalizadorLexico.valto=0
        AnalizadorLexico.vfilas=0
        AnalizadorLexico.vcolumnas=0
        AnalizadorLexico.Filtros=[]
        AnalizadorLexico.Celdas=[]
        AnalizadorLexico.Contador=0; AnalizadorLexico.titulo =''
        self.listaTokens = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 1
        self.buffer = ''
        self.estado = 0
        self.i = 0

    
    def agregar_token(self,caracter,token,linea,columna):
        self.listaTokens.append(Token(caracter,token,linea,columna))
        self.buffer = ''


    def agregar_error(self,caracter,linea,columna):
        self.listaErrores.append(Error('Caracter ' + caracter + ' no reconocido en el lenguaje.', linea, columna))
        self.buffer=''

    def estado0(self,caracter):
        global bceldas, color, boo, col, cel
        global btitulo
        '''Estado 0'''
        #Elementos del token Color

        
        #Comparacion de caracteres
        #Estas transiciones siguen en el estado 0
        if caracter == ';':
            self.agregar_token(caracter,'puntoycoma',self.linea,self.columna)
            self.buffer = ''
            self.columna+=1
        
        elif caracter == '{':
           
            bceldas=True
            self.agregar_token(caracter,'llave_izquierda',self.linea,self.columna)
            self.buffer = ''
            self.columna+=1


        elif caracter == ',':
            self.agregar_token(caracter,'coma',self.linea,self.columna)
            self.buffer = ''
            self.columna+=1


        elif caracter == '}':
            self.agregar_token(caracter,'llave_derecha',self.linea,self.columna)
            self.buffer = ''
            self.columna+=1
            bceldas=False

        elif caracter == '=':
            self.agregar_token(caracter,'igual',self.linea,self.columna)
            self.buffer = ''
            self.columna+=1

        elif caracter == '[':
            self.agregar_token(caracter,'corchete_izquierdo',self.linea,self.columna)
            self.buffer = ''
            self.columna+=1

        elif caracter == ']':
            self.agregar_token(caracter,'corchete_derecho',self.linea,self.columna)
            self.buffer = ''
            self.columna+=1
            AnalizadorLexico.Celdas.append([cel, col, boo, color])

        elif caracter == ';':
            self.agregar_token(caracter,'coma',self.linea,self.columna)
            self.buffer = ','
            self.columna+=1

        #Transicion para estado 1
        elif caracter.isdigit():
            self.buffer += caracter
            self.columna+=1
            self.estado = 1

        #Transicion estado 3,
        elif caracter == '#':
            self.buffer += caracter
            self.columna+=1
            self.estado=3

         #Transicion estado 10,
        elif caracter == 'M':
            self.buffer += caracter
            self.columna+=1
            self.estado=10

        #Transicion estado 18,
        elif caracter == 'D':
            self.buffer += caracter
            self.columna+=1
            self.estado=18

        #Transicion estado 30,
        elif caracter == '@':
            self.buffer += caracter
            self.columna+=1
            self.estado=30 
        #Transicion estado 72, 
        elif caracter == 'T':
            btitulo=True
            self.buffer += caracter
            self.columna+=1
            self.estado=72

        #Transicion estado 40, 
        elif caracter == 'A':
            self.buffer += caracter
            self.columna+=1
            self.estado=40

        #Transicion estado 48, 
        elif caracter == 'F':
            self.buffer += caracter
            self.columna+=1
            self.estado=48   

        #Transicion estado 57, 
        elif caracter == 'C':
            self.buffer += caracter
            self.columna+=1
            self.estado=57   
        
        elif caracter == '"':
            self.buffer+=caracter
            self.columna+=1
            self.estado=70

 

                   
        #Comparacion de espacios en blanco y otros caracteres
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1      
        elif caracter == '\r':
            pass


        #Zona de errores
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1            


    def estado1(self,caracter):
        global bceldas
        global col, cel, ContadorCol
        if caracter.isdigit():
            self.buffer+=caracter
            self.columna+=1
        else:
            if bceldas == True and ContadorCol==0:
               cel=self.buffer
               ContadorCol+=1
            elif bceldas == True and ContadorCol==1:
                col = self.buffer
                ContadorCol=0

            if AnalizadorLexico.Contador==0:
                AnalizadorLexico.vancho=self.buffer
                AnalizadorLexico.Contador+=1
                
                                
            elif AnalizadorLexico.Contador==1:
                AnalizadorLexico.valto=self.buffer
                AnalizadorLexico.Contador+=1

            elif AnalizadorLexico.Contador==2:
                AnalizadorLexico.vfilas=self.buffer
                AnalizadorLexico.Contador+=1

            elif AnalizadorLexico.Contador==3:
                AnalizadorLexico.vcolumnas=self.buffer
                AnalizadorLexico.Contador+=1

            self.agregar_token(self.buffer,'entero',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado3(self,caracter):
        global token_color
        global contador_color
        
        

        if caracter in token_color:
            self.buffer += caracter
            self.columna+=1
            self.estado=4
                
        #Esto se gaurda como error
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado4(self,caracter):
        global token_color
        global contador_color
        
        

        if caracter in token_color:
            self.buffer += caracter
            self.columna+=1
            self.estado=5
                
        
        #Esto se gaurda como error
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado5(self,caracter):
        global token_color
        global contador_color
        
        

        if caracter in token_color:
            self.buffer += caracter
            self.columna+=1
            self.estado=6
                
        
        #Esto se gaurda como error
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado6(self,caracter):
        global token_color
        global contador_color
        
        

        if caracter in token_color:
            self.buffer += caracter
            self.columna+=1
            self.estado=7
                
        
        #Esto se gaurda como error
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado7(self,caracter):
        global token_color
        global contador_color
        
        

        if caracter in token_color:
            self.buffer += caracter
            self.columna+=1
            self.estado=8
                
        
        #Esto se gaurda como error
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado8(self,caracter):
        global token_color
        global contador_color, color, bceldas
        
        

        if caracter in token_color:
            self.buffer += caracter
            # if AnalizadorLexico.CambiarImg==True:
            #     print(self.buffer)

            if bceldas==True:
                color = self.buffer
            self.agregar_token(self.buffer,'color',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            
            
            

            
            
                
        
        #Esto se gaurda como error
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado10(self,caracter):
                
        if caracter =='I':
            self.buffer += caracter
            self.estado = 11
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado11(self,caracter):
                
        if caracter =='R':
            self.buffer += caracter
            self.estado = 12
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado12(self,caracter):
                
        if caracter =='R':
            self.buffer += caracter
            self.estado = 13
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado13(self,caracter):
                
        if caracter =='O':
            self.buffer += caracter
            self.estado = 14
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado14(self,caracter):
                
        if caracter =='R':
            self.buffer += caracter
            self.estado = 15
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado15(self,caracter):
                
        if caracter =='X':
            self.buffer += caracter
            self.agregar_token(self.buffer,'MIRRORX',self.linea,self.columna)
            self.estado = 0
            self.columna+=1

        elif caracter =='Y':
            self.buffer += caracter
            self.agregar_token(self.buffer,'MIRRORY',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado18(self,caracter):
                
        if caracter =='O':
            self.buffer += caracter
            self.estado = 19
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado19(self,caracter):
                
        if caracter =='U':
            self.buffer += caracter
            self.estado = 20
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado20(self,caracter):
                
        if caracter =='B':
            self.buffer += caracter
            self.estado = 21
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado21(self,caracter):
                
        if caracter =='L':
            self.buffer += caracter
            self.estado = 22
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado22(self,caracter):
                
        if caracter =='E':
            self.buffer += caracter
            self.estado = 23
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado23(self,caracter):
                
        if caracter =='M':
            self.buffer += caracter
            self.estado = 24
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado24(self,caracter):
                
        if caracter =='I':
            self.buffer += caracter
            self.estado = 25
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado25(self,caracter):
                
        if caracter =='R':
            self.buffer += caracter
            self.estado = 26
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado26(self,caracter):
                
        if caracter =='R':
            self.buffer += caracter
            self.estado = 27
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado27(self,caracter):
                
        if caracter =='O':
            self.buffer += caracter
            self.estado = 28
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado28(self,caracter):
                
        if caracter =='R':
            self.buffer += caracter
            self.agregar_token(self.buffer,'DOUBLEMIRROR',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado30(self,caracter):
                
        if caracter =='@':
            self.buffer += caracter
            self.estado = 31
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado31(self,caracter):
                
        if caracter =='@':
            self.buffer += caracter
            self.estado = 32
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado32(self,caracter):
                
        if caracter =='@':
            self.buffer += caracter
            self.agregar_token(self.buffer,'Separador de imagenes',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            AnalizadorLexico.NImg+=1
            AnalizadorLexico.MultipleImg=True
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado72(self,caracter):
                
        if caracter =='R':
            self.buffer += caracter
            self.estado = 34
            self.columna+=1

        elif caracter == 'I':
            self.buffer+=caracter
            self.estado=73
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
        
    def estado34(self,caracter):
                
        if caracter =='U':
            self.buffer += caracter
            self.estado = 35
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado35(self,caracter):
        global bceldas, boo          
        if caracter =='E':
            self.buffer += caracter
            if bceldas==True:
                boo = self.buffer
            self.agregar_token(self.buffer,'BOLEANO',self.linea,self.columna)
            self.estado = 0
            self.columna+=1

            
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado73(self,caracter):
                
        if caracter =='T':
            self.buffer += caracter
            self.estado = 74
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado74(self,caracter):
                
        if caracter =='U':
            self.buffer += caracter
            self.estado = 75
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=75
   
    def estado75(self,caracter):
                
        if caracter =='L':
            self.buffer += caracter
            self.estado = 76
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
   
    def estado76(self,caracter):
                
        if caracter =='O':
            self.buffer += caracter
            self.agregar_token(self.buffer,'TITULO',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
   
    def estado70(self,caracter):
                
        if caracter =='"':
            self.buffer += caracter
            AnalizadorLexico.titulo=self.buffer
            self.agregar_token(self.buffer,'TITULO IMAGEN',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            
        else:
            self.buffer += caracter
            self.columna+=1
    
    def estado40(self,caracter):
                
        if caracter =='N':
            self.buffer += caracter
            self.estado = 41
            self.columna+=1

        elif caracter=='L':
            self.buffer+= caracter
            self.estado=45
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    

    def estado41(self,caracter):
                
        if caracter =='C':
            self.buffer += caracter
            self.estado = 42
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado42(self,caracter):
                
        if caracter =='H':
            self.buffer += caracter
            self.estado = 43
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado43(self,caracter):
        global bancho        
        if caracter =='O':
            self.buffer += caracter
            self.agregar_token(self.buffer,'PALABRA RESERVADA',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            bancho=True
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado45(self,caracter):
                
        if caracter =='T':
            self.buffer += caracter
            self.estado = 46
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado46(self,caracter):
                
        if caracter =='O':
            self.buffer += caracter
            self.agregar_token(self.buffer,'PALABRA RESERVADA',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado48(self,caracter):
                
        if caracter =='I':
            self.buffer += caracter
            self.estado = 49
            self.columna+=1
        elif caracter =='A':
            self.buffer += caracter
            self.estado = 78
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado49(self,caracter):
                
        if caracter =='L':
            self.buffer += caracter
            self.estado = 50
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado50(self,caracter):
                
        if caracter =='A':
            self.buffer += caracter
            self.estado = 51
            self.columna+=1

        elif caracter =='T':
            self.buffer += caracter
            self.estado = 53
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado51(self,caracter):
                
        if caracter =='S':
            self.buffer += caracter
            self.agregar_token(self.buffer,'PALABRA RESERVADA',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado53(self,caracter):
                
        if caracter =='R':
            self.buffer += caracter
            self.estado = 54
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0


    def estado54(self,caracter):
                
        if caracter =='O':
            self.buffer += caracter
            self.estado = 55
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado55(self,caracter):
                
        if caracter =='S':
            self.buffer += caracter
            self.agregar_token(self.buffer,'PALABRA RESRVADA',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0


    def estado78(self,caracter):
                
        if caracter =='L':
            self.buffer += caracter
            self.estado = 79
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado79(self,caracter):
                
        if caracter =='S':
            self.buffer += caracter
            self.estado = 80
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    

    def estado80(self,caracter):
        global bceldas, boo        
        if caracter =='E':
            self.buffer += caracter
            if bceldas==True:
                boo = self.buffer
            self.agregar_token(self.buffer,'PALABRA RESRVADA',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0
    
    def estado57(self,caracter):
                
        if caracter =='O':
            self.buffer += caracter
            self.estado = 58
            self.columna+=1

        elif caracter =='E':
            self.buffer += caracter
            self.estado = 65
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado58(self,caracter):
                
        if caracter =='L':
            self.buffer += caracter
            self.estado = 59
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado59(self,caracter):
                
        if caracter =='U':
            self.buffer += caracter
            self.estado = 60
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado60(self,caracter):
                
        if caracter =='M':
            self.buffer += caracter
            self.estado = 61
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado61(self,caracter):
                
        if caracter =='N':
            self.buffer += caracter
            self.estado = 62
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado62(self,caracter):
                
        if caracter =='A':
            self.buffer += caracter
            self.estado = 63
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado63(self,caracter):
                
        if caracter =='S':
            self.buffer += caracter
            self.agregar_token(self.buffer,'PALABRA RESRVADA',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado65(self,caracter):
                
        if caracter =='L':
            self.buffer += caracter
            self.estado = 66
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado66(self,caracter):
                
        if caracter =='D':
            self.buffer += caracter
            self.estado = 67
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado67(self,caracter):
                
        if caracter =='A':
            self.buffer += caracter
            self.estado = 68
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def estado68(self,caracter):
                
        if caracter =='S':
            self.buffer += caracter
            self.agregar_token(self.buffer,'PALABRA RESRVADA',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1
            self.estado=0

    def analizar(self, cadena):
        
        '''Analiza léxicamente una cadena'''
        #inicializar listas nuevamente
        self.listaTokens = []
        self.listaErrores = []


        #recorrer caracter por caracter
        self.i = AnalizadorLexico.IndiceCadena
        

        if AnalizadorLexico.CambiarImg==False:    
            while self.i < len(cadena):
                AnalizadorLexico.MultipleImg=False
                if self.estado == 0:
                    self.estado0(cadena[self.i])
                elif self.estado == 1:
                    self.estado1(cadena[self.i])
                elif self.estado == 3:
                    self.estado3(cadena[self.i])
                elif self.estado == 4:
                    self.estado4(cadena[self.i])
                elif self.estado == 5:
                    self.estado5(cadena[self.i])   
                elif self.estado == 6:
                    self.estado6(cadena[self.i]) 
                elif self.estado == 7:
                    self.estado7(cadena[self.i])
                elif self.estado == 8:
                    self.estado8(cadena[self.i])
                elif self.estado == 10:
                    self.estado10(cadena[self.i])
                elif self.estado == 11:
                    self.estado11(cadena[self.i])
                elif self.estado == 12:
                    self.estado12(cadena[self.i])
                elif self.estado == 13:
                    self.estado13(cadena[self.i])
                elif self.estado == 14:
                    self.estado14(cadena[self.i])
                elif self.estado == 15:
                    self.estado15(cadena[self.i])
                elif self.estado == 18:
                        self.estado18(cadena[self.i])
                elif self.estado == 19:
                    self.estado19(cadena[self.i])
                elif self.estado == 20:
                    self.estado20(cadena[self.i])
                elif self.estado == 21:
                    self.estado21(cadena[self.i])
                elif self.estado == 22:
                    self.estado22(cadena[self.i])
                elif self.estado == 23:
                    self.estado23(cadena[self.i])
                elif self.estado == 24:
                        self.estado24(cadena[self.i])
                elif self.estado == 25:
                    self.estado25(cadena[self.i])
                elif self.estado == 26:
                    self.estado26(cadena[self.i])
                elif self.estado == 27:
                    self.estado27(cadena[self.i])
                elif self.estado == 28:
                    self.estado28(cadena[self.i])
                elif self.estado == 30:
                    self.estado30(cadena[self.i])
                elif self.estado == 31:
                    self.estado31(cadena[self.i])
                elif self.estado == 32:
                    self.estado32(cadena[self.i])
                    if AnalizadorLexico.MultipleImg==True:
                        self.i+=1
                        print('aqui si')
                        # AnalizadorLexico.NImg=self.i
                        AnalizadorLexico.IndiceCadena=self.i
                        AnalizadorLexico.CambiarImg=True
                        break    
                elif self.estado == 72:
                    self.estado72(cadena[self.i])
                elif self.estado == 34:
                    self.estado34(cadena[self.i])
                elif self.estado == 35:
                    self.estado35(cadena[self.i])     
                elif self.estado == 73:
                    self.estado73(cadena[self.i])
                elif self.estado == 74:
                    self.estado74(cadena[self.i])
                elif self.estado == 75:
                    self.estado75(cadena[self.i])     
                elif self.estado == 76:
                    self.estado76(cadena[self.i])
                elif self.estado == 70:
                    self.estado70(cadena[self.i])
                elif self.estado == 40:
                    self.estado40(cadena[self.i])
                elif self.estado == 41:
                    self.estado41(cadena[self.i])  
                elif self.estado == 42:
                    self.estado42(cadena[self.i])
                elif self.estado == 43:
                    self.estado43(cadena[self.i])
                elif self.estado == 45:
                    self.estado45(cadena[self.i])
                elif self.estado == 46:
                    self.estado46(cadena[self.i])
                elif self.estado == 48:
                    self.estado48(cadena[self.i])
                elif self.estado == 49:
                    self.estado49(cadena[self.i])
                elif self.estado == 50:
                    self.estado50(cadena[self.i])
                elif self.estado == 51:
                    self.estado51(cadena[self.i])
                elif self.estado == 53:
                    self.estado53(cadena[self.i])
                elif self.estado == 54:
                    self.estado54(cadena[self.i])
                elif self.estado == 55:
                    self.estado55(cadena[self.i])
                elif self.estado == 78:
                    self.estado78(cadena[self.i])
                elif self.estado == 79:
                    self.estado79(cadena[self.i])
                elif self.estado == 80:
                    self.estado80(cadena[self.i])
                elif self.estado == 57:
                    self.estado57(cadena[self.i])
                elif self.estado == 58:
                    self.estado58(cadena[self.i])
                elif self.estado == 59:
                    self.estado59(cadena[self.i])
                elif self.estado == 60:
                    self.estado60(cadena[self.i])
                elif self.estado == 61:
                    self.estado61(cadena[self.i])
                elif self.estado == 62:
                    self.estado62(cadena[self.i])
                elif self.estado == 63:
                    self.estado63(cadena[self.i])
                elif self.estado == 65:
                    self.estado65(cadena[self.i])
                elif self.estado == 66:
                    self.estado66(cadena[self.i])
                elif self.estado == 67:
                    self.estado67(cadena[self.i])
                elif self.estado == 68:
                    self.estado68(cadena[self.i])
                self.i += 1

        if AnalizadorLexico.CambiarImg==True:
            while self.i < len(cadena):
                # print('aqui si entra')
                AnalizadorLexico.MultipleImg=False
                if self.estado == 0:
                    self.estado0(cadena[self.i])
                elif self.estado == 1:
                    self.estado1(cadena[self.i])
                elif self.estado == 3:
                    self.estado3(cadena[self.i])
                elif self.estado == 4:
                    self.estado4(cadena[self.i])
                elif self.estado == 5:
                    self.estado5(cadena[self.i])   
                elif self.estado == 6:
                    self.estado6(cadena[self.i]) 
                elif self.estado == 7:
                    self.estado7(cadena[self.i])
                elif self.estado == 8:
                    self.estado8(cadena[self.i])
                elif self.estado == 10:
                    self.estado10(cadena[self.i])
                elif self.estado == 11:
                    self.estado11(cadena[self.i])
                elif self.estado == 12:
                    self.estado12(cadena[self.i])
                elif self.estado == 13:
                    self.estado13(cadena[self.i])
                elif self.estado == 14:
                    self.estado14(cadena[self.i])
                elif self.estado == 15:
                    self.estado15(cadena[self.i])
                elif self.estado == 18:
                        self.estado18(cadena[self.i])
                elif self.estado == 19:
                    self.estado19(cadena[self.i])
                elif self.estado == 20:
                    self.estado20(cadena[self.i])
                elif self.estado == 21:
                    self.estado21(cadena[self.i])
                elif self.estado == 22:
                    self.estado22(cadena[self.i])
                elif self.estado == 23:
                    self.estado23(cadena[self.i])
                elif self.estado == 24:
                        self.estado24(cadena[self.i])
                elif self.estado == 25:
                    self.estado25(cadena[self.i])
                elif self.estado == 26:
                    self.estado26(cadena[self.i])
                elif self.estado == 27:
                    self.estado27(cadena[self.i])
                elif self.estado == 28:
                    self.estado28(cadena[self.i])
                elif self.estado == 30:
                    self.estado30(cadena[self.i])
                elif self.estado == 31:
                    self.estado31(cadena[self.i])
                elif self.estado == 32:
                    self.estado32(cadena[self.i])
                    if AnalizadorLexico.MultipleImg==True:
                        self.i+=1
                        AnalizadorLexico.NImg=self.i
                        break    
                elif self.estado == 72:
                    self.estado72(cadena[self.i])
                elif self.estado == 34:
                    self.estado34(cadena[self.i])
                elif self.estado == 35:
                    self.estado35(cadena[self.i])     
                elif self.estado == 73:
                    self.estado73(cadena[self.i])
                elif self.estado == 74:
                    self.estado74(cadena[self.i])
                elif self.estado == 75:
                    self.estado75(cadena[self.i])     
                elif self.estado == 76:
                    self.estado76(cadena[self.i])
                elif self.estado == 70:
                    self.estado70(cadena[self.i])
                elif self.estado == 40:
                    self.estado40(cadena[self.i])
                elif self.estado == 41:
                    self.estado41(cadena[self.i])  
                elif self.estado == 42:
                    self.estado42(cadena[self.i])
                elif self.estado == 43:
                    self.estado43(cadena[self.i])
                elif self.estado == 45:
                    self.estado45(cadena[self.i])
                elif self.estado == 46:
                    self.estado46(cadena[self.i])
                elif self.estado == 48:
                    self.estado48(cadena[self.i])
                elif self.estado == 49:
                    self.estado49(cadena[self.i])
                elif self.estado == 50:
                    self.estado50(cadena[self.i])
                elif self.estado == 51:
                    self.estado51(cadena[self.i])
                elif self.estado == 53:
                    self.estado53(cadena[self.i])
                elif self.estado == 54:
                    self.estado54(cadena[self.i])
                elif self.estado == 55:
                    self.estado55(cadena[self.i])
                elif self.estado == 78:
                    self.estado78(cadena[self.i])
                elif self.estado == 79:
                    self.estado79(cadena[self.i])
                elif self.estado == 80:
                    self.estado80(cadena[self.i])
                elif self.estado == 57:
                    self.estado57(cadena[self.i])
                elif self.estado == 58:
                    self.estado58(cadena[self.i])
                elif self.estado == 59:
                    self.estado59(cadena[self.i])
                elif self.estado == 60:
                    self.estado60(cadena[self.i])
                elif self.estado == 61:
                    self.estado61(cadena[self.i])
                elif self.estado == 62:
                    self.estado62(cadena[self.i])
                elif self.estado == 63:
                    self.estado63(cadena[self.i])
                elif self.estado == 65:
                    self.estado65(cadena[self.i])
                elif self.estado == 66:
                    self.estado66(cadena[self.i])
                elif self.estado == 67:
                    self.estado67(cadena[self.i])
                elif self.estado == 68:
                    self.estado68(cadena[self.i])
                self.i += 1              

    def impTokens(self):
        
        
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        for i in self.listaTokens:
            print(i.enviar())
            x.add_row(i.enviarData())
        # print(x)

    def impErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "Fila", "Columna"]
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                x.add_row(i.enviarData())
                
            print(x)

    def RTokens(self):
        try:
            Nombre=AnalizadorLexico.titulo.replace('"','')
            Nombre='Tokens'+Nombre+'.html'
            reporte = open(Nombre, 'w')
            reporte.write('<html>')
            reporte.write('     <head>')
            reporte.write('<style type="text/css">')
            reporte.write('table, th, td {')

            reporte.write('border: 1px solid black;')
            reporte.write('border-collapse: collapse;;')
            reporte.write('}')
            reporte.write('</style>')

            reporte.write('<title>''TOKENS''</title>')
            reporte.write('<body>')
            reporte.write('<h1 style="text-align: center;">' 'REPORTE DE TOKENS '+AnalizadorLexico.titulo+ '</h1>')

            reporte.write('<table style="margin: 0 auto; width:50%">')
            reporte.write('<tr>')
            reporte.write('<th>' 'LEXEMA' '</th>')
            reporte.write('<th>' 'TOKEN' '</th>')
            reporte.write('<th>' 'FILA' '</th>')
            reporte.write('<th>' 'COLUMNA' '</th>')
            reporte.write('</tr>')

            for i in self.listaTokens:
                reporte.write('<tr>')

                reporte.write('<td>' +i.enviarLexema()+ '</td>')
                reporte.write('<td>' +i.enviarTipo()+ '</td>')
                reporte.write('<td>' +str(i.enviarLinea())+ '</td>')
                reporte.write('<td>' +str(i.enviarColumna())+ '</td>')


                reporte.write('</tr>')

            reporte.write('</table>')

            reporte.write('</head>')
            reporte.write('</body>')
            reporte.write('</html>')
            MessageBox.showinfo('REPORTE TOKENS', 'REPORTE TOKENS GENERADO')
        except:
            MessageBox.showinfo('REPORTE TOKENS', 'ERROR AL GENERAR EL REPORTE DE TOKENS')

    
    def Rerrores(self):
        try:
            Nombre=AnalizadorLexico.titulo.replace('"','')
            Nombre='Errores'+Nombre+'.html'
            reporte = open(Nombre, 'w')
            reporte.write('<html>')
            reporte.write('     <head>')
            reporte.write('<style type="text/css">')
            reporte.write('table, th, td {')

            reporte.write('border: 1px solid black;')
            reporte.write('border-collapse: collapse;;')
            reporte.write('}')
            reporte.write('</style>')

            reporte.write('<title>''TOKENS''</title>')
            reporte.write('<body>')
            reporte.write('<h1 style="text-align: center;">' 'REPORTE DE TOKENS '+AnalizadorLexico.titulo+ '</h1>')

            reporte.write('<table style="margin: 0 auto; width:50%">')
            reporte.write('<tr>')
            reporte.write('<th>' 'DESCRIPCION' '</th>')
            reporte.write('<th>' 'FILA' '</th>')
            reporte.write('<th>' 'COLUMNA' '</th>')
            reporte.write('</tr>')

            for i in self.listaErrores:
                reporte.write('<tr>')

                reporte.write('<td>' +i.enviarData()[0]+ '</td>')
                reporte.write('<td>' +str(i.enviarData()[1])+ '</td>')
                reporte.write('<td>' +str(i.enviarData()[2])+ '</td>')
               


                reporte.write('</tr>')

            reporte.write('</table>')

            reporte.write('</head>')
            reporte.write('</body>')
            reporte.write('</html>')
            MessageBox.showinfo('REPORTE TOKENS', 'REPORTE DE ERRORES GENERADO')
        except:
            MessageBox.showinfo('REPORTE TOKENS', 'ERROR AL GENERAR REPORTE ERRORES')
        