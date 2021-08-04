'''
Crear Archivo .Json

A partir del siguiente listado de usuarios. Desarrolla un programa el cual nos permita crear un archivo .json.

El programa debe cumplir con los siguiente requerimientos.

El programa debe ser capaz de generar el archivo users.json.
El archivo debe poseer los 200 usuarios del listado en un formato json.
Cada objeto json debe encontrarse identado por 4 espacios.
Ejemplo.

[
    {
        "age": "73",
        "country": "United States",
        "email": "jerome.thomas@example.com",
        "gender": "male",
        "id": "0",
        "name": "Mr Jerome Thomas"
    },
    {
        "age": "70",
        "country": "United Kingdom",
        "email": "gary.berry@example.com",
        "gender": "male",
        "id": "1",
        "name": "Mr Gary Berry"
    },
...
]
Ayuda:

Muy probablemente necesites hacer uso del módulo json.
'''


import json

def read_file(file_name: str) -> list:

    with open(file_name, 'r', encoding='utf-8') as f:
        users = f.readlines()
    
    user_list = [user.strip('\n').split(',') for user in users]

    return user_list


def users_list_to_json(users: list) -> list:
    def user_dict(user: list) -> dict:
        return {
                "age": user[0],
                "country": user[1],
                "email": user[2],
                "gender": user[3],
                "id": user[4],
                "name": user[5]
            }

    users_list = [user_dict(user) for user in users]
    
    users_json = json.dumps(users_list, indent=4, ensure_ascii=False)
    
    return users_json


def write_json_file(users_json: list, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(users_json)


if __name__ == '__main__':
    users_list = read_file('intermedios/recursos/lista_usuarios.txt')
    users_json = users_list_to_json(users_list)
    write_json_file(users_json, 'intermedios/recursos/lista_usuarios.json')