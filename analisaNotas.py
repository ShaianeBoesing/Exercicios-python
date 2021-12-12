def analisaNotas(notas):
    media = sum(notas)/len(notas)
    notas.sort()
    menor = notas[len(notas)-len(notas)]
    maior = notas[len(notas) - 1]
    print(f'Média do aluno: {media:.2f}')
    print(f'Maior nota do aluno: {maior}')
    print(f'Menor nota do aluno: {menor}')
    print(f'Diferença entre maior e menor nota: {maior-menor}')

notas = list()
while len(notas) < 3:
    nota = float(input(f'Informe a {len(notas)+1}ª nota: '))
    if (0 <= nota <= 10):
        notas.append(nota)
    else:
        print('A nota deve estar entre 0 e 10. ')


analisaNotas(notas)