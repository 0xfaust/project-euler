'''
Project Euler Problem 30: Digit fifth powers

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
    1634 = 14 + 64 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

Answer: 443839
https://projecteuler.net/problem=30
'''
#!/usr/bin/python3
def powers(x):
    def power(num):
        return int(num) ** x
    if x <= 1:
        return 0
    else:
        total_sum = 0
        upper = (x + 1) * (9 ** x)
        for num in range(10, upper + 1):
            digits = [i for i in str(num)]
            if num == sum(map(power, digits)):
                total_sum += num
        return total_sum

ans = powers(5)

print (ans)
