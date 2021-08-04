'''
Sobre Escritura De Métodos Simple

Dada la siguiente clase

class Animal():

    def comer(self):
        print('El animal come.')

    def dormir(self):
        print('El animal duerme.')
Define dos nuevas clases (Perro, Gato) que hereden de la clase Animal. Las clases hijas debe ser capaces de sobre escribir los métodos de la clase padre (Animal)

La clase Perro deberá imprimir en consola: el Perro Come y el Perro Duerme para los métodos comer y dormir respectivamente.
La clase Gato deberá imprimir en consola: el Gato Come y el Gato Duerme para los métodos comer y dormir respectivamente.
Ejemplo.

>>> gato.comer()
El Gato come.

>>> perro.dormir()
El Perro duerme.
'''

class Animal():
    
    def comer(self):
        print('El animal come.')

    def dormir(self):
        print('El animal duerme.')


class Perro(Animal):

    def comer(self):
        print(f'El {type(self).__name__} Come')

    def dormir(self):
        print(f'El {type(self).__name__} Duerme')


class Gato(Animal):

    def comer(self):
        print(f'El {type(self).__name__} Come')

    def dormir(self):
        print(f'El {type(self).__name__} Duerme')


Perro().comer()
Perro().dormir()
Gato().comer()
Gato().dormir()