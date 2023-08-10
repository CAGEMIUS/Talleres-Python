# Taller 2 Python Intrucciones secuenciales
# Autor: Juan Camilo Jiménez Galindo
# Fecha: 9/08/2023

from datetime import date 
hoy = date.today()           #Fecha actual
print("Hoy es el dia: ", hoy)

a=int(input("Digite el primer número: "))
b=int(input("Digite el seguno número: "))
c=int(input("Digite el tercer número: "))

x = [a, b, c]

print("El valor maximo es: ", max(x))
print("El valor minimo es: ", min(x))
print("La suma de los 3 número es: ", sum(x))
print()

z=float(input("Digite un número con decimales: "))
redondo=round(z)
print("El valor decial es: ", z, "Redondiado: ", redondo)
print()

frase=input("Digite una oración: ")
print("La frase en mayuscula es: ", frase.upper())
print("La frase en minuscula es: ", frase.lower())
print("La frase con mayuscula inicial es: ", frase.capitalize())
print("La frase con palabras en mayusculas es: ", frase.title())
print("La longitud de la frase es: ", len(frase), "caracteres")
print()
print("FIN")