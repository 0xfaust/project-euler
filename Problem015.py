'''
Project Euler Problem 15: Lattice paths

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

Link to image: http://projecteuler.net/project/images/p015.gif

How many such routes are there through a 20×20 grid?

Answer: 137846528820
https://projecteuler.net/problem=15
'''
#!/usr/bin/python3

def path(grid):
	x = [1] * grid
	for i in range(grid):
		for j in range(i):
			x[j] = x[j]+x[j-1]
		x[i] = 2 * x[i-1]
	return x[grid -1]
ans = path(20)
print(ans)
