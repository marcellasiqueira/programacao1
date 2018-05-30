# coding: utf-8
# Convertendo um Número Octal em um Número Decimal
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

octal = raw_input()

cont, soma = len(octal) - 1, 0

for i in range(len(octal)):
	print "%i * 8^%i = %i" % (int(octal[i]), cont, int(octal[i]) * 8 ** cont)
	soma += int(octal[i]) * 8 ** cont
	cont -= 1

print "%i(8) = %i(10)" % (int(octal), soma)