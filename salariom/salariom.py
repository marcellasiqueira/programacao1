# coding: utf-8
# Salário Mínimo 
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

ano_inicio = int(raw_input())
ano_fim = int(raw_input())
anos_acima = 0
anos_abaixo = 0
soma_acima = 0
soma_abaixo = 0

for i in range(ano_inicio, ano_fim+1):
    salario = float(raw_input())
    if salario > 100:
        anos_acima += 1
        soma_acima += salario
    if salario <= 100:
        anos_abaixo += 1
        soma_abaixo += salario

porcento_acima = (float(anos_acima) / (anos_acima + anos_abaixo)) * 100
porcento_abaixo = (float(anos_abaixo) / (anos_acima + anos_abaixo)) * 100
        
print "%d ano(s) abaixo (%.f%% dos anos)" % (anos_abaixo, porcento_abaixo)

if anos_abaixo > 0:
    media_abaixo = soma_abaixo / anos_abaixo
    print "média dos anos abaixo: U$ %.2f" % media_abaixo
    
print "%d ano(s) acima (%.f%% dos anos)" % (anos_acima, porcento_acima)

if anos_acima > 0:
    media_acima = soma_acima / anos_acima
    print "média dos anos acima: U$ %.2f" % media_acima
