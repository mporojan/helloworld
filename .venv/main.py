print("Hello World2")

salary = float(input("Enter salary: "))
income_tax = 0

if (salary <= 1000):
    income_tax = 0.10
elif (salary <= 2000):
    income_tax = 0.12
elif (salary <= 4000):
    income_tax = 0.14
elif (salary > 4000):
    income_tax = 0.18

tax = salary * income_tax

kids = float(input("Enter kids: "))

while (kids != 0):
    if (salary <= 2000):
        tax *= 0.99
    elif (salary > 2000):
        tax *= 0.995
    kids -=1

net = salary - tax

print(net)