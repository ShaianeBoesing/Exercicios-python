numero = int(input('Quantos números da sequência de Fibonacci desejas ver? '))
val1 = 0
val2 = 1
seq = 0
while (numero >= 1):
    seq = val1
    if (numero > 1):
        print(seq, end=' - ')
    else:
        print (seq)
    
    seq = val1 + val2
    val1 = val2
    val2 = seq
    numero -= 1