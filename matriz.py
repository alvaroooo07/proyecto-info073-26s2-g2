def matriz_diagonal (L):
    LD=[]
    for x in range (len(L)):
        for y in range (len(L)):
            if x==y:
                LD.append(L[x][y])
    return LD

L=[[1,2,3],[4,5,6],[7,8,9]]
print(matriz_diagonal(L))