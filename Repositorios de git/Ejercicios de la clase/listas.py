#Crear en listas separadas ingresos y egresos, no puede ser negativo y no puede quedar en cero
#cada vez que ingrese o retire debe mostrar el saldo

ingresos = []
egresos = []
saldo = 0

while True:
    print("Menú:")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Ver saldo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad = float(input("Ingrese la cantidad a ingresar: "))
        saldo += cantidad
        ingresos.append(cantidad)
        print(f"Se han ingresado {cantidad:.2f} pesos.")
        print(f"Saldo actual: {saldo:.2f} pesos.")
    elif opcion == "2":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        if saldo - cantidad < 0:
            print("No se puede retirar esa cantidad. Saldo insuficiente.")
        else:
            saldo -= cantidad
            egresos.append(cantidad)
            print(f"Se han retirado {cantidad:.2f} pesos.")
            print(f"Saldo actual: {saldo:.2f} pesos.")
    elif opcion == "3":
        print(f"Saldo actual: {saldo:.2f} pesos.")
        print(f"Ingresos: {ingresos}")
        print(f"Egresos: {egresos}")
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Intente de nuevo.")