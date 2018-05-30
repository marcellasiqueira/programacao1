# coding: utf-8
# Guerra Baralho
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

jogador1, jogador2, empates = 0, 0, 0

while True:
	rodada = raw_input().split()
	if rodada[0] == '0' and rodada[1] == '0': break
	if int(rodada[0]) > int(rodada[1]):
		jogador1 += 1
	elif int(rodada[1]) > int(rodada[0]):
		jogador2 += 1
	else:
		empates += 1

print "Jogador 1: %i, Jogador 2: %i, Empates: %i" % (jogador1, jogador2, empates)