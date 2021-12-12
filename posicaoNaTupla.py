minhaTupla = (-14,12,9,7,-80,1,2,20,22,14376852154)

for val in minhaTupla:
    pos = minhaTupla.index(val)
    if (pos == 0):
        maior = val
        menor = val
        posMaior = pos
        posMenor = pos
        
    if (val > maior):
        posMaior = pos
    
    if (val < menor):
        posMenor = pos
        
print ('posição do maior:', posMaior)
print ('posição do menor:', posMenor)
