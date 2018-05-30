# coding: utf-8
# Conjuntos Maiores
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

limite, num = int(raw_input()), int(raw_input())
mconj, mnum = [], []

for i in range(num):
	soma = 0
	while True:
		conjunto = int(raw_input())
		if conjunto < 0: break
		soma += conjunto
	if soma > limite:
		mconj.append(i + 1)
		mnum.append(soma)

for i in range(len(mnum)):
	print "conjunto %i: %i" % (mconj[i], mnum[i])

