from math import ceil

principal = float(input("Enter the loan principal: "))
print("""
What do you want to calculate?
Enter 'm' to know how many months it will take to pay off the loan.
Enter 'p' to know how much you should pay per month.
""")
selection = input()

if selection == "m":
    mthly_pay_amt = int(input("Enter the monthly payment amount: "))
    mths_to_zero = round(principal / mthly_pay_amt)
    if mths_to_zero == 1:
        print("It will take {} month to repay the loan.".format(mths_to_zero))
    else:
        print("It will take {} months to repay the loan.".format(mths_to_zero))
elif selection == "p":
    num_mths = int(input("Enter the number of months: "))
    proposed_mthly_pay_amt = ceil(principal / num_mths)
    last_payment = int(principal - (num_mths - 1) * proposed_mthly_pay_amt)
    if proposed_mthly_pay_amt == last_payment:
        print("Your monthly payment = {}.".format(proposed_mthly_pay_amt))
    else:
        print("Your monthly payment = {} and the last payment = {}.".format(proposed_mthly_pay_amt, last_payment))