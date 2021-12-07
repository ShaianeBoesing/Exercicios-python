exercise = int(input('Exercício: '))

if (exercise == 1):
        housePrice = float(input('Valor da casa: '))
        buyerSalary = float(input('Seu salário: '))
        yearsToPay = float(input('Pagar em quantos anos? '))

        coustPerMonth = housePrice / (yearsToPay*12)

        if (coustPerMonth >= buyerSalary * 0.3):
            print('Empréstimo negado')
        else:
            print(f'Empréstimo aceito: R$ {coustPerMonth:0.2f}/mês')

elif (exercise == 2):
    valor = float(input('Valor do produto: '))
    condicao = input('''Condição de pagamento:
                        a. à vista (dinheiro ou cheque)    - 10% de desconto
                        b. 1x no cartão                    - 5% de desconto
                        c. 2x cartão                       - preço normal
                        d. 3x ou mais no cartão            - 20% de juros
                     ''')
    
    if (condicao == 'a'):
        valor -= valor*0.1
    elif (condicao == 'b'):
           valor -= valor*0.05
    elif (condicao == 'd'):
        valor += valor*0.2
        
    print(f'Valor final: R$ {valor:0.2f}')
    
elif (exercise == 3):
    peso = float(input('peso: '))
    altura = float(input('altura: '))
    
    imc = (peso / altura**2)
    
    if (imc < 18.5):
        print('abaixo do peso: ', round(imc,1))
    elif (imc < 25):
        print('peso ideal: ', round(imc,1))
    elif (imc < 30):
        print('sobrepeso: ', round(imc,1))
    elif (imc < 40):
        print('obesidade: ', round(imc,1))
    else:
        print('obesidade mórbida: ', round(imc,1))
        
    

elif (exercise == 4):
    n1 = int(input('nota 1: '))
    n2 = int(input('nota 2: '))
    n3 = int(input('nota 3: '))
    media = (n1+n2+n3)/3
    
    if (media < 5):
        print ('reprovado: ', round(media,2))
    elif (media < 7):
        print ('em recuperaçao: ', round(media,2))
    else:
        print ('aprovado: ', round(media,2))
        
else:
    print(f'Não há exercício número {exercise}')
        
    