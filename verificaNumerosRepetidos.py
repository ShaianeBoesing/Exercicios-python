def verificaNumerosRepetidos(numeros):
    for num in numeros:
        qtd = numeros.count(num)
        if (qtd > 1):
             print('Existem valores repetidos nessa lista')
             break
        


nElementos = int(input('Informe quantos elementos deseja informar: '))
listaNumeros = []
for i in range(nElementos):
    listaNumeros.append(int(input(f'{i+1}º número:')))
    
verificaNumerosRepetidos(listaNumeros)