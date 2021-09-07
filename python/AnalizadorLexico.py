from tkinter.constants import INSIDE
from Token import Token
from Error import Error
from prettytable import PrettyTable

class AnalizadorLexico:
    
    def __init__(self):
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

    def estado0(self,caracter):
        '''Estado 0'''
        #Elementos del token Color
        token_color = list(range(1,10))
        for a in range(65,71):
            token_color.append(chr(a))
        
        #Comparacion de caracteres
        #Estas transiciones siguen en el estado 0
        if caracter == ';':
            self.agregar_token(caracter,'puntoycoma',self.linea,self.columna)
            self.buffer = ''
            self.columna+=1
        elif caracter == '"':
            self.agregar_token(caracter,'comilla',self.linea,self.columna)
            self.buffer = ''
            self.columna+=1
        elif caracter == '{':
            self.agregar_token(caracter,'llave_izquierda',self.linea,self.columna)
            self.buffer = ''
            self.columna+=1

        elif caracter == '}':
            self.agregar_token(caracter,'llave_derecha',self.linea,self.columna)
            self.buffer = ''
            self.columna+=1

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

        elif caracter == ';':
            self.agregar_token(caracter,'coma',self.linea,self.columna)
            self.buffer = ','
            self.columna+=1

        #Transicion para estado 1
        elif caracter.isdigit():
            self.buffer += caracter
            self.columna+=1
            self.estado = 1

        #Transicion estado 3, token color
        elif caracter == '#':
            self.buffer += caracter
            self.columna+=1
            self.estado=3

 

        #Transicion para estado 2
        elif caracter.isalpha():
            self.buffer += caracter
            self.columna+=1
            self.estado = 2            
        #Comparacion de espacios en blanco y otros caracteres
        elif caracter == '\n':
            self.linea += 1
            self.columna = 1
        elif caracter in ['\t',' ']:
            self.columna += 1      
        elif caracter == '\r':
            pass
        elif caracter == '#':
            print('Se aceptó la cadena!')
            pass

        #Zona de errores
        else:
            self.buffer += caracter
            self.agregar_error(self.buffer,self.linea,self.columna)
            self.buffer = ''
            self.columna += 1            


    def estado1(self,caracter):
        if caracter.isdigit():
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregar_token(self.buffer,'entero',self.linea,self.columna)
            self.estado = 0
            self.columna+=1
            self.i -= 1

    def estado2(self,caracter):
        if caracter.isalpha():
            self.buffer+=caracter
            self.columna+=1
        else:
            self.agregar_token(self.buffer,'palabra',self.linea,self.columna)            
            self.estado = 0
            self.columna+=1
            self.i -= 1



    def analizar(self, cadena):
        '''Analiza léxicamente una cadena'''
        #inicializar listas nuevamente
        self.listaTokens = []
        self.listaErrores = []


        #recorrer caracter por caracter
        self.i = 0
        while self.i < len(cadena):
            if self.estado == 0:
                self.estado0(cadena[self.i])
            elif self.estado == 1:
                self.estado1(cadena[self.i])
            elif self.estado == 2:
                self.estado2(cadena[self.i])
            self.i += 1
                    

    def impTokens(self):
        x = PrettyTable()
        x.field_names = ["Lexema", "Token", "Fila", "Columna"]
        for i in self.listaTokens:
            x.add_row(i.enviarData())
        print(x)

    def impErrores(self):
        x = PrettyTable()
        x.field_names = ["Descripcion", "Fila", "Columna"]
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                x.add_row(i.enviarData())
            print(x)