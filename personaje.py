class Personaje:

#atributos

    especie = "Human"
    nombre = "MasterChief"
    altura = 2.7

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
        print("Rifle de asalto de "+self.nombre+" ha sido recargado y tiene "+cargador+" municiones")
 