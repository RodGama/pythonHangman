income = int(input())
percent = 0.0
calculated_tax = 0
if income >= 132407:
    percent = 28
elif 42708 <= income <= 132407:
    percent = 25
elif income >= 15528:
    percent = 15
else:
    percent = 0

if percent != 0:
    calculated_tax = int(round(income * percent/100))

print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
