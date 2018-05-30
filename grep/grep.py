# coding: utf-8
# Grep
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

palavra, N = raw_input(), int(raw_input())

for i in range(N):
	frase = raw_input()
	f_dividida = frase.split()
	if len(f_dividida) == 1: 
		for i in range(len(frase) - 2):
			if palavra[0] == frase[i] and palavra[1] == frase[i+1] and palavra[2] == frase[i+2]:
				print frase
	else:	
		for chave in f_dividida:
			if palavra == chave:
				print frase