# Taller 5 Python Ciclo FOR
# Autor: Juan Camilo Jiménez Galindo
# Fecha: 21/08/2023

from datetime import date 
hoy=date.today()          #Fecha actual
print("Hoy es el dia: ", hoy)
print()
print("Taller 5 Python: Ciclos iterativos con la sentencia FOR")
print()
num1=int(input("Digite un primer número: "))
num2=int(input("Digite un segundo número (MAYOR) al primero: "))
print("Ciclo para el primer  número")
for i in range(num1):
    print(i+1)
print("Fin del ciclo")

print()
print("Ciclo desde el primer número hasta el segundo  número")
for i in range(num1,num2):
    print(i+1)
print("Fin del ciclo")

print()
print(print("Ciclo desde el primer número hasta el segundo  número con un incremento de 2"))
for i in range(num1,num2, 2):
    print(i)
print("Fin del ciclo")

print()
empresa=input("Didigte el nombre de una empresa: ")
empresa= empresa.lower()
for caracter in empresa:
    print(caracter)
print("Fin del ciclo")

print()
print("FIN")