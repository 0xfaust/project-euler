'''
Project Euler Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Answer: 142913828922
https://projecteuler.net/problem=10
'''

#!/usr/bin/env python3
def primes(x):
    sum, num = 0, [True] * x
    for i in range(2, x):
        if num[i]:
            sum += i
            for j in range(i*i, x, i):
                num[j] = False
    return sum

print (primes(2000000))
