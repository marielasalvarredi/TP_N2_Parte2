grado = int(input("Ingrese el grado del polinomio: "))

x = float(input("Ingrese el valor de x: "))

coeficientes = []

for i in range(grado + 1):
    coeficiente = float(input(f"Ingrese a{i}: "))
    coeficientes.append(coeficiente)

resultado = 0
resultados= []
for i in range(grado + 1):
    resultado = resultado + coeficientes[i] * (x ** i)
    resultados.append(resultado)

print("Coeficientes:", coeficientes)
print("El valor del polinomio es:", resultado)

print("Resultados:", resultados)
print("Valor máximo obtenido:", max(resultados))
print("Valor mínimo obtenido:", min(resultados))

Ingrese el grado del polinomio: 3
Ingrese el valor de x: 2
Ingrese a0: 1
Ingrese a1: 2
Ingrese a2: 3
Ingrese a3: 4
Coeficientes: [1.0, 2.0, 3.0, 4.0]
El valor del polinomio es: 49.0
Resultados: [1.0, 5.0, 17.0, 49.0]
Valor máximo obtenido: 49.0
Valor mínimo obtenido: 1.0
