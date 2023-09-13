# Importamos el archivo que contiene la lista de libros
import libros

# Definimos una función que elimina un libro de la lista
def eliminar():
  # Pedimos al usuario que ingrese el título del libro que desea eliminar
  titulo = input("Ingrese el título del libro que desea eliminar: ")

  # Creamos una variable para indicar si se encontró el libro
  encontrado = False

  # Recorremos la lista de libros
  for libro in libros.lista:
    # Verificamos si el libro tiene el mismo título que el ingresado por el usuario
    if libro["titulo"] == titulo:
      # Eliminamos el libro de la lista
      libros.lista.remove(libro)

      # Mostramos un mensaje de confirmación
      print("El libro ha sido eliminado exitosamente")

      # Cambiamos el valor de la variable encontrado a True
      encontrado = True

      # Salimos del bucle
      break

  # Verificamos si no se encontró el libro
  if not encontrado:
    # Mostramos un mensaje de error
    print("No se encontró ningún libro con ese título")

  # Volvemos al menú principal
  import menu
  menu.mostrar_menu()
  