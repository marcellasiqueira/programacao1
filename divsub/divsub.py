# coding: utf-8
# Divisão por Subtrações
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

entrada = raw_input().split()
D, d, cont = int(entrada[0]), int(entrada[1]), 0

while True:
	if D < d:
		print "%i - %i < 0" % (D, d)
		break
	D -= d 
	print "%i - %i = %i" % (D + d, d, D)
	cont += 1

print "==="
print "quociente = %i" % cont
print "resto = %i" % D
