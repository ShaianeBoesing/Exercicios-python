N = int(input())

hours = N // 3600
N -= hours*3600
minutes = N // 60
seconds = N - minutes*60 

print(f'{hours}:{minutes}:{seconds}')
