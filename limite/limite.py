# coding: utf-8
# Limite de gastos
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

limite, medias = float(raw_input()), []

while True:
	sequenciastr = raw_input()
	soma = 0
	if sequenciastr == 'fim': break
	sequencia = sequenciastr.split()
	for i in range(len(sequencia)):
		soma += float(sequencia[i])
	media = soma / len(sequencia)
	if media * 2 < limite: break
	if media > limite:
		medias.append(sequenciastr)

for m in medias:
	print m