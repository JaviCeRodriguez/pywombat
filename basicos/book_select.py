'''
Seleccionar Libros

Dado el siguiente listado de libros

libros = [
    'Don Quijote de la Mancha',
    'Historia de dos ciudades',
    'El Señor de los Anillos',
    'El principito',
    'El hobbit',
    'Sueño en el pabellón rojo',
    'Las aventuras de Alicia en el país de las maravillas',
    'Triple representatividad,',
    'Y no quedó ninguno (Diez negritos)',
    'El león, la bruja y el armario'
]
Desarrolla un programa el cual cumpla con los siguiente requerimientos.

El programa listará en consola todos los elementos de la lista.
El usuario podrá seleccionar (mediante un número) un libro en especifico.
En caso el usuario ingrese un número mayor a la cantidad de libros en el listado, el programa deberá mostrar en consola el siguiente mensaje:
Indice no disponible
Ejemplo.

1º- Don Quijote de la Mancha
2º- Historia de dos ciudades
3º- El Señor de los Anillos
4º- El principito
5º- El hobbit
6º- Sueño en el pabellón rojo
7º- Las aventuras de Alicia en el país de las maravillas
8º- Triple representatividad,
9º- Y no quedó ninguno (Diez negritos)
10º- El león, la bruja y el armario

Selecciona un libro: 10
El león, la bruja y el armario
Ayuda: En Python más vale pedir perdón que pedir permiso.

Deseado:

Sería estupendo que la enumeración que el usuario visualizará en consola comenzará desde 1 y no desde 0.
Si tienes tiempo y así lo deseas, sería un muy buena idea validar que el usuario solo pueda introducir números.
'''

libros = [
    'Don Quijote de la Mancha',
    'Historia de dos ciudades',
    'El Señor de los Anillos',
    'El principito',
    'El hobbit',
    'Sueño en el pabellón rojo',
    'Las aventuras de Alicia en el país de las maravillas',
    'Triple representatividad,',
    'Y no quedó ninguno (Diez negritos)',
    'El león, la bruja y el armario'
]

for i, libro in enumerate(libros):
    print(f"{i + 1}° - {libro}")

try:
    sel = int(input("\nSelecciona un libro: "))
    print (libros[sel - 1])
except:
    print("Entrada inválida! Elige un número de la lista!")