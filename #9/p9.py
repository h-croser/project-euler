"""
Project Euler: Problem 9
Problem link (specification): https://projecteuler.net/problem=9
Author: Hamish Croser
"""

"""
Finds the product of the pythagorean triad that adds to the add_target.
add_target: int - the value for which the pythagorean triad must add to.
product: int - the product of a,b and c where a^2 + b^2 = c^2 and a + b + c = add_target.
"""
def find_pythagorean(add_target):
	a = 1
	b = 2
	c = add_target - a - b
	product = 0
	while b < add_target/2:
		for i in range(1,b):
			a = i
			c = add_target - a - b
			if (a**2 + b**2) == c**2:
				product = a*b*c
		b += 1
	return product

"""
Called directly by the program. This function calls find_pythagorean() with the required argument
as provided in the specification and prints the result.
"""
def main():
	add_target = 1000
	product = find_pythagorean(add_target)
	print("Product: {}".format(product))

import time
start = time.time()
main()
print("Runtime: %.3f seconds" % (time.time() - start))
