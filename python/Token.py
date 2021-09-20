class Token:
    '''Clase token'''
    def __init__(self, lexema, tipo, linea, columna):
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
    
    def imprimirData(self):
        print(self.lexema, self.tipo, self.linea, self.columna)

    def enviarData(self):
        return [self.lexema, self.tipo, self.linea, self.columna]

    def enviarLexema(self):
        return self.lexema
    def enviarTipo(self):
        return self.tipo

    def enviarLinea(self):
        return self.linea

    def enviarColumna(self):
        return self.columna       