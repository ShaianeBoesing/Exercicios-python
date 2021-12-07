salary = float(input())
def calculate(salary):
    if (salary <= 400):
        perc = 15
        increased = salary*0.15
        newSalary = salary + increased
    elif (salary <= 800):
        perc = 12
        increased = salary*0.12
        newSalary = salary + increased
    elif (salary <= 1200):        
        perc = 10
        increased = salary*0.1
        newSalary = salary + increased
    elif (salary <= 2000):
        perc = 7
        increased = salary*0.07
        newSalary = salary + increased
    else:
        perc = 4
        increased = salary*0.04
        newSalary = salary + increased

    print(f"Novo salario: {newSalary:.2f}")
    print(f"Reajuste ganho: {increased:.2f}")
    print(f"Em percentual: {perc} %")

calculate(salary)

