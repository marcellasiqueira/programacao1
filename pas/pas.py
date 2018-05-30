# coding: utf-8
# Quantas PAs?
# 2017, Marcella Siqueira / UFCG, Programação 1

razao, pas = int(raw_input()), 0

while True:
	sequencia = raw_input()
	if sequencia == 'fim': break
	sequencia = sequencia.split()
	cont = 0
	for i in range(len(sequencia) - 1):
		if int(sequencia[i + 1]) == int(sequencia[i]) + razao:
			cont += 1
	if cont == len(sequencia) - 1:
		pas += 1

print pas