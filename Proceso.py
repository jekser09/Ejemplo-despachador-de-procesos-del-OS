class Proceso():
    def __init__(self):
        
        self.__nombre=""
        self.__tamano = 0
        self.__tiempoEjecucion = 0
        self.__estado = ""
        self.__pid=0
        
    # METODOS GET Y SET
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, valor):
        self.__nombre=valor

    def getTamaño(self):
        return self.__tamaño
    
    def setTamano(self, valor):
        self.__tamaño=valor
        
    def getTiempoEjecucion(self):
        return self.__tiempoEjecucion

    def setTiempoEjecucion(self,valor):
        self.__tiempoEjecucion=valor

    def getEstado(self):
        return self.__estado
    
    def setEstado(self,valor):
        self.__estado=valor
    
    def getPid(self):
        return self.__pid
    
    def setPid(self,valor):
        self.__pid=valor