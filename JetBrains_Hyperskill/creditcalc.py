import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str, choices=["diff", "annuity"])
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)

args = parser.parse_args()
pass1 = 'ppp'

if args.type == None:
    print('Incorrect parameters')
    exit()
else:
    if args.type == 'diff':
        if args.principal == None or args.periods == None or args.interest == None:
            print('Incorrect parameters')
            exit()
    elif args.type == 'annuity':
        if args.principal != None and args.periods != None and args.interest != None:
            pass1 = 'pri'
        elif args.principal != None and args.payment != None and args.interest != None:
            pass1 = 'pyi'
        elif args.periods != None and args.payment != None and args.interest != None:
            pass1 = 'yri'
        else:
            print('Incorrect parameters')
            exit()

    if args.principal != None and args.principal < 0:
        print('Incorrect parameters')
        exit()
    if args.interest != None and args.interest < 0:
        print('Incorrect parameters')
        exit()
    if args.periods != None and args.periods < 0:
        print('Incorrect parameters')
        exit()
    if args.payment != None and args.payment < 0:
        print('Incorrect parameters')
        exit()

t = args.type
p = args.principal
r = args.periods
i = args.interest / 1200
y = args.payment

def diff_months(n, m):
    return math.ceil(p / n + i * (p - p * (m - 1) / n))

if t == 'diff':
    sums = 0
    for x in range(r):
        payment = diff_months(r, x + 1)
        print(f'Month {x + 1}: payment is {payment}')
        sums += payment
    print()
    print(f'Overpayment = {sums - p}')

def calc_monthly_payment(p1, r1, i1):
    a1 = p1 * i1 * math.pow((1 + i1), r1) / (math.pow((1 + i1), r1) - 1)
    return math.ceil(a1)

def calc_loan_principal(a1, r1, i1):
    p1 = a1 / (i1 * math.pow((1 + i1), r1) / (math.pow((1 + i1), r1) - 1))
    return p1

def calc_loan_duration(p1, a1, i1):
    n1 = math.log(a1 / (a1 - i1 * p1), 1 + i1)
    return n1

if t == 'annuity':
    if pass1 == 'pri':
        payment = calc_monthly_payment(p, r, i)
        print(f'Your annuity payment = {payment}!')
        print(f'Overpayment = {payment * r - p}')
    elif pass1 == 'yri':
        payment = calc_loan_principal(y, r, i)
        print(f'Your loan principal = {math.floor(payment)}!')
        print(f'Overpayment = {math.ceil(y * r - payment)}')
    elif pass1 == 'pyi':
        t = calc_loan_duration(p, y, i)
        year = int(t // 12)
        s = math.ceil(t - year * 12)
        if s == 12:
            year += 1
            s = 0
        if s == 0:
            print(f'It will take {year} years to repay this loan!')
        else:
            print(f'It will take {year} years and {s} months to repay this loan!')
        print(f'Overpayment = {(year * 12 + s) * y - p}')
        
