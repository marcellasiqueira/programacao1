# coding: utf-8
# Seleciona os Números Ímpares Positivos
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

numero, impares = int(raw_input()), []

for i in range(numero):
	if i % 2 != 0:
		impares.append(i)

for impar in impares:
	print impar		 