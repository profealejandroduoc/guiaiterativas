'''
Diseñar un programa que lea N números enteros y determine el promedio de ellos.
'''

from os import system
system("cls")

nums=0
suma=0
while True:
    n=input("Ingrese un número: ")
    if n.isnumeric():
        n=int(n)
        nums+=1
        suma+=n
    else:
        print("Debe ser un valor numérico")
    resp=input("Desea agregar otro número s/n:")
    if resp=="n":
        break
print(f"El promedio es: {suma/nums}")

