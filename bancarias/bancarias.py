# coding: utf-8
# Operações Bancárias 
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

entrada = raw_input().split()
conta = float(entrada[1])

while True:
	operacao = raw_input().split()
	if len(operacao) == 1 and operacao[0] == '3': break
	if operacao[0] == '1':
		conta -= float(operacao[1])
	else:
		conta += float(operacao[1])

print "Saldo de R$ %.2f na conta de %s" % (conta, entrada[0])