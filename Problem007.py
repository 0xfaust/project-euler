'''
Project Euler Problem 7: 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

Answer: 104743
https://projecteuler.net/problem=7
'''
#!/usr/bin/env python3
def isPrime(num):

  i = 2
  while ((i * i) <= num):
    if (num % i == 0 and num != i):
      return False
      
    i = i+1

  return True

def findPrime(num):
  x = 1
  i = 0

  while (i < num):
    x = x+1

    if (isPrime(x) == True):
      i = i+1
      
  return x

print (findPrime(10001))
