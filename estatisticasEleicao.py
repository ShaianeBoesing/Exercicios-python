totalEleitores = int(input('Total de eleitores da cidade: '))
totalBranco = int(input('Total de votos brancos: '))
totalNulo = int(input('Total de votos nulos: '))
totalValido = int(input('Total de votos válidos: '))
totalVotos = totalBranco + totalNulo + totalValido

percentualBranco = (totalBranco / totalEleitores)*100
percentualNulo = (totalNulo / totalEleitores)*100
percentualValido = (totalValido / totalEleitores)*100

if (totalEleitores == totalVotos):
    result = 'Todos eleitores votaram'
else:
    naoVotaram = totalEleitores-totalVotos
    percentualNaoVotaram = (naoVotaram/totalEleitores)*100
    result = str(naoVotaram)+' eleitores não votaram'
    
    
print('Votos brancos: ', percentualBranco, '%')
print('Votos nulos: ', percentualNulo, '%')
print('Votos válidos: ', percentualValido, '%')
if percentualNaoVotaram:
    print('Não votaram: ', percentualNaoVotaram, '%')
    
print('Resultado: ', result)
