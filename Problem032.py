'''
Project Euler Problem 32: Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

Answer: 45228
https://projecteuler.net/problem=32
'''

#!/usr/bin/python3
def Pandigital(num):
    digits = len(num)

    if digits >= 10:
        return False

    for i in range(1,digits+1):
        if str(i) not in num:
            return False
    return True
def Product(a, b):
    numbers = str(a) + str(b) + str(a*b)
    if len(numbers) != 9:
        return False
    return Pandigital(numbers)
products = []
for i in range(0, 100000):
    for j in range(i, 100000):
        if len(str(i*j) + str(i) + str(j)) > 9:
            break
        if Product(i, j):
            products.append(i*j)
print(sum(set(products)))
