from personaje import *

#Solicitar datos
print("")
print("###Solicitud Datos Heroe")
especieH = input("Escriba la especie del Heroe: ")
nombreH = input("Escriba el nombre del Heroe: ")
alturaH = float(input("Escriba la altura del Heroe: "))
recargaH = int(input("Ingrese munición a recargar (Heroe): "))

print("")
print("###Solicitud Datos Heroe")
especieV = input("Escriba la especie del Villano: ")
nombreV = input("Escriba el nombre del Villano: ")
alturaV = float(input("Escriba la altura del Villano: "))
recargaV = int(input("Ingrese munición a recargar (Villano): "))

#Creamos Objetos usando el constructor
Heroe=Personaje(especieH,nombreH,alturaH)
Villano=Personaje(especieV,nombreV,alturaV)

# Usamos los atributos del Heroe y Villano 
print("")
print("###Atributos y metodos del Heroe###")
print("El personaje se llama: "+Heroe.nombre)
print("El personaje pertenenece a la especie : "+Heroe.especie)
print("El personaje tiene una altura de : "+str(Heroe.altura))
Heroe.correr(True)
Heroe.lanzargranadas()
Heroe.recargararma(recargaH)

print("")
print("###Atributos y metodos del Villano###")
print("El personaje se llama: "+Villano.nombre)
print("El personaje pertenenece a la especie : "+Villano.especie)
print("El personaje tiene una altura de : "+str(Villano.altura))
Villano.correr(True)
Villano.lanzargranadas()
Villano.recargararma(recargaV)