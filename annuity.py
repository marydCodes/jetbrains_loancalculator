import math

def ask_principal():
    return float(input("Enter the loan principal: "))

def ask_mthly_paymt():
    return float(input("Enter monthly payment: "))

def ask_repay_pd():
    return float(input("Enter the number of periods: "))

def ask_interest():
    return float(input("Enter the loan interest: ")) / 12 / 100

def annu():
    principal = ask_principal()
    repay_pd = ask_repay_pd()
    inte = ask_interest()
    
    result = math.ceil(((principal * inte * math.pow(1 + inte, repay_pd)) / (math.pow(1 + inte, repay_pd) - 1)))
    
    print(f'Your monthly payment = {result}!')

def num_month():
    principal = ask_principal()
    paym = ask_mthly_paymt()
    inte = ask_interest()
    
    box = paym / (paym - inte * principal)
    result = math.ceil(math.log(box, 1 + inte))
    times = divmod(result, 12)
    
    if result < 12:
        print(f'It will take {result} months to repay this loan')
    elif result == 12:
        print(f'It will take 1 year to repay this loan')
    elif times[1] == 0:
        print(f'It will take {times[0]} years to repay this loan')
    else:
        print(f'It will take {times[0]} years and {times[1]} months to repay this loan')
    
def loan_prince():
    print('Enter the annuity payment:')
    anus = float(input())
    repay_pd = ask_repay_pd()
    inte = ask_interest()
    
    box1 = inte * math.pow(1 + inte, repay_pd)
    box2 = math.pow(1 + inte, repay_pd) - 1
    box = box1 / box2
    result = round(anus / box)
    
    print(f'Your loan principal = {result}!')
    
# START PROGRAMME
print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')

menu = input()
if menu == 'n':
    num_month()
elif menu == 'p':
    loan_prince()
elif menu == 'a':
    annu()