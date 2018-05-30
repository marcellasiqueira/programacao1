# coding: utf-8

def insercao(lista):
	for i in range(1, len(lista)):
		escolhido = lista[i]
		j = i - 1
		while j >= 0 and escolhido < lista[j]:
			lista[j + 1] = lista[j]
			j = j - 1
		lista[j + 1] = escolhido

	return lista

l = [7,4,1,2,0]
print insercao(l)