# coding: utf-8
# Utilizando o Teorema de Herão para Calcular a Área de Triângulos
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

import math
N, triangulos = int(raw_input()), []

for i in range(N):
	lados = raw_input().split()
	triangulos.append(lados)

sperimetros = []

for i in range(len(triangulos)):
	sperimetro = 0
	for lado in triangulos[i]:
		sperimetro += float(lado) / 2
	sperimetros.append(sperimetro)

areas = []

for i in range(len(triangulos)):
	ladoa = float(sperimetros[i]) - float(triangulos[i][0])
	ladob = float(sperimetros[i]) - float(triangulos[i][1])
	ladoc = float(sperimetros[i]) - float(triangulos[i][2])
	A = math.sqrt(float(sperimetros[i]) * ladoa * ladob * ladoc)
	areas.append(A)

quant_acima, soma = 0, 0

for area in areas:
	if float(area) >= 100:
		quant_acima += 1
		soma += float(area)

for i in range(len(triangulos)):
	print "Área %i: %.2f" % (i + 1, float(areas[i]))

media = 0.0

if quant_acima >= 1:
	media = float(soma) / quant_acima
	print "Número maiores: %i, área média: %.2f" % (quant_acima, media)