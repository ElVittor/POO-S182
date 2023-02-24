class Personaje:

    #atributos con constructor, agregamos __ despues del self. para encapsular 
    def __init__(self,esp,nom,alt):
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt

    #Metodos

    def correr(self,estado): #al usar el self le digo que es un metodo no una funcion, agregamos una coma para el parametro a usar
        if(estado):
            print("El Personaje "+self.__nombre+" está corriendo")
        else:
            print("El personaje "+self.__nombre+" se detuvo.")
            
    def lanzargranadas(self):
        print("Granada lanzada por "+self.__nombre+" youre dead")
        
    def recargararma(self,municion):
        cargador = 10
        cargador=cargador + municion
        print("Rifle de asalto de "+self.__nombre+" ha sido recargado y tiene "+str(cargador)+" municiones")
 
    def __pensar(self):
        print("Esperame tantito toy agarrando señal")
        
 #Generamos GETTER´S & SETTER´S
 
    def getEspecie(self):
        return self.__especie
    
    def setEspecie(self,esp):
        self.__especie=esp
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nom):
        self.__nombre=nom
    
    def getAltura(self):
        return self.__altura
    
    def setAltura(self,alt):
        self.__altura=alt