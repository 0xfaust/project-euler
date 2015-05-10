'''
Project Euler Problem 26: Reciprocal cycles

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

Answer: 983
https://projecteuler.net/problem=26
'''
#!/usr/bin/python3
def reciprocal_cycle(x, y):
    for i in range(1, y):
        if 1 == 10**i % y:
            return i
    return 0

longest = max(reciprocal_cycle(1, i) for i in range(2,1001))
print ([i for i in range(2,1001) if reciprocal_cycle(1, i) == longest][0])
