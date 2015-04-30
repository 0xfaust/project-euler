'''
Project Euler Problem 16: Power digit sum

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

Answer: 1366
https://projecteuler.net/problem=16
'''
#!/usr/bin/python3
def power_sum(exp):
   pow = list(str(2**1000))
   return sum([int(i) for i in pow])

num = power_sum(1000)
print (num)
