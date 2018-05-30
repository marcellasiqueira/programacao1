# coding: utf-8
# Imprime Ranking (Cumulativo)
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

n, pontos, times, classificacao = int(raw_input()), [], [], []

for i in range(n):
	times.append(raw_input())
	pontos.append(int(raw_input()))
	classificacao.append(i + 1)

for i in range(n - 1):
	if pontos[i] == pontos[i + 1]:
		classificacao[i + 1] = classificacao[i] 

for i in range(n):
	print "%i. %s (%i)" % (classificacao[i], times[i], pontos[i])