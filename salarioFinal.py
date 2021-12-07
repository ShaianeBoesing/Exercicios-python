employeeNumber = int(input())
workedHours = float(input())
amountPerHour = float(input())

SALARY = workedHours*amountPerHour
print('NUMBER =', employeeNumber)
print(f'SALARY = U$ {SALARY:.2f}')