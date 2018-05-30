# coding: utf-8
# Palavras com Letras Dobradas
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

N = int(raw_input())
palavras, dobradas, nao_dobradas = [], [], []

for i in range(N):
	palavras.append(raw_input())
	
for palavra in palavras:
	for i in range(len(palavra) - 1):
		if palavra[i] == palavra[i + 1]:
			dobradas.append(palavra)
			break
	else:
		nao_dobradas.append(palavra)
		
print "%i palavra(s) com letras dobradas:" % len(dobradas)

for palavra in dobradas:
	print palavra
print "---"

print "%i palavra(s) sem letras dobradas:" % len(nao_dobradas)

for palavra in nao_dobradas:
	print palavra
