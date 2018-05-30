# coding: utf-8
# Lucro Mensal de uma Empresa
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

total = []  # a quantidade total de receitas e despesas no ano

for i in range(12):
    variavel_auxiliar = []
    receita_despesa = raw_input()
    variavel_auxiliar = receita_despesa.split()
    total.append(variavel_auxiliar[0])
    total.append(variavel_auxiliar[1])
    
lucros_mensais = [] 

for i in range(0, len(total), 2):
    lucro = float(total[i]) - float(total[i+1])
    lucros_mensais.append(lucro)
    
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'] 

for i in range(12):
    print meses[i], "%4.1f" % float(lucros_mensais[i])

