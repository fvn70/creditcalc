import math


def calc_period(p, a):
    # number of months
    m = math.ceil(p / a)
    y = m // 12
    m -= y * 12
    word = ""
    if y > 0:
        w_year = "years" if y > 1 else "year"
        word += f"{y} {w_year}{' and ' if m > 0 else ''}"
    if m > 0:
        w_month = "months" if m > 1 else "month"
        word += f"{m} {w_month}"
    print(f"It will take {word} to repay the loan")


def calc_payment(p, n):
    month_pay = math.ceil(p / n)
    last_pay = p - month_pay * (n - 1)
    result = "Your monthly payment = " + str(month_pay)
    if last_pay != month_pay:
        result += " and the last payment = " + str(last_pay)
    print(result)


print("Enter the loan principal:")
loan_pay = int(input())
print('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:''')
cmd = input()

if cmd == 'm':
    month_pay = int(input("Enter the monthly payment:\n"))
    calc_period(loan_pay, month_pay)
elif cmd == 'p':
    month_num = int(input("Enter the number of months:\n"))
    calc_payment(loan_pay, month_num)
