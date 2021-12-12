nElementos = int(input('Informe quantos elementos deseja informar: '))
listaNumeros = []
for i in range(nElementos):
    listaNumeros.append(int(input(f'{i+1}º número:')))
    
multiplicador = int(input('Informe o multiplicador: '))
listaNumeros = [num * multiplicador for num in listaNumeros]

print(listaNumeros)