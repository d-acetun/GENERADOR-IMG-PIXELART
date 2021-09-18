class Persona:
     
    def __init__(self,ancho,alto,filas,columnas):
        self.ancho = ancho
        self.alto = alto
        self.filas = filas
        self.columnas = columnas

   
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getEdad(self):
        return self.edad

    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setEdad(self, edad):
        self.edad = edad