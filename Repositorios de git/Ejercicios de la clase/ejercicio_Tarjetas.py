#simular una tarjeta de credito que pide valor y cuotas  (Ciclo While)

def procesar_compra(compra, cuotas):
    estado = True
    deuda = compra
    saldo = 0
    pago = 0
    valor_cuota = compra / cuotas
    print(f"El valor de cuota mínimo es {valor_cuota:.2f}")

    if valor_cuota > deuda:
        valor_cuota = deuda
    else:
        valor_cuota = valor_cuota

    while estado:
        if deuda > 0:
            if cuotas > 0:
                pagar_minimo = input("¿Deseas pagar el mínimo? (si / otro): ")

                if pagar_minimo.lower() == "si":
                    deuda -= valor_cuota
                    print(f"Valor pagado {valor_cuota:.2f} valor deuda {deuda:.2f}")
                else:
                    pago = float(input("Ingrese el monto a pagar: $"))

                if pago > deuda:
                    print("El monto ingresado es mayor que la deuda restante.")
                    continue

                deuda -= pago
                cuotas -= 1
                saldo += pago

                print(f"Deuda restante: ${deuda:.2f}")
                print(f"Cuotas restantes: {cuotas}")
            else:
                print("Tarjeta pagada.")
                cuotas = 0
                deuda = 0
                estado = False
        else:
            print("Tarjeta pagada.")
            cuotas = 0
            deuda = 0
            estado = False
