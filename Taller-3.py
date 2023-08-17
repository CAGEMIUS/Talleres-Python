# Taller 3 Python Condicionales simples
# Autor: Juan Camilo Jiménez Galindo
# Fecha: 17/08/2023

from datetime import date 
hoy=date.today()          #Fecha actual
print("Hoy es el dia: ", hoy)
a=int(input("Digite el primer valor 1: "))
b=int(input("Digite el segundo valor 2: "))

if a>=b:
    print("El primer valor 1: ", a, " Es mayor o igual al segundo valor 2: ",b)
else:
    print("El primer valor 1: ", a, "Es menor que el segundo valor 2: ",b)
print()
curso1="Requerimientos"
curso2="Algoritmos"
print("El curso 1 es: ", curso1)
print("El curso 2 es: ", curso2)
if curso1 == "Requerimientos" and curso2 == "Algoritmos":
    print("Ustes esta estudiando programación de software")
else:
    print("Usted no esta estudiando programación de software, esta estudiando otro programa de formación.")
print()
print("***   Final del Análisis del programa de formación SENA   ***")
print()
frase=input("Digite una oración: ")
print("La oración ingresada en mayuscula es: ", frase.upper())
longitud=len(frase)
print("La longitud de la oración ingresada es de: ", len(frase), "caracteres")
if longitud>10:
    print("La oración ingresada tiene mas de 10 caracteres")
else:
    print("La frase ingresa tiene menos de 11 caracteres")
print()
print("FIN :)")