time = int(input())
avgSpeed = int(input())

km = avgSpeed * time
litersSpent = km / 12

print(f'{litersSpent:0.3f}')