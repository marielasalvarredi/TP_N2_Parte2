n = int(input("Ingrese la cantidad de términos: "))

suma = 1
resultados = [1]

for i in range(1, n):
    termino = ((-1) ** i) / (2 * i)

    resultados.append(termino)
    suma += termino

print("Lista de términos:", resultados)
print("Suma final =", suma)
print(f"Término máximo: {max(resultados)}")
print(f"Término mínimo: {min(resultados)}")
print(f"Promedio de los términos: {suma / len(resultados)}")
