def calculaMedia():
    mediaTurma = 0
    notasTurma = 0
    contador = 0
    maiorMedia = 0
    for i in range(1, 6):
        notasAluno = 0
        for c in range(1, 4):
            nota = int(input(f'Informe a {c}ª nota do aluno {i} na escala de 0 a 10: '))
            notasTurma += nota
            contador += 1
            notasAluno += nota
        
        mediaAluno = notasAluno / (c)
        if (mediaAluno > maiorMedia):
            maiorMedia = mediaAluno
        
    mediaTurma = notasTurma/contador
    
    return mediaTurma, maiorMedia


def verificaAprovacao(media):
    if (media > 5.75):
        resultado = 'Aprovado!'
    elif (media > 2.75):
        resultado = 'Em recuperação!'
    else:
        resultado = 'Reprovado!'
    
    return resultado


mediaTurma, maiorMedia = calculaMedia()

print (f'A média da turma foi {mediaTurma:.2f}')
print (f'A maior média de um aluno foi: {maiorMedia:.2f}', end = '. ')
print (f'Portanto, sua situação é: {verificaAprovacao(maiorMedia)}')
