def limiteElevador(N, C):
    count = N
    exc = 0
    while count:
        if( N > C ):
            exc = 0


        S, E = input('Saídas e Entradas: ').split()
        S = int(S)
        E = int(E)
        
        N = N - S
        N = N + E
        #print('No elevador agora estão ', N, ' pessoas')
        count -= 1
        
    if exc:
        print('S')
    else:
        print('N')
  
  
N, C = input('Quantos Entraram? Qual a capacidade do elevador?').split()
limiteElevador (int(N), int(C))
