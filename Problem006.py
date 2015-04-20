'''
Project Euler Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,
		12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
	(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer: 25164150
https://projecteuler.net/problem=6
'''
#!/usr/bin/env python3
num = 100
x = num*(num + 1)/2
y = num*(num + 1)*(2*num + 1)/6
a = x*x - y
print (a)
