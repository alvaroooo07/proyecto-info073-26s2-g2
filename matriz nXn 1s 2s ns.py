def llena_filas(N):
    matriz = []
    for i in range(1, N+1):
        fila = [i] * N
        matriz.append(fila)
    return matriz

try:
    N = int(input("Ingrese el tamaño N de la matriz: "))
    if N > 0:
        matriz_resultado = llena_filas(N)
        print(f"\nMatriz de {N}x{N} generada:")
        for fila in matriz_resultado:
            print(fila)
    else:
        print("Por favor, ingrese un número entero positivo para N.")
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número entero positivo para N.")