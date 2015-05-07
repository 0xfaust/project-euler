'''
Project Euler Problem 23: Non-abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Answer: 4179871
https://projecteuler.net/problem=23
'''
#!/usr/bin/python3
def sum_divisors(num):
  if num == 1:
    return 1
  top = num
  sum = 1
  i = 2
  while i < top:
    if (num % i) == 0:
      top = num / i
      sum += i
      if top > i:
        sum += top
    i += 1
  return sum

def abundant_test(num):
  if num < 12:
    return False
  elif sum_divisors(num) > num:
    return True
  return False

abundant = [x for x in range(12, 28124) if sum_divisors(x) > x]

soa = {}

for x in abundant:
  for y in abundant:
    summ = x + y
    soa[summ] = summ

def sum_abundant(num):
  if num < 24:
    return False
  if num > 28123:
    return True
  global soa
  if num in soa:
    return True
  else:
    return False

ans = 0

for x in range(1, 28124):
  if not sum_abundant(x):
    ans += x

print (ans)
