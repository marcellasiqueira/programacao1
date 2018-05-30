# coding: utf-8
# Encontra elemento
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

N = int(raw_input())
sequencia = raw_input().split()

for numero in sequencia:
	if N == int(numero):
		print "sim"
		break
else:
	print "não"
