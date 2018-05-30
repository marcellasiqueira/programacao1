# coding: utf-8
# A Primeira Letra em Caixa Alta
# 2017, Marcella Siqueira / UFCG, Programação 1
# Matrícula: 117110492

def caixa_alta(frase):

    palavra_modificada = ''
    ajustado = False
    if len(frase) == 1:
        palavra_modificada += frase[0].lower()
    else:
        for palavra in range(len(frase) - 1):
            if frase[palavra + 1] != chr(32) and ajustado == False:
                palavra_modificada += frase[palavra].upper()
                ajustado = True
            elif frase[palavra + 1] == chr(32) or frase[palavra - 1] == chr(32) and frase[palavra + 1] == chr(32):
                palavra_modificada += frase[palavra].lower()
            elif frase[palavra - 1] == chr(32) and frase[palavra] != ' ':
                palavra_modificada += frase[palavra].upper()
            else:
                palavra_modificada += frase[palavra]
        if frase[len(frase) - 2] == chr(32):
            palavra_modificada += frase[len(frase) -1].lower()
        else:
            palavra_modificada += frase[len(frase) - 1]

    return palavra_modificada