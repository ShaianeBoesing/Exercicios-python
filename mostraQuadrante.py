def mostraQuadrante(X, Y):
    if (X > 0):
        if (Y > 0):
            quad = 'primeiro'
        else:
            quad = 'quarto'
    else:
        if (Y > 0):
            quad = 'segundo'
        else:
            quad = 'terceiro'
    print(quad)    
    
while True:
    X, Y = input('Informe X e Y com um espaço entre eles: ').split(' ')
    if not X or not Y:
        break

    X = int(X)
    Y = int(Y)
    mostraQuadrante(X, Y)