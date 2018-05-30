# coding: utf-8
# Coluna
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

def coluna(matriz, i):
	nova_matriz = []

	for j in range(len(matriz)):
		nova_matriz.append(matriz[j][i])

	return nova_matriz


M = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
assert coluna(M,0) == [1,2,3]
assert coluna(M,1) == [1,2,3]
assert coluna(M,2) == [1,2,3]
assert coluna(M,3) == [1,2,3]