# coding: utf-8
# Pares de Múltiplos
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

nums = raw_input()
sequencia = nums.split()
multiplo = int(raw_input())
cont = 0 
pares = []

for i in range(len(sequencia) - 1):
    if int(sequencia[i]) * multiplo == int(sequencia[i+1]) or int(sequencia[i+1]) * multiplo == int(sequencia[i]):
	    cont += 1
	    pares.append(sequencia[i])
	    pares.append(sequencia[i+1])
	    
print "%.f par(es)" % cont

for i in range(0, len(pares), 2):
    print pares[i], pares[i+1]
