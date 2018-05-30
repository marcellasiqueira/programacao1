# coding: utf-8
# Tiro ao Alvo
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

from math import sqrt

cont, distancias, dmedia = 0, [], 0

while True:
	coordenada = raw_input().split(",")
	x, y = float(coordenada[0]), float(coordenada[1])
	distancia = sqrt(x ** 2 + y ** 2)
	if distancia > 200: break
	cont += 1
	distancias.append(distancia)

for num in distancias:
	dmedia += num / len(distancias)

for num in distancias:
	print "%.2f" % num

print "--"
print "num disparos: %i" % cont
print "distancia media: %.2f" % dmedia 

