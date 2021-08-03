'''
Dadas dos listas de números enteros con longitud x y y ( y > x), respectivamente, desarrolla un programa el cual nos permita conocer si los elementos de la lista longitud x se encuentran dentro de la lista con longitud y.

x = [1, 2, 3, 4, 5, 6, 7, 8] 
y = [10, 25, 52, 80, 1, 46, 6, 33, 14, 27, 19]
El programa debe cumplir con los siguiente requerimientos.

Debe existir una función llamada _sub_list.
La función debe poseer los parámetros _list_x_ y _list_y_.
La función debe retornar una nueva lista con todos aquellos elementos que se encuentren tanto en _list_x_ como en _list_y_.
En caso no existan elementos que coincidan, la función debe retornar una lista vacía.
Ejemplo.

>>> sub_list( [1, 2, 3, 4, 5],  [0, 2, 4, 6, 8, 10] )
[2, 4]

>>> sub_list( [6, 7, 1, 2, 1, 3, 4, 5], [7, 8, 1, 3, 2, 1, 7, 3,7, 10] )
[7, 1, 2, 1, 3]
Deseado: Si es posible, sería una muy buena idea validar la longitud de ambas listas. En caso la longitud del parámetro _list_x sea mayor a _list_y_, retornar una lista vacía.
'''

def sub_list(x: list, y: list) -> list:
    if len(x) > len(y):
        return []
    
    result = [e for e in x if e in y]

    return result

print(sub_list( x=[1, 2, 3, 4, 5], y=[0, 2, 4, 6, 8, 10] ))
print(sub_list( x=[6, 7, 1, 2, 1, 3, 4, 5], y=[7, 8, 1, 3, 2, 1, 7, 3,7, 10] ))
print(sub_list( x=[6, 7, 1, 2, 1, 3, 4, 5], y=[7, 8, 1] ))