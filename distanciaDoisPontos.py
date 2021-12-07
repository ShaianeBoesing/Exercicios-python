import math

x1,y1 = list(map(float, input().split()))
x2,y2 = list(map(float, input().split()))
Distance = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
print(f'{Distance:0.4f}')
