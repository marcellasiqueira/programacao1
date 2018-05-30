# coding: utf-8
# Criptografando uma Senha
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

palavra = raw_input()
palavra = palavra.lower()

for i in range(1, len(palavra)):
    if palavra[i] == 'a':
        palavra[i] = 4

print palavra
