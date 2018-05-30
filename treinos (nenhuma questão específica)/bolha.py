# coding: utf-8

def bolha(lista):
	for i in range(len(lista) - 1):
		for j in range(len(lista) - 1):
			if lista[j] > lista[j + 1]:
				lista[j], lista[j + 1] = lista[j + 1], lista[j]
	return lista
		
l = [7,1,4,0]
print bolha(l)