
def parOuImpar(numero):
    if (numero%2 == 0):
        return 'Par'
    else:
        return 'Ímpar'
    
   
totalPar = 0;
totalImpar = 0;

for i in range(10):
    numero = int(input('Informe um número inteiro: '))
    resultado = parOuImpar(numero)
    if (resultado == 'Par'):
        totalPar += 1
    else:
        totalImpar += 1
        
print('Total de pares digitados ', totalPar)
print('Total de ímppares digitados ', totalImpar)


