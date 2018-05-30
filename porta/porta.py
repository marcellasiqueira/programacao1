# coding: utf-8
# Porta Eletrônica
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
pontos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
	entrada = raw_input()
	if entrada == 'S': break
	if entrada[0] == 'R':
		for i in range(len(alfabeto)):
			if entrada[2] == alfabeto[i]:
				pontos[i] += 1
	if entrada[0] == 'P':
		for i in range(len(alfabeto)):
			if entrada[2] == alfabeto[i]:
				print pontos[i]
