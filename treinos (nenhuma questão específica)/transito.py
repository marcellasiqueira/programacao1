# coding: utf-8

sequencia = raw_input()
letra = 'v'

tam = len(sequencia)
vetor = []

cont_letra = 0
i = 0
j = 0
       
while i < tam:
    if letra == sequencia[i]:
        j = i
        cont_letra = 1
        while j <= tam-2:
            if letra == sequencia[j]:
                j += 1
                cont_letra += 1 
            
        vetor.append(cont_letra)
        i = j + 1  
    else:
        i += 1
    
print vetor


