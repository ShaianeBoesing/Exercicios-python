def retornaPrimos (min, max):
    totalPrimos = 0
    if (min == 1):
        min = 2
        
    for i in range(min, max+1):
        primo = True
        for p in range (2, (int(i/2))+1):
            if (i%p == 0):
                primo = False
                break
            
        if(primo):
            totalPrimos += 1
    
    return totalPrimos
    

min, max = input('Informe o intervalo de números primos que vc deseja ver! (ex: "1 20" para um intervalo de 1 a 20: ').split()
min = int(min)
max = int(max)
totalPrimo = retornaPrimos(min, max)
print(totalPrimo)