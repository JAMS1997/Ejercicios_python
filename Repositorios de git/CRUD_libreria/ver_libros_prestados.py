import libros

# Definimos una función que muestra los datos de los libros prestados
def ver():
  # Mostramos un mensaje indicando que se van a listar los libros prestados
  print("Estos son los libros prestados:")

  # Recorremos la lista de libros
  for libro in libros.lista:
    # Verificamos si el libro tiene el estado "prestado"
    if libro["estado"] == "prestado":
      # Mostramos los datos del libro
      print("Título:", libro["titulo"])
      print("Autor:", libro["autor"])
      print("Género:", libro["genero"])
      print("Año:", libro["año"])
      print("--------------------")

  # Volvemos al menú principal
  import menu
  menu.mostrar_menu()