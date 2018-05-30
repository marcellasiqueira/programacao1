# coding: utf-8

N = int(raw_input())
pos_maior, digitos = 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(N):
	matricula = raw_input()
	
	for digito in matricula:
		dig = int(digito)
		digitos[dig] += 1
	
for i in range(1, 10):
	if digitos[pos_maior] < digitos[i]:
		pos_maior = i
		
print pos_maior, digitos[pos_maior]
