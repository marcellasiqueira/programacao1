# coding: utf-8
# Bingo
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

jogador1, jogador2 = raw_input().split(), raw_input().split()
pontos1, pontos2 = 0, 0

while True:
	num = int(raw_input())
	for i in range(len(jogador1)):
		if num == int(jogador1[i]):
			pontos1 += 1
		if num == int(jogador2[i]):
			pontos2 += 1
	if pontos1 == len(jogador1) or pontos2 == len(jogador2): break

if pontos1 > pontos2:
	print "Bingo! Jogador 1 venceu."
elif pontos2 > pontos1:
	print "Bingo! Jogador 2 venceu."
else:
	print "Empate."