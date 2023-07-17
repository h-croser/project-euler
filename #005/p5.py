"""
Project Euler: Problem 5
Problem link (specification): https://projecteuler.net/problem=5
Author: Hamish Croser
"""

"""
Finds the smallest number that can be divided by each of the numbers from 1 to ceiling without any remainder.
ceiling: int - largest number to be checked for even division.
candidate: int - the number found to be the smallest multiple of all numbers up to ceiling
"""
def smallest_divisible(ceiling):
	candidate = ceiling
	coprimes = find_coprimes(ceiling)
	while True:
		divisible = True
		for i in coprimes:
			if candidate % i != 0:
				divisible = False
				break
		if divisible:
			return candidate
		candidate += 1

"""
Finds a list of coprimes from 2 to the ceiling (inclusive) in order to minimize iteration time.
ceiling: int - the largest potential coprime in the return list
coprimes: list of ints - the list of coprimes to be returned
"""
def find_coprimes(ceiling):
	potentials = [i for i in range(ceiling,1,-1)]
	excluded = []
	for x in potentials:
		for y in range(x-1,1,-1):
			if x % y == 0 and y not in excluded:
				excluded.append(y)
	coprimes = [i for i in potentials if i not in excluded]
	return coprimes

"""
Called directly by the program. This function calls smallest_divisible() with the required argument
as provided in the specification and prints the result.
"""
def main():
	ceiling = 20
	smallest = smallest_divisible(ceiling)
	print("Smallest evenly divisible: {}".format(smallest))

import time
start = time.time()
main()
print("Runtime: %.3f seconds" % (time.time() - start))
