# coding: utf-8
# Quem Acertou Menos
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

N, alunos = int(raw_input()), []

for i in range(N):
	alunos.append(raw_input())

erros = []

for aluno in alunos:
	erro = 0
	for fail in aluno:
		if fail == 'f':
			erro += 1
	erros.append(erro)

errou_mais, aluno_necessitado = 0, 0

for i in range(len(erros)):
	if erros[i] > errou_mais:
		errou_mais = erros[i]
		aluno_necessitado = i + 1

print "O aluno %i errou %i teste(s)." % (aluno_necessitado, errou_mais)
