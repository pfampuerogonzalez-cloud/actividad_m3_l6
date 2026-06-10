while True:
    try:
        num = int(input("Ingrese un número entre 1 y 100: "))
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")
        continue

    if num <= 1 or num > 100:
        print("El úmero debe estar entre 1 y 100. Intente nuevamente.")
        continue

    if num % 2 == 0:
        pares = [str(i) for i in range(num + 2, 101, 2)]
        print(f"Ha ingresado un número par y los números pares siguientes son: {' '.join(pares)}")
    else:
        impares = [str(i) for i in range(num + 2, 100, 2)]
        print(f"Ha ingresado un número impar y los números impares siguientes son: {' '.join(impares)}")
    break
