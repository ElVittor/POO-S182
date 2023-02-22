class Personaje:

    #atributos con constructor
    def __init__(self,esp,nom,alt):
        self.especie = esp
        self.nombre = nom
        self.altura = alt

    #Metodos

    def correr(self,estado): #al usar el self le digo que es un metodo no una funcion, agregamos una coma para el parametro a usar
        if(estado):
            print("El Personaje "+self.nombre+" está corriendo")
        else:
            print("El personaje "+self.nombre+" se detuvo.")
            
    def lanzargranadas(self):
        print("Granada lanzada por "+self.nombre+" youre dead")
        
    def recargararma(self,municion):
        cargador = 10
        cargador=cargador + municion
        print("Rifle de asalto de "+self.nombre+" ha sido recargado y tiene "+str(cargador)+" municiones")
 