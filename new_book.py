import json   #Lee un archivo JSON y devuelve su contenido.""""


def read_file(file_path):
    """
    Parámetros:
        file_path (str): Ruta del archivo JSON.

    Retorna:
        list: Lista de libros almacenados en el archivo.
    """

    # Abre el archivo en modo lectura utilizando codificación UTF-8
    with open(file_path, 'r', encoding='utf-8') as file:

        # Convierte el contenido del archivo JSON a una lista de Python
        books = json.load(file)

    # Devuelve la lista de libros
    return books


def new_book_data():
    """
    Solicita al usuario la información de un nuevo libro.

    Retorna:
        dict: Diccionario con toda la información del libro.
    """

    # Solicita los datos principales del libro
    tittle = input("Ingrese el titulo del libro nuevo: ")
    author = input("Ingrese el nombre del autor de dicho libro: ")
    while True:
        try:
            publish_date = int(input("Ingrese el año de publicacion del libro: "))
            break
        except ValueError:
                print("Error. Debe ingresar únicamente números.")
    
    genre = input("Ingrese el genero del titulo: ")
    page_amount = int(input("Ingrese la cantidad de paginas que posee tal titulo: "))

    # Convierte la respuesta "si" o "no" en un valor booleano
    availability = input("¿Está el titulo disponible? (si/no): ").lower() == "si"

    # Solicita la editorial
    editorial = input("Ingrese la editorial del titulo: ")

    # Si el usuario no escribe nada, se guarda como None
    if editorial == '':
        editorial = None

    print("Ingrese las palabras claves relacionadas con el libro:")

    # Lista donde se almacenarán las palabras clave
    key_words = []

    # Solicita cinco palabras clave
    for i in range(5):
        word = input(f"Palabra {i+1}: ")
        key_words.append(word)

    # Diccionario con información adicional del libro
    additional = {

        "ISBN": input("ISBN: "),

        "Idioma": input("Idioma: "),

        "Numero de edicion": int(input("Numero de edicion: ")),

        "Calificacion promedio": float(input("Calificacion promedio: ")),

        "Cantidad de prestamos realizados": int(input("Cantidad de prestamos realizados: "))
    }

    # Diccionario principal que contiene toda la información del libro
    new_book = {

        "Titulo": tittle,

        "Autor": author,

        "Fecha de publicacion": publish_date,

        "Genero": genre,

        "Cantidad de paginas": page_amount,

        "Disponibilidad": availability,

        "Editorial": editorial,

        "Palabras clave": key_words,

        "Adicionales": additional
    }

    # Devuelve el diccionario del nuevo libro
    return new_book


def save_files(file_path, books):
    """
    Guarda la lista de libros en un archivo JSON.

    Parámetros:
        file_path (str): Ruta del archivo.
        books (list): Lista de libros que será almacenada.
    """

    # Abre el archivo en modo escritura
    with open(file_path, 'w', encoding='utf-8') as file:

        # Convierte la lista de Python en formato JSON
        # indent=4 mejora la legibilidad del archivo
        json.dump(books, file, indent=4)


def main():
    """
    Función principal del programa.

    Se encarga de:
        1. Leer el archivo JSON.
        2. Solicitar un nuevo libro.
        3. Agregarlo a la lista.
        4. Guardar nuevamente el archivo.
    """

    # Ruta del archivo JSON
    file_path = "books.json"

    # Lee todos los libros existentes
    books = read_file(file_path)

    # Obtiene la información del nuevo libro
    new_book = new_book_data()

    # Agrega el nuevo libro a la lista
    books.append(new_book)

    # Guarda nuevamente el archivo actualizado
    save_files(file_path, books)

    # Mensaje de confirmación
    print("¡Libro agregado correctamente!")


# Ejecuta la función principal del programa
main()