# coding: utf-8

def selecao(lista):
	for i in range(len(lista) - 1):
		min = i
		for j in range(i + 1, len(lista)):
			if lista[j] < lista[min]:
				min = j
		lista[min], lista[i] = lista[i], lista[min]
	return lista

l = [7,4,1,2,0]

print selecao(l)