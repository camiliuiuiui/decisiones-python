minValor = int(input(("Ingrese el valor mínimo del intervalo: ")))
maxValor = int(input(("Ingrese el valor máximo del intervalo: ")))
number = int(input(("Ingrese el número a verificar: ")))
if number >= minValor and number <= maxValor:
    print("El valor", number, "está dentro del intervalo [", minValor, ",", maxValor, "]")
else:
    print("El valor", number, "está afuera del intervalo [", minValor, ",", maxValor, "]")