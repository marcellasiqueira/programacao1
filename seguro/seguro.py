# coding: utf-8
# Cálculo de Seguro
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

def calcula_seguro(valor, lista):

	saida = []
	soma = 0
	idade, casado, risco = lista[0], lista[1], lista[2]
	portao, casa, propria, uso = lista[3], lista[4], lista[5], lista[6]
# avalia respostas
	if idade <= 21 or idade > 60:
		soma += 20
	elif idade >= 22 and idade <= 30:
		soma += 15
	elif idade >= 31 and idade <= 40:
		soma += 12
	elif idade >= 41 and idade <= 60:
		soma += 10
	if casado:
		soma += 10
	else:
		soma += 20
	if risco:
		soma += 20
	else:
		soma += 10
	if portao:
		soma += 20
	else:
		soma += 10
	if casa:
		soma += 20
	else:
		soma += 10
	if propria:
		soma += 10
	else:
		soma += 20
	if uso == 'Trabalho':
		soma += 10
	elif uso == 'Lazer' or uso == 'Misto':
		soma += 20
# nivel de risco e valor do seguro
	if soma <= 80:
		nivel_risco = "Risco Baixo"
		seguro = valor * 0.1
	elif soma > 80 and soma <= 100:
		nivel_risco = "Risco Medio"
		seguro = valor * 0.2
	else:
		nivel_risco = "Risco Alto"
		seguro = valor * 0.3

	saida.append(soma)
	saida.append(nivel_risco)
	saida.append(seguro)
	return saida
