# coding: utf-8
# Pesquisa Hotéis
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

valores, tamanhos, confortos, hoteis, melhor = [], [], [], [], []

while True:
	registro = raw_input().split(',')
	if len(registro) == 1 or registro == '---': break
	valores.append(registro[0])
	tamanhos.append(registro[1])
	confortos.append(registro[2])
	hoteis.append(registro[3])

valor = 10000000

ind_valores = -1

for i in range(len(valores)):
	if float(valores[i]) < valor:
		valor = float(valores[i])
		ind_valores = i

melhor.append(hoteis[ind_valores])

tamanho = 0

ind_tamanho = -1

for i in range(len(tamanhos)):
	if int(tamanhos[i]) > tamanho:
		tamanho = int(tamanhos[i])
		ind_tamanho = i

melhor.append(hoteis[ind_tamanho])

conforto = 0

ind_conforto = -1

for i in range(len(confortos)):
	if int(confortos[i]) > conforto:
		conforto = int(confortos[i])
		ind_conforto = i

melhor.append(hoteis[ind_conforto])

while True:
	saida = raw_input()
	if saida == 'fim': break
	if saida == 'valor':
		print melhor[0]
	if saida == 'tamanho':
		print melhor[1]
	if saida == 'conexões':
		print melhor[2]
