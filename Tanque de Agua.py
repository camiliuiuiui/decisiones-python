litros = float(input("Ingrese la cantidad de litros del tanque: "))
if litros < 250:
    print("Abrir la llave")
else:
    if litros > 450:
        print("Cerrar la llave")
    else:
        print("Mantener la llave cerrada")