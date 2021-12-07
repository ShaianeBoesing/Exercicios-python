ageInDays = int(input())
years = int(ageInDays/365)
ageInDays -= years*365
months = int(ageInDays/30)
ageInDays -= months*30

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{ageInDays} dia(s)')
