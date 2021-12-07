exercicio = int(input(''' 1: for
 2: while
 3: media
 qual deseja visualizar:'''))

if (exercicio == 1):
    numero = int(input('Quero calcular o fatorial de: '))
    result = numero
    for numero in range (numero, 1, -1):
        result =  result * (numero - 1)
        

    print(f'O fatorial é {result}')


elif (exercicio == 2):
    
    numero = int(input('Quero calcular o fatorial de: '))
    result = numero
    while (numero > 1):
        result =  result * (numero - 1)
        numero -= 1

    print(f'O fatorial é {result}')
    
elif (exercicio == 3):
    soma = 0;
    maior = 0;
    menor = 0;
    contador = 0;
    while True:

        numero = int(input('informe um numero: '))
        soma += numero
        
        contador += 1
        if (contador == 1):
            maior = numero
            menor = numero

        if (numero > maior):
            maior = numero
            
        if (numero < menor):
            menor = numero
        
        continuar = input('Deseja continuar? y/n: ')
        
        if (continuar == 'n'):
            break;
        
    
    media = numero/contador
    print(f'A média é: {media:0.2f}')
    print(f'O maior numero digitado foi: {maior}')
    print(f'O menor numero digitado foi: {menor}')
    
    