'''
Project Euler Problem 31: Coin sums

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

Answer: 73682
https://projecteuler.net/problem=31
'''

#!/usr/bin/python3
def coins(x, y):
    num = [1]
    for i in range(0, len(y)):
        for j in range(x + 1):
            if len(num) <= j:
                num.append(0)
            if j >= y[i]:
                num[j] += num[j - y[i]]

    return num[x]
ans = coins(200, [1, 2, 5, 10, 20, 50, 100, 200])
print (ans)
