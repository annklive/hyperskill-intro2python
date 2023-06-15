import math
import argparse

TYPES = ["annuity", "diff"]


def calculate_diff_payment(m, P, n, i):
    return math.ceil(P/n + i * (P - (P*(m-1)/n)))


def calculate_months(P, A, i):
    n = math.ceil(math.log(A / (A - i * P), 1 + i))
    y = n // 12
    m = n % 12
    if y == 0:
        time_to_pay = ''
    else:
        time_to_pay = f'{y} year'
        if y > 1:
            time_to_pay += 's'
    if m > 0:
        time_to_pay += f'{m} month'
    if m > 1:
        time_to_pay += 's'
    print(f'It will take {time_to_pay} to repay this loan!')
    return n


def interest_factor(n, i):
    x = math.pow(1 + i, n)
    return i * x / (x - 1)


def calculate_annuity(P, n, i):
    A = math.ceil(P * interest_factor(n, i))
    print(f"Your monthly payment = {A}!")
    return A

def calculate_principal(A, n, i):
    P = int(A / interest_factor(n, i))
    print(f"Your loan principal = {P}!")
    return P


def check_arguments(args):
    if args.type is None or args.type not in TYPES:
        return False
    elif args.interest is None:
        return False
    elif args.type == "diff":
        if args.payment is not None:
            return False
        if args.principal is None or args.periods is None or args.interest is None:
            return False
    elif args.type == "annuity":
        mode = None
        count = 0
        if args.payment is None:
            mode = 'a'
            count += 1
        if args.principal is None:
            mode = 'p'
            count += 1
        if args.periods is None:
            mode = 'n'
            count += 1

        if count != 1:
            return False
        else:
            return mode

    return True


parser = argparse.ArgumentParser()
parser.add_argument("--type", choices=TYPES,
                    help='indicates the type of payment: "annuity" or "diff" (differentiated)')
parser.add_argument("--payment", type=int, help="the monthly payment amount")
parser.add_argument("--principal", type=int, help="loan principal")
parser.add_argument("--periods", type=int, help="the number of months needed to repay the loan")
parser.add_argument("--interest", type=float, help="annual interest rate")

args = parser.parse_args()

mode = check_arguments(args)

if not mode:
    print("Incorrect parameters")
else:
    nominal_interest = args.interest/1200
    if args.type == "annuity":
        if mode == "n":
            n = calculate_months(args.principal, args.payment, nominal_interest)
            overpaid = args.payment * n - args.principal
        elif mode == "a":
            A = calculate_annuity(args.principal, args.periods, nominal_interest)
            overpaid = A * args.periods - args.principal
        elif mode == "p":
            P = calculate_principal(args.payment, args.periods, nominal_interest)
            overpaid = args.payment * args.periods - P

    else:
        paid = 0
        for m in range(1, args.periods+1):
            D = calculate_diff_payment(m, args.principal, args.periods, nominal_interest)
            print(f"Month {m}: payment is {D}")
            paid += D
        overpaid = paid - args.principal
    
    print(f"\nOverpayment = {overpaid}")
