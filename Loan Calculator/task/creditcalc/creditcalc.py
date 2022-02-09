import argparse
import math
import sys


def calc_period(lp, mp, rate):
    # interest rate
    i = rate / 12 / 100
    # number of months
    n = math.log(mp / (mp - i * lp), 1 + i)
    m = math.floor(n)
    if n > m:
        m += 1
    n = m
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
    print(f"Overpayment = {mp * n - lp}")


def calc_annual_payment(p, n, per):
    # interest rate
    i = per / 12 / 100
    j = (1 + i) ** n
    a = math.ceil(p * i * j / (j - 1))
    last_pay = p - a * n
    result = "Your monthly payment = " + str(a)
    if last_pay > 0:
        result += " and the last payment = " + str(last_pay)
    print(result + "!")
    print(f"Overpayment = {a * n - p}")


def calc_loan_payment(a, n, per):
    # interest rate
    i = per / 12 / 100
    j = (1 + i) ** n
    p = math.floor(a * (j - 1) / (i * j))
    print(f"Your loan principal = {p}!")
    print(f"Overpayment = {a * n - p}")


def calc_diff_payment(p, n, per):
    # interest rate
    i = per / 1200
    p1 = p / n
    s = 0
    for m in range(n):
        d = math.ceil(p1 * (1 + i * (n - m)))
        s += d
        print(f"Month {m + 1}: payment is {d}")
    print(f"Overpayment = {s - p}")


while True:
    args = sys.argv
    num_arg = len(args)

    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=["diff", "annuity"])
    parser.add_argument("--principal")
    parser.add_argument("--payment")
    parser.add_argument("--periods")
    parser.add_argument("--interest")

    args = parser.parse_args()

    principal = 0 if args.principal is None else int(args.principal)
    payment = 0 if args.payment is None else int(args.payment)
    periods = 0 if args.periods is None else int(args.periods)
    interest = 0.0 if args.interest is None else float(args.interest)

    if num_arg < 5 or principal < 0 or payment < 0 or periods < 0 or interest < 0:
        print("Incorrect parameters.")
        break
    if args.type not in ["diff", "annuity"]:
        print("Incorrect parameters.")
        break
    if args.type == "diff":
        calc_diff_payment(principal, periods, interest)
    else:
        if payment == 0:
            calc_annual_payment(principal, periods, interest)
        if principal == 0:
            calc_loan_payment(payment, periods, interest)
        if periods == 0:
            calc_period(principal, payment, interest)
    break

