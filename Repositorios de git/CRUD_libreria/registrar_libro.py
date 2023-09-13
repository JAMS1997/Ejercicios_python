# Importamos el archivo que contiene la lista de libros
import libros

# Definimos una función que pide al usuario que ingrese los datos del libro y lo agrega a la lista
def registrar():
  # Pedimos al usuario que ingrese los datos del libro
  print("Ingrese los datos del libro que desea registrar")
  titulo = input("Título: ")
  autor = input("Autor: ")
  genero = input("Género: ")
  año = input("Año: ")
  estado = input("Estado (disponible o prestado): ")

  # Creamos un diccionario con los datos del libro
  libro = {
    "titulo": titulo,
    "autor": autor,
    "genero": genero,
    "año": año,
    "estado": estado
  }

  # Agregamos el diccionario a la lista de libros
  libros.lista.append(libro)

  # Mostramos un mensaje de confirmación
  print("El libro ha sido registrado exitosamente")

  # Volvemos al menú principal
  import menu
  menu.mostrar_menu()
