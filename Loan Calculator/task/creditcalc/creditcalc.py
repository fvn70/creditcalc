import math


def calc_period(lp, mp, rate):
    # interest rate
    i = rate / 12 / 100
    # number of months
    n = math.log(mp / (mp - i * lp), 1 + i)
    m = math.floor(n)
    if n > m:
        m += 1
    y = m // 12
    m -= y * 12
    word = ""
    if y > 0:
        w_year = "years" if y > 1 else "year"
        word += f"{y} {w_year}{' and ' if m > 0 else ''}"
    if m > 0:
        w_month = "months" if m > 1 else "month"
        word += f"{m} {w_month}"
    print(f"It will take {word} to repay this loan!")


def calc_payment(lp, n, rate):
    # interest rate
    i = rate / 12 / 100
    j = (1 + i) ** n
    mp = math.ceil(lp * i * j / (j - 1))
    last_pay = lp - mp * n
    result = "Your monthly payment = " + str(mp)
    if last_pay > 0:
        result += " and the last payment = " + str(last_pay)
    print(result + "!")


def calc_apayment(a, n, rate):
    # interest rate
    i = rate / 12 / 100
    j = (1 + i) ** n
    p = round(a * (j - 1) / (i * j))
    print(f"Your loan principal = {p}!")


print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
cmd = input()

if cmd == 'n':
    print("Enter the loan principal:")
    loan_pay = int(input())
    print("Enter the monthly payment:")
    month_pay = int(input())
    print("Enter the loan interest:")
    rate = float(input())
    calc_period(loan_pay, month_pay, rate)
elif cmd == 'a':
    print("Enter the loan principal:")
    loan_pay = int(input())
    print("Enter the number of periods:")
    m = int(input())
    print("Enter the loan interest:")
    rate = float(input())
    calc_payment(loan_pay, m, rate)
else:
    print("Enter the annuity payment:")
    annu_pay = float(input())
    print("Enter the number of periods:")
    m = int(input())
    print("Enter the loan interest:")
    rate = float(input())
    calc_apayment(annu_pay, m, rate)