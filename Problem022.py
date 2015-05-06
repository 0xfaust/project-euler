'''
Project Euler Problem 22: Number Scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?

names.txt can be downloaded here: https://projecteuler.net/project/resources/p022_names.txt
Answer: 871198282
https://projecteuler.net/problem=22
'''
#!/usr/bin/python3
f = open('names.txt', 'rU')
names = []
 
names = sorted(f.read().replace('"', '').split(','), key=str)
 
dmap = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10, \
        'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19, \
        'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
 
def letter_counter(letter):
    counter = dmap[letter]
    return counter
    
lenght = len(names)
num = 0
for i in range(0,(lenght)):
    x = 0
    y = 0
    for letter in names[i]:
        lenght = letter_counter(letter)
        x = x + lenght
    y = x * (i + 1)
    num = num + y
print (num)
