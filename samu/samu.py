# coding: utf-8
# Atendimentos no SAMU
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

soma, atendimentos = 0, []

for i in range(12):
	atendimento = int(raw_input())
	soma += atendimento
	atendimentos.append(atendimento)

media = float(soma) / 12
acima_media, meses = [], []

for i in range(len(atendimentos)):
	if atendimentos[i] > media:
		acima_media.append(atendimentos[i])
		meses.append(i+1)

print "Média mensal de atendimentos: %.2f" % media
print "----"

for i in range(len(acima_media)):
	print "Mês %s: %s" % (meses[i], acima_media[i])
