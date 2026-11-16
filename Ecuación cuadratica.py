valor1 = float(input(("Ingrese el valor 1: ")))
valor2 = float(input(("Ingrese el valor 2: ")))
valor3 = float(input(("Ingrese el valor 3: ")))
resultado = valor2**2 - 4 * valor1 * valor3
if valor1 == 0:
    print("No es una ecuación cuadrática")
else:
    if resultado >= 0:
        print("La ecuación tiene solución")
    else:
        print("La ecuación no tiene solución")