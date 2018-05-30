# coding: utf-8
# Pesquisa Voos
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

N, cont, registro, melhor = int(raw_input()), 0, [], []
valores, horas, conexoes, empresas = [], [], [], []

while cont < N:
	registro = raw_input().split(',')
	valores.append(registro[0])
	conexoes.append(registro[1])
	horas.append(registro[2])
	empresas.append(registro[3])
	cont += 1

valor, ind_valor = 10000000, -1

for i in range(len(valores)):
	if float(valores[i]) < valor:
		valor = float(valores[i])
		ind_valor = i

melhor.append(empresas[ind_valor])

hora, ind_horas = 1000000, -1

for i in range(len(horas)):
	if int(horas[i]) < hora:
		hora = int(horas[i])
		ind_horas = i

melhor.append(empresas[ind_horas])

conexao, ind_conexao = 1000000, -1

for i in range(len(conexoes)):
	if int(conexoes[i]) < conexao:
		conexao = int(conexoes[i])
		ind_conexao = i

melhor.append(empresas[ind_conexao])

while True:
	saida = raw_input()
	if saida == 'fim': break
	if saida == 'valor':
		print melhor[0]
	elif saida == 'tempo':
		print melhor[1]
	else:
		print melhor[2]
