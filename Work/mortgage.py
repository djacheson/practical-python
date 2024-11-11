# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
start_payment = 2684.11
total_paid = 0
total_months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if total_months >= extra_payment_start_month and total_months <= extra_payment_end_month:
        payment = start_payment + extra_payment
    else:
        payment = start_payment
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    total_months += 1
    print(f'{total_months} {round(total_paid,2)} {round(principal,2)}')

print(f'Total paid {round(total_paid,2)}')
print(f'Months {round(total_months,2)}')

