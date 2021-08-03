'''
Para este ejercicio será necesario crees un script el cual sea capaz de ordernar, de forma descendente, tres números positivos. El script debe cumplir las siguientes reglas.

El usuarios debe ser capaz de introducir (vía teclado) tres números de su conveniencia.
El Script debe pedir, uno a uno, los números del usuario.
El Script debe mostrar en consola, mediante un mensaje, los tres números ordenados de forma descendente.
El mensaje será: El orden es: n1 - n2 - n3
Ejemplo.

Introduce tu primer número: 
10

Introduce tu segundo número: 
5

Introduce tu tercer número: 
60

El orden es: 60 - 10 - 5
Ayuda: Recuerda que la función input retorna un string, aun hay que convertirlo a un número entero.

Pista: Para este ejemplo no te preocupes de excepciones. Confía en que el usuarios siempre ingresará números positivos.
'''

numbers = []
n_input = ["primer", "segundo", "tercer"]

for i in range(0, 3):
    n = int(input(f"Introduce tu {n_input[i]} número: "))
    numbers.append(n)

numbers.sort(reverse=True)

print(f"El orden es: {numbers[0]} - {numbers[1]} - {numbers[2]}")