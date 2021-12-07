X = int(input('Informe um número: '))
count = 0
def ultrapassarX(X):
    soma = X
    Z = X - 1

    while (Z < X):
        Z = int(input('Informe outro número: '))
    else:
        count = 1
        while (soma <= Z):
            X += 1;
            soma += X
            count += 1
        else:
            print(count)

ultrapassarX(X)
