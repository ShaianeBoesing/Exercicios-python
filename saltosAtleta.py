
while True:
    nome = input('Nome do atleta: ')
    saltos = []
    maior = 0
    menor = 0
    media = 0
    for i in range(1, 6):
        salto = float(input(f'Salto {i}: '))
        saltos.append(salto)
        if (i == 1):
            menor = salto

        if (salto > maior):
            maior = salto
        if (salto < menor):
            menor = salto

    saltosRestantes = saltos.copy();
    saltosRestantes.remove(menor)
    saltosRestantes.remove(maior)
    media = sum(saltosRestantes)/len(saltosRestantes)

    print(f'Atleta: {nome}')
    for i in range(1, len(saltos)+1):
        print(f'{i}º : {saltos[i-1]}')

    print(f'melhor salto: {maior}')
    print(f'pior salto: {menor}')
    print(f'média dos demais saltos: {media:.2f}')
    print(f'Resultado final: {nome} {media:.2f}')

    if (nome == ''):
        break