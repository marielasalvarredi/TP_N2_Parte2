try:
    limite = float(input("Ingrese un valor límite positivo: "))

    if limite <= 0:
        print("El límite debe ser positivo.")
    else:
        suma = 0
        n = 0
        sumas = []

        while suma <= limite:
            n += 1
            suma += 1 / n
            sumas.append(suma)

        print("Cantidad de términos necesarios:", n)
        print("Suma obtenida:", suma)
        print("Sumas parciales:", sumas)

except ValueError:
    print("Debe ingresar un número válido.")
