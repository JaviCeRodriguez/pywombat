'''
Colores

Dada la siguiente lista de colores

['Azul', 'Verde', 'Amarillo', 'Rojo', 'Morado', 'Negro', 'Blanco', 'Gris']
Desarrolla un programa que nos permita conocer:

El primer color de la lista.
El penúltimo color de la lista.
El último color de la lista.
Ejemplo.

Primer color: Azul
Penúltimo color: Blanco
Último color: Gris
Ayuda:

Recuerda, en Python, las lista comienzan en el índice 0.
Es posible utilizar números negativos en los índices.
'''

colors = ['Azul', 'Verde', 'Amarillo', 'Rojo', 'Morado', 'Negro', 'Blanco', 'Gris']

print(f'Primer color: {colors[0]}')
print(f'Penúltimo color: {colors[-2]}')
print(f'Último color: {colors[-1]}')