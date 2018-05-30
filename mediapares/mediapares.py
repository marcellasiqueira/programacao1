# coding: utf-8
# Quantidade e Média de Números Pares
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

N, numeros = int(raw_input()), []

for i in range(N):
	num = int(raw_input())
	numeros.append(num)

quant_pares = 0
soma = 0

for numero in numeros:
	if numero % 2 == 0:
		soma += numero
		quant_pares += 1

media = float(soma) / quant_pares

abaixo_media = 0

for numero in numeros:
	if numero < media:
		abaixo_media += 1

print "soma: %i" % soma
print "média: %.1f" % media
print "%i número(s) abaixo da média" % abaixo_media