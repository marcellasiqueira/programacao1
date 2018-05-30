# coding: utf-8
# Sequência de DNA
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

seq1, seq2 = raw_input(), raw_input()
contador = 0

for i in range(len(seq1)):
	if seq1[i] == seq2[i]:
		contador += 1

if contador > len(seq1) / 2:
	print "sim"
else:
	print "nao"