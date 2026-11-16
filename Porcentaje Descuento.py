tipo = int(input("1 = Textil 2 = Electrodomésticos 3 = Elementos de cocina 4 = Videojuegos"))
if tipo == 1:
    descuento = 0
else:
    if tipo == 2:
        descuento = 3.7
    else:
        if tipo == 3:
            descuento = 4.2
        else:
            if tipo == 4:
                descuento = 7.8
            else:
                print("Invalido")
                descuento = 0
print("El descuento es", descuento, "%")