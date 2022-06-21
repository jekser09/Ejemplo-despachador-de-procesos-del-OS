from Proceso import *
import time
import random
import threading
class Principal():
    
    def __init__(self):
        
        self.__listaProc=[]
        self.__rechazados=[]
        self.__detener=threading.Event()
        self.__detener.set()
        self.__bandera=True
        self.__hilo1=threading.Thread(target=self.crearProceso,args=(self.__detener,))
        self.__hilo2=threading.Thread(target=self.culminar)
        self.__hilo3=threading.Thread(target=self.ejecutarProcesos,args=(self.__detener,))
        self.__hilo1.start()    
        self.__hilo2.start()
        self.__hilo3.start()

    def culminar(self):        
        time.sleep(60)        
        self.__detener.clear()
        self.__bandera=False
        self.final()
        
    def crearProceso(self,detener):
        cont=0
        print("Creando Procesos...")       
        while detener.is_set():                                       
            proceso=Proceso()
            proceso.setNombre("Proceso "+str(cont+1))
            proceso.setTamano(random.randrange(1024,1048576))
            proceso.setTiempoEjecucion(random.randrange(15,45,1))
            proceso.setPid(cont+1)            
            if len(self.__listaProc)<10:
                proceso.setEstado("Espera")
                self.__listaProc.append(proceso)
            else:
                proceso.setEstado("Rechazado")
                self.__rechazados.append(proceso)            
            cont=cont+1            
            time.sleep(random.randrange(1,7,1))        
      
    def ejecutarProcesos(self,detener):
        cont=0
        while self.__bandera==True:                           
            print(self.__listaProc[cont].getNombre()+" ejecutandose...")
            self.__listaProc[cont].setEstado("Ejecutando")
            if not detener.is_set():
                break
            time.sleep(self.__listaProc[cont].getTiempoEjecucion())
            self.__listaProc[cont].setEstado("Terminado")
            cont=cont+1
    
    def final(self):
        print("\nLista procesos --- "+str(len(self.__listaProc)))
        for i in range(len(self.__listaProc)):
            print(self.__listaProc[i].getNombre()+" "+self.__listaProc[i].getEstado())
        
        if self.__rechazados:
            print("\nLista procesos rechazados --- "+str(+len(self.__rechazados)))
            for i in range(len(self.__rechazados)):
                print(self.__rechazados[i].getNombre()+" "+self.__rechazados[i].getEstado()) 
        else:
            print("La lista esta vacia")
        
Principal()