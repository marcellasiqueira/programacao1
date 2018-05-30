# coding: utf-8
# Calculadora
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

while True:
	entrada = raw_input().split() 
	if len(entrada) == 1 and entrada[0] == '5': break
	if entrada[0] == '1':
		soma = int(entrada[1]) + int(entrada[2])
		print soma
	elif entrada[0] == '2':
		sub = int(entrada[1]) - int(entrada[2])
		print sub
	elif entrada[0] == '3':
		mult = int(entrada[1]) * int(entrada[2])
		print mult
	elif entrada[0] == '4' and entrada[2] == '0':
		print "Erro: Divisão por 0"
	else:
		div = int(entrada[1]) / int(entrada[2])
		print div