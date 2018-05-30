# coding: utf-8

num_linha = int(raw_input())
simbolos = []

for i in range(num_linha):
	simbolos.append(raw_input())

simbolo_x, simbolo_o = 0, 0

for linha in simbolos:
	if len(linha) != num_linha:
		print "Tabuleiro inválido"
		break
	else:
		for caractere in linha:
			if caractere == 'x':
				simbolo_x += 1
			else:
				simbolo_o += 1
else:
	if simbolo_x > simbolo_o:
		print "Xis ganhou com %i pontos." % simbolo_x
	elif simbolo_o > simbolo_x:
		print "Bola ganhou com %i pontos." % simbolo_o
	else:
		print "Empatou com %i pontos." % simbolo_x	
