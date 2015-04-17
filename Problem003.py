'''
Project Euler Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

Answer: 6857
https://projecteuler.net/problem=3
'''
#!/usr/bin/env python3
num = 600851475143  
i = 2  

while i * i < num:  
	while num % i == 0:  
		num = num / i  
	i = i + 1
	
print(num) 
