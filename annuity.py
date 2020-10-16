import math

### DEFINE FUNCTIONS
def ask_principal():
    return float(input("Enter the loan principal: "))

def ask_mthly_pay_amt():
    return float(input("Enter the monthly payment: "))

def ask_repay_pd():
    return int(input("Enter the repayment period in months: "))

def ask_interest():
    return float(input("Enter the loan interest: "))

# calculate nominal interest rate, given known interest rate
def calc_nom_irate(interest):
    return (interest/100) / 12

# calculate number of months to repay loan, given known principal and how much you will pay each month
def calc_num_mths(nom_irate, mthly_pay_amt, principal):
    b = 1 + nom_irate
    x = mthly_pay_amt / (mthly_pay_amt - nom_irate * principal)
    return math.ceil(math.log(x, b))

# calculate how much you will pay each month, given known principal and interest rate
def calc_mthly_payment(principal, nom_irate, repay_pd):
    numerator = nom_irate * math.pow((1 + nom_irate), repay_pd)
    denom = math.pow((1 + nom_irate), repay_pd) - 1
    return principal * (numerator / denom)

# calculate loan principal, given loan interest and number of months to pay off
def calc_principal():
    pass

### PROGRAM START
print("""
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
""")
selection = str(input())

if selection == "n":
    principal = ask_principal()
    mthly_pay_amt = ask_mthly_pay_amt()
    interest = ask_interest()

    nom_irate = calc_nom_irate(interest)
    repay_pd = calc_num_mths(nom_irate, mthly_pay_amt, principal)

    num_yrs = math.floor(repay_pd / 12)
    num_mths = (repay_pd / 12) - num_yrs
    
    if repay_pd < 12:
        print(f"It will take {num_mths} months to repay this loan!")
    elif repay_pd % 12 == 0:
        if repay_pd == 12:
            print("It will take 1 year to repay this loan!")
        else:
            print(f"It will take {num_yrs} years to repay this loan!")
    else:
        print(f"It will take {num_yrs} years and {num_mths} months to repay this loan!")

elif selection == "a":
    principal = ask_principal()
    repay_pd = ask_repay_pd()
    interest = ask_interest()
    print("Out of luck!")

elif selection == "p":
    print("Shouldn't you know this?! lololol")



