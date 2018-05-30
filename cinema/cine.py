# coding: utf-8
# Calcula despesas do cinema
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

dia =  raw_input("Dia da semana? ")
orcamento =  int(raw_input("Orcamento? R$ "))
adultos =  int(raw_input("Numero de adultos? "))
criancas =  int(raw_input("Numero de criancas? "))
pizza = int(raw_input("Preco da pizza? R$ "))
refrigerante = float(raw_input("Preco do refrigerante? R$ "))
estacionamento = float(raw_input("Preco do estacionameto? R$ "))
cinema = float(raw_input("Preco do ingresso do cinema? R$ "))

gastos_alimentacao = pizza + refrigerante
gastos_cinema = (cinema + 2) * adultos + (cinema + 2 / 2) * criancas
gastos_total = gastos_cinema + gastos_alimentacao + estacionamento

print "========== Despesas de %s ==========" % dia
print "Despesas com alimentacao: R$ %.1f" % gastos_alimentacao
print "Despesas com cimena: R$ %.1f" % gastos_cinema
print "Despesas por pessoa: R$ %.1f" % (gastos_total / criancas + adultos)
print "Saldo diponivel: %.1f" % (orcamento - gastos_total)
