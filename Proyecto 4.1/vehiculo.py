class Vehiculo:
    color = "Verde"
    ruedas = 4
    puertas = 5

#Clase Coche, hija de la clase Vehiculo
class Coche(Vehiculo):
    velocidad = 100
    cilindrada = 4

coche1 = Coche() #Instanciación de la clase Coche.
print (dir(coche1))
print("Color:", coche1.color)
print("Ruedas:", coche1.ruedas)
print("Puertas:", coche1.puertas)
print("Velocidad:", coche1.velocidad)
print("Cilindrada:", coche1.cilindrada)