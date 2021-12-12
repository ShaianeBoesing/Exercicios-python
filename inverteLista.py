X = []
for i in range (20):
    X.append(input(f'Elemento {i+1}: '))
    
X = X[::-1]
print(X)