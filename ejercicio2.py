notas = []
for i in range(1, 6):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i} (0-10): "))
        except ValueError:
            print("Entrada inválida. Ingrese un número.")
            continue
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        print("La nota debe estar entre 0 y 10.")

media = sum(notas) / len(notas)
maxima = max(notas)
minima = min(notas)

print("\n--- Resumen de Notas ---")
print(f"Notas obtenidas: {notas}")
print(f"Nota media: {media:.2f}")
print(f"Nota más alta: {maxima}")
print(f"Nota más baja: {minima}")

