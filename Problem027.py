'''
Project Euler Problem 27: Quadratic Primes

Euler discovered the remarkable quadratic formula:
n² + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.
The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
    n² + an + b, where |a| < 1000 and |b| < 1000
    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

Answer: -59231
https://projecteuler.net/problem=27
'''
#!/usr/bin/python3
def f(n,a,b):
	return n * n + a * n + b

def check(x):
	for i in range(3,x,2):
		if x % i == 0:
			return False
	return True

def make_b(n):
	b_list = range(2,n)
	b = []
	while b_list != []:
		test = b_list[0]
		b.append(b_list[0])
		sub_list = []
		for i in b_list:
			if i % test != 0:
				sub_list.append(i)
		b_list = sub_list[:]
	return b

max_len = 0
b_list = make_b(1000)
max_a = 0
max_b = 0
for a in range(-999,1001,2):
	for b in b_list:
		n = 1
		while f(n,a,b) > 0 and check(f(n,a,b)):
			n += 1
		if n > max_len:
			max_a = a
			max_b = b
			max_len = n
print (max_a*max_b)
