# coding: utf-8
# Busca Todos em Matriz
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

def busca_matriz(m, e):
	nova_matriz = []
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j] == e:
				nova_matriz.append((i, j))

	if len(nova_matriz) > 0:
		return nova_matriz
	else:
		return []

matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [1, 2, 3, 2, 1],
]
assert busca_matriz(matriz, 4) == []
assert set(busca_matriz(matriz, 3)) == set( [(0,1), (0,3), (1,0), (2,2)] )
