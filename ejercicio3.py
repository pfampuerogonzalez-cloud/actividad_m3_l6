meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

try:
    num_mes = int(input("Ingrese el número del mes (1-12): "))
    
    if 1 <= num_mes <= 12:
        nombre = meses[num_mes - 1]
        dias = dias_por_mes[num_mes - 1]
        
        print(f"El mes {num_mes} es {nombre} y tiene {dias} días.")
    else:
        print("Fuera de rango. Debe ser del 1 al 12.")
except ValueError:
    print("Por favor, ingrese un número entero.")
