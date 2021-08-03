'''
Escribe un programa en Python donde el usuario podrá ingresar una secuencia de números enteros. Los números debe encontrarse separados por una coma (,)

Ejemplo.

Ingresa una secuencia de números: 10, 20, 30, 14, 14, 16, 20
El programa deberá imprimir en consola todos los número ingresados en líneas diferentes.

Ingresa una secuencia de números: 10, 20, 30, 14, 14, 16, 20
10
20
30
14
14
16
20
'''

sequence = input("Ingresa una secuencia de números: ")

numbers = sequence.replace(' ', '').split(',')

for i in numbers:
    print(int(i))