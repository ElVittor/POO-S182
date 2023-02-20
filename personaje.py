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