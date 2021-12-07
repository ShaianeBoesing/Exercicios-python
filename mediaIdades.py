age = int(input('Informe uma idade: '))

def mediaIdades(idade):
    sum = 0
    count = 0
    while True:
        age = idade
        if (age >= 0):
            sum += age
            count += 1
        else:
            break

        idade = int(input('Informe uma idade: '))

    print (f'Média das idades: {sum/count:.2f}')


mediaIdades(age)