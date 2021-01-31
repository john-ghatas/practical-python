#!/bin/python

# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

month_extra_start = 61
month_extra_end = 108
extra_payment = 1000

while principal > 0:
    if month_extra_start <= month <= month_extra_end:
        payment_temp = payment + extra_payment
    else:
        payment_temp = payment
    
    test_principal = principal * (1+rate/12) - payment_temp
    
    if test_principal < 0:
        payment_temp = principal * (1+rate/12)

    principal = principal * (1+rate/12) - payment_temp
    total_paid = total_paid + payment_temp
    print(f'{month} {total_paid} {principal}')
    month += 1

print('Total paid', total_paid)
