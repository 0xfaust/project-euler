'''
Project Euler Problem 34: Digit factorials

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Answer: 40730
https://projecteuler.net/problem=34
'''
#!/usr/bin/python3

factorials = [1, 1]
for i in range(2, 10):
    factorials.append(i * factorials[-1])

def factorion_sum(num, factorial_sum):
    num *= 10
    total = 0
    for digit in range(10):
        new = num + digit
        new_sum = factorial_sum + factorials[digit]
        if new == new_sum:
            total += new
        if new*10 <= new_sum + factorials[-1]:
            total += factorion_sum(new, new_sum)
    return total

print (sum(factorion_sum(i, factorials[i]) for i in range(1, 10)))
