# coding: utf-8
# Quem Bebeu Mais Menos
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

def quem_bebeu_mais_menos(sabado, domingo):
	# Para somar as bebidas do fim de semana
	bebida_fds = []
	for i in range(len(sabado)):
		bebida_fds.append([])

	for i in range(len(sabado)):
		for j in range(len(sabado[0])):
			soma = sabado[i][j] + domingo[i][j]
			bebida_fds[i].append(soma)

	# Para somar a bebida de cada amigo
	bebida_total = []
	for i in range(len(bebida_fds)):
		bebida_total.append([])

	for i in range(len(bebida_fds[0])):
		total = 0
		for j in range(len(bebida_fds)):
			total += bebida_fds[j][i]
		bebida_total[i].append(total)

	# Para calcular quem bebeu mais e quem bebeu menos
	bebado, sobrio = 0, 50

	for i in range(len(bebida_total)):
		if bebida_total[i][0] > bebado:
			bebado = bebida_total[i][0]
			mais = i + 1

		if bebida_total[i][0] < sobrio:
			sobrio = bebida_total[i][0]
			menos = i + 1

	return (mais, menos)


sabado = [[1,2,3], [0,1,0], [3,1,2]]
domingo = [[2,1,3], [0,2,1], [1,1,2]]
assert quem_bebeu_mais_menos(sabado, domingo) == (3,1)

sabado = [[1,2,3,4,5], [0,1,2,3,1], [2,1,0,1,2], [3,1,2,1,3], [4,1,3,0,0]]
domingo = [[0,1,1,0,1], [1,2,2,0,2], [2,3,1,1,1], [3,4,2,0,0], [4,3,3,0,0]]
assert quem_bebeu_mais_menos(sabado, domingo) == (1,4)

	

