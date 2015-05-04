'''
Project Euler Problem 20: Factorial digit sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Answer: 648
https://projecteuler.net/problem=20
'''
#!/usr/bin/python3
def factorial(num):
    if num == 0: return 1
    else: return num * factorial(num - 1)
 
def sum_digits(num):
    return sum([int(i) for i in str(num)])
 
sum_factorial = sum_digits(factorial(100))
print(sum_factorial)
