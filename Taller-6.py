# Taller 6 Python Ciclo WHILE
# Autor: Juan Camilo Jiménez Galindo
# Fecha: 21/08/2023

from datetime import date 
hoy=date.today()          #Fecha actual
print("Hoy es el dia: ", hoy)
print()
print("Taller 6 Python: Ciclos iterativos con la sentencia WHILE")
print()
num1=int(input("Digita un número: "))
print("***   Ciclo controlado por contador   ***")
i = 1
while i <= num1:
    print(i)
    i += 1
print("Fin del ciclo")

print()
print("***   Ciclo controlado por evento   ***")
print("***   Hay un número escodido, encuetra el número   ***")
i = 1 
numero1=5
numero2= int(input("Digita un número de 1 a 10: "))
while numero2 != numero1:
    i += 1
    numero2 = int(input("Digita un número de 1 a 10: "))
print("Acertaste el número en el intento", i ,"FELICIDADES :) ")
print("Fin del ciclo")

print()
print("***   Ciclo abortado con la sentencia break   ***")
amistad = input("Digita el nombre de una amigo suyo: ")
amistad=amistad.upper()
for character in amistad:
    print(character)
    if character=="A":
        break
print("Fin del ciclo")
print()
print("FIN")