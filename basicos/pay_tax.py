'''
Tributar impuesto

En México 🇸🇳 para poder tributar impuestos ser mayor de edad (Tener más de 18 años), es por ello que en esta ocasión es necesario crear un programa en Python que le permita conocer al usuario es debe o no tributar impuestos.

El programa deberá pedir al usuario ingrese, vía teclado su edad.
El programa deberá imprimir en consola los siguientes mensajes con respecto a la edad del usuarios:
Debes tributar impuestos. y Por el momento no es necesario realizar una declaración.
Ejemplos

$ python main.py
Ingrese su edad: 28
Debes tributar impuestos
$ python main.py
Ingrese su edad: 10
Por el momento no es necesario realizar una declaración.
'''

age = int(input("Ingrese su edad: "))
if age > 18:
    print("Debes tributar impuestos")
else:
    print("Por el momento no es necesario realizar una declaración.")