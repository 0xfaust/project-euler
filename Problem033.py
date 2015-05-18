'''
Project Euler Problem 33: Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

Answer: 100
https://projecteuler.net/problem=33
'''
#!/usr/bin/python3
fractions = []
def common(a, b):
    count = 0
    num = 0
    for i in a:
        for j in b:
            if i == j:
                count += 1
                num = i
    if count == 1:
        return num
    return False

for numerator in range(10, 100):
    for denominator in range(numerator + 1, 100):
        n = sorted([int(x) for x in str(numerator)])
        d = sorted([int(x) for x in str(denominator)])
        num = common(n, d)
        if num:
            n.remove(num)
            d.remove(num)
            n_rem = n[0]
            d_rem = d[0]
            if 0 not in n and 0 not in d:
                if float(numerator) / denominator == float(n_rem) / d_rem:
                    fractions.append([numerator, denominator])        
product = [1, 1]
for frac in fractions:
    product[0] *= frac[0]
    product[1] *= frac[1]

ans = product[1] // product[0]
print (ans)
