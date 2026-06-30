def crea_matriz (L):
    matriz=[]
    contador= inicio
    for i in range (L):
        fila=([])
        for j in range (L):
            fila.append(contador)
            contador +=1
        matriz.append(fila)
    return matriz

inicio=int(input("Ingrese el número inicial: "))
L=int(input("Ingrese el tamaño de matriz: "))
matriz=crea_matriz(L)
for fila in matriz:
    print(fila)