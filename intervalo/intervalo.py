# coding: utf-8

def soma_intervalo(a,b):
	i = a
	soma = 0
	while i <= b:
		soma += i
		i += 1
	return soma

assert soma_intervalo(5,15) == 110
assert soma_intervalo(10,10) == 10