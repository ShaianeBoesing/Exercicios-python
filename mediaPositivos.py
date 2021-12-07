def positivesAverage():
    pos = 0
    sum = 0
    for i in range(6):
        num = float(input('Informe um número: '))
        if (num > 0):
            pos += 1
            sum += num
    
    
    media = sum / pos
    print(f"{pos} valores positivos")
    print(f"{media:0.1f}")
    
positivesAverage()