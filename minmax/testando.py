# coding: utf-8

def minmax_sort(lista):
    lista_final = []
    maior, menor, m = 0, 0, len(lista)
    for i in range(0, int(m/2)):
        for j in range(i, m):
            if lista[j] < lista[menor]:
                menor = j

        lista[menor], lista[i] = lista[i], lista[menor]

        for k in range(i, m):
            if lista[k] > lista[maior]:
                maior = k

        lista[maior], lista[m - 1] = lista[m - 1], lista[maior]

        m -= 1
        
        lista_copia = []
        for i in range(len(lista)):
            lista_copia.append(lista[i])

        lista_final.append(lista_copia)

    return lista_final

assert minmax_sort([7, 4, 8, 1, 2, 3]) == [[1, 4, 3, 7, 2, 8],
                                           [1, 2, 3, 4, 7, 8],
                                           [1, 2, 3, 4, 7, 8]]