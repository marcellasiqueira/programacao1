# coding: utf-8
# Movimento Retilíneo Uniforme
# 2017, Marcella Siqueira / UFCG, Programação 1

pos_inicial = float(raw_input(""))
velocidade = float(raw_input(""))
tempo = float(raw_input(""))

pos_final = pos_inicial + (velocidade * tempo)

print "Posição final do móvel"
print "S(%.1f) = %.1f m" % (tempo, pos_final)
