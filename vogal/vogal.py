# coding: utf-8
# Imprime Primeira Vogal
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

palavra = raw_input()

vogais = "aeiouAEIOU"

for letra in palavra:
	if letra in vogais:
		print letra
		break
else:
	print "-"