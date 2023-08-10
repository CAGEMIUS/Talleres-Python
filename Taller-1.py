# Taller 1 Python Entrada y salida de datos
# Autor: Juan Camilo Jiménez Galindo
# Fecha: 9/08/2023

from datetime import date

hoy = date.today()  #fecha actual

print("Hoy es el dia: ", hoy)

n1=int(input("Digite el primer número: "))
n2=int(input("Digite el segundo número: "))

print("La suma de los números es: ", n1+n2)
print("La resta de los números es: ", n1-n2)
print("La multiplicación de los números es: ", n1*n2)
print("La división de los números es: ", n1/n2)
print("FIN")