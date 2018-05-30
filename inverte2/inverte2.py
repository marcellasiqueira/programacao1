# coding: utf-8
# Inverte 2 a 2 condicional
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

def inverte2a2_condicional(seq):
	for i in range(0, len(seq) - 1, 2):
		if int(seq[i]) > int(seq[i + 1]):
			seq[i], seq[i + 1] = seq[i + 1], seq[i]

seq = [3,1,2,3,10,5,6]
inverte2a2_condicional(seq)
assert seq == [1,3,2,3,5,10,6]

seq = [5,4,3,2,1]
inverte2a2_condicional(seq)
assert seq == [4,5,2,3,1]