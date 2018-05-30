# coding: utf-8
# Transposta
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

def transposta(M):
	lista_transposta = []
	for i in range(len(M[0])):
		lista_transposta.append([])

	for i in range(len(M[0])):
		for j in range(len(M)):
			lista_transposta[i].append(M[j][i])

	return lista_transposta

M = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3]]

assert transposta(M) == [[1,2,3],
                         [1,2,3],
                         [1,2,3],
                         [1,2,3]]

assert M == [[1,1,1,1],
             [2,2,2,2],
             [3,3,3,3]]