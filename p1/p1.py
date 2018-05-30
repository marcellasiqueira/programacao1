# coding: utf-8
# Questões para P1
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

profs, questoes = [], []

while True:
	recebe_prof = raw_input()
	if recebe_prof == '**': break
	profs.append(recebe_prof)
	questao = 0
	while True:
		quant_quest = raw_input()
		if quant_quest == '*': break
		questao += int(quant_quest)
	questoes.append(questao)

print "Relatório de novas questões:\n"

for i in range(len(profs)):
	print "%s: %i" % (profs[i], int(questoes[i]))

total = 0

for quest in questoes:
	total += quest

print "---"

print "Total de novas questões: %i" % total