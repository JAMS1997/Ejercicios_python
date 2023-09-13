#1. Validar que una compra se va a pagar por un valor x y si incluye o no propina 

valor = input ("Valor a pagar: $_")
pago = input("Va a pagar (si/no) :")
propina = input("incluir propina (si/no) :")

if (pago.lower() == 'si' and propina.lower() == 'si'):
    print(f"el pago es de $ {float(valor) * 1.10}")
elif (pago.lower() == 'si' and propina.lower() == 'no'):
    print(f"el pago es de $ {valor}")
else: 
    print("suerte")