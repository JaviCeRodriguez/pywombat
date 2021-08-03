'''
Define una función la cual nos permita conocer todas las llaves dentro de un diccionario. La función debe cumplir con los siguientes requerimientos.

La función debe tener por nombre sequences_items.
La función debe recibir como argumento un diccionario.
La función deberá imprimir en consola cada una de la llaves dentro del diccionario.
Ejemplo.

my_dict = {'a': 1, 'b': 2, 'c':3, 'd': 4}
>>> sequences_items(my_dict)
'a'
'b'
'c'
'd'
Ayuda:

El método items sin duda puede serte de mucha útilidad.
'''

def sequences_items(dictionary: dict) -> None:
    for key in list(dictionary):
        print(key)

sequences_items({'California': 'Sacramento', 'Pennsylvania': 'Harrisburg', 'Texas': 'Austin'})