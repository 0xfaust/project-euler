'''
Project Euler Problem 28: Number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Answer: 669171001
https://projecteuler.net/problem=28
'''
#!/usr/bin/python3
def spiral_diagonals(x):
    if x < 1: return 0
    elif x == 1: return 1
    elif x % 2 == 0: return 0
    else:
        num = [1]
        while len(num) < (2*x - 1):
            inc = int(len(num) * 0.5 + 1.5)
            for i in range(4):
                num.append(num[-1] + inc)     
    return sum(num)

ans = spiral_diagonals(1001)
print (ans)
