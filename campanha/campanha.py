# coding: utf-8
# Campanha
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

pro, contra, vitorias, empates, derrotas = 0, 0, 0, 0, 0
casa, fora = 0, 0

for i in range(10):
	placar = raw_input()
	if placar[5] == 'c':
		pro += int(placar[0])
		contra += int(placar[2])
		if placar[0] > placar[2]:
			vitorias += 1
			casa += 3
		elif placar[0] == placar[2]:
			empates += 1
			casa += 1
		else:
			derrotas += 1
	else:
		pro += int(placar[2])
		contra += int(placar[0])
		if placar[2] > placar[0]:
			vitorias += 1
			fora += 3
		elif placar[0] == placar[2]:
			empates += 1
			fora += 1
		else:
			derrotas += 1

pontos = casa + fora

saldo = pro - contra

print "%iv, %ie, %id" % (vitorias, empates, derrotas)
print "pontos: %i" % pontos
print "saldo: %i (%i pro, %i contra)" % (saldo, pro, contra)
print "pontos em casa: %i" % casa
print "pontos fora: %i" % fora