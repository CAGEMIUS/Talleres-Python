# Taller 4 Python Condicionales anidadas
# Autor: Juan Camilo Jiménez Galindo
# Fecha: 17/08/2023

from datetime import date 
hoy=date.today()          #Fecha actual
print("Hoy es el dia: ", hoy)
print()
print("Programa de identificación de tipos de clases de triangulos")
a=int(input("Digite el primer valor de triangulo: "))
b=int(input("Digite el segundo valor de triangulo: "))
c=int(input("Digite el tercer valor de triangulo: "))
print()
if a==b and a==c and b==c:
    print("Es triangulo es equilatero :)")
else:
    if a==b or b==c or a==c:
        print("El triangulo es de tipo isoceles")
    else:
        print("El triangulo es de tipo escaleno")
print()
animal=input("Digite un animal: ")
animal=animal.upper()
if animal=="Perro":
    print("Este animal es el mejor amigo del hombre:", animal)
elif animal=="Gato":
    print("Este animal es muy independiente: ", animal)
elif animal=="Oso":
    print("Este animal vive en el bosque: ", animal)
else:
    print("No es Perro, no es Gato, ni es Oso... es: ", animal)
print()
print("Fin :)")