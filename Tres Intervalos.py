a1 = int(input("Intervalo 1, ingrese límite inferior: "))
b1 = int(input("Intervalo 1, ingrese límite superior: "))
a2 = int(input("Intervalo 2, ingrese límite inferior: "))
b2 = int(input("Intervalo 2, ingrese límite superior: "))
a3 = int(input("Intervalo 3, ingrese límite inferior: "))
b3 = int(input("Intervalo 3, ingrese límite superior: "))
number = int(input("Ingrese el número: "))

if (number > a1 and number < b1) or (number > a2 and number < b2) or (number > a3 and number < b3):
    print("El valor", number, "está dentro")
else:
    print("El valor", number, "está afuera")