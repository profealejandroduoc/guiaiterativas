'''
Crear un programa que lea un Número 5 dígitos e indique cuantos ceros lo componen. El número
no puede comenzar por cero.
'''
from os import system
system("cls")

ceros=0

while True:
    num=int(input("Ingrese un número:"))
    if num>=10000 and num<=99999:
        break
    else:
        print("El número debe ser de 5 dígitos")
        input("presione una tecla para continuar...")
        system("cls")
    
for i in range(4):
    dig=num%10
    if dig==0:
        ceros+=1
    num=num//10

print(f"Cantidad de ceros: {ceros}")        



    