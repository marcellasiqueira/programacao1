# coding: utf-8

altura = int(raw_input())

qnt_esp = altura - 1

qnt_o = 1

for alt in range(altura):

	saida = " " * qnt_esp + "o" * qnt_o

 	print saida

 	qnt_o += 2

 	qnt_esp -= 1

print " " * (altura - 1) + "o"