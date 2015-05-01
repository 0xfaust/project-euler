'''
Project Euler Problem 17: Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

Answer: 21124
https://projecteuler.net/problem=17
'''
#!/usr/bin/python3
singles = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,3,6,6,5,5,5,7,6,6]
hundreds = 7
thousands = 8
 
total = 0
for i in range(1,1000):
    c = i % 10
    b = ((i % 100) - c) // 10
    a = ((i % 1000) - (b * 10) - c) // 100
    if a != 0:
        total += singles[a] + hundreds
        if b != 0 or c != 0: total += 3
    if b == 0 or b == 1: total += singles[b * 10 + c]
    else: total += tens[b] + singles[c]
 
total += singles[1] + thousands
print (total)
