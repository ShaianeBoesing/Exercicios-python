while True:
    nome = input('Nome: ')
    if (nome == ''):
        break
    saltos = [float(input(f'{i+1}º salto: ')) for i in range (5)]

    copiaSaltos = saltos.copy()
    saltos.sort()
    maiorSalto = saltos[len(saltos)-1]
    menorSalto = saltos[len(saltos)-len(saltos)]
    saltos.remove(maiorSalto)
    saltos.remove(menorSalto)
    media = sum(saltos)/len(saltos)

    print('Atleta: ', nome)
    [print(f'{i+1}º salto: {copiaSaltos[i]}') for i in range (5)]
    print(f'Melhor salto: {maiorSalto}')
    print(f'Pior salto: {menorSalto}')
    print(f'Média dos demais saltos: {media:.1f}')
    print(f'''Resultado Final:
        {nome}: {media:.1f}''')
    
    