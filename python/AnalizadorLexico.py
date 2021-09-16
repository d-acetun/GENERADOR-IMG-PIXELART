from tkinter.constants import INSIDE
from Token import Token
from Error import Error
from prettytable import PrettyTable
token_color=[]
contador_color=0

for a in range(48,58):
    token_color.append(chr(a))
for a in range(65,71):
    token_color.append(chr(a))

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
        self.buffer=''

    def estado0(self,caracter):
        '''Estado 0'''
        #Elementos del token Color

        
        #Comparacion de caracteres
        #Estas transiciones siguen en el estado 0
        if caracter == ';':
            self.agregar_token(caracter,'puntoycoma',self.linea,self.columna)
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
            print('si entra')
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
        if caracter.isdigit():
            print('estad 1')
            self.buffer+=caracter
            self.columna+=1
        else:
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
        global contador_color
        
        

        if caracter in token_color:
            self.buffer += caracter
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
                
        if caracter =='E':
            self.buffer += caracter
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