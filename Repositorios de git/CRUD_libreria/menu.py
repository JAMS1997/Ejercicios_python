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