# coding: utf-8
# Matriz Menor
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

def matriz_menor(matriz, matriz2):
	nova_matriz = []
	for i in range(len(matriz)):
		nova_matriz.append([])

	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if matriz[i][j] < matriz2[i][j]:
				nova_matriz[i].append(matriz[i][j])
			else:
				nova_matriz[i].append(matriz2[i][j])

	return nova_matriz

M1 = [[1,2,3],
          [13,14,15],
          [7,8,9]]

M2= [[10,11,12],
         [4,5,6],
         [7,8,9]]

M3= [[1,2,3],
         [0,0,0],
         [7,8,9]]

assert matriz_menor(M1, M2) == [[1,2,3],[4,5,6],[7,8,9]]
assert matriz_menor(M1, M3) == [[1,2,3],[0,0,0],[7,8,9]]