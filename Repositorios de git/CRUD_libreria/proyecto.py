# Importamos los archivos que contienen las funciones para cada opción
import registrar_libro
import listar_libros
import eliminar_libro
import ver_libros_prestados

# Definimos una función que muestra el menú y pide al usuario que ingrese una opción
def mostrar_menu():
  # Mostramos las opciones disponibles
  print("Bienvenido al sistema de administración de la librería")
  print("Seleccione una opción:")
  print("1. Registrar libro")
  print("2. Listar libros disponibles")
  print("3. Eliminar libro")
  print("4. Ver libros prestados")
  print("5. Salir")

  # Pedimos al usuario que ingrese un número
  opcion = input("Ingrese el número de la opción: ")

  # Verificamos si el número es válido
  if opcion == "1":
    # Llamamos a la función para registrar libro
    registrar_libro.registrar()
  elif opcion == "2":
    # Llamamos a la función para listar libros disponibles
    listar_libros.listar()
  elif opcion == "3":
    # Llamamos a la función para eliminar libro
    eliminar_libro.eliminar()
  elif opcion == "4":
    # Llamamos a la función para ver libros prestados
    ver_libros_prestados.ver()
  elif opcion == "5":
    # Salimos del programa
    print("Gracias por usar el sistema")
    return
  else:
    # Mostramos un mensaje de error
    print("Opción inválida, por favor intente de nuevo")

  # Volvemos a mostrar el menú
  mostrar_menu()

# Llamamos a la función para mostrar el menú al iniciar el programa
mostrar_menu()

#Registrar-----------------------------------------------------------------------------

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
  
  #-Listar libros-----------------------------------------------------------------------
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
  #Eliminar------------------------------------------------------------------------------------
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
  
  #Libros prestados---------------------------------------------------------------------------------
  # Importamos el archivo que contiene la lista de libros
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