# Importamos el archivo que contiene la lista de libros
import libros

# Definimos una función que muestra los datos de los libros disponibles
def listar():
  # Mostramos un mensaje indicando que se van a listar los libros disponibles
  print("Estos son los libros disponibles:")

  # Recorremos la lista de libros
  for libro in libros.lista:
    # Verificamos si el libro tiene el estado "disponible"
    if libro["estado"] == "disponible":
      # Mostramos los datos del libro
      print("Título:", libro["titulo"])
      print("Autor:", libro["autor"])
      print("Género:", libro["genero"])
      print("Año:", libro["año"])
      print("--------------------")

  # Volvemos al menú principal
  import menu
  menu.mostrar_menu()