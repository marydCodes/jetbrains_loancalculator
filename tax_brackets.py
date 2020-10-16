# tax brackets
# 0 — 15,527: 0% tax
# 15,528 — 42,707: 15% tax
# 42,708 — 132,406: 25% tax
# 132,407+: 28% tax

income = int(input())

if income <= 15527:
    percent = 0
    calculated_tax = 0
elif income >= 15528 and income <= 42707:
    percent = 15
    calculated_tax = round(income*(percent/100))
elif income >= 42708 and income <= 132406:
    percent = 25
    calculated_tax = round(income*(percent/100))
elif income >= 132407:
    percent = 28
    calculated_tax = round(income*(percent/100))


print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
