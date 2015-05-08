'''
Project Euler Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Answer: 2783915460
https://projecteuler.net/problem=24
'''
#!/usr/bin/python3
def Permutation(x, y):
    z = len(x)
    if z == 0:
        return []
    num = 1
    for i in range(1, z):
        num *= i
    index = y / num
    res = [x[index]]
    count = y % num
    x.pop(index)
    res += Permutation(x, count)
    return res

buf = '0123456789'
n = 999999
print "".join(Permutation(list(buf), n))
