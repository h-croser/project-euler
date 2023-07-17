"""
Project Euler: Problem 6
Problem link (specification): https://projecteuler.net/problem=6
Author: Hamish Croser
"""

"""
Finds the absolute difference between the sum of the squares and the square of the sum of
the natural numbers up to the ceiling.
ceiling: int - the largest natural number included in the sum and the squares.
diff: int - the absolute difference between the sum of the squares and the square of the sum
"""
def sum_square_diff(ceiling):
	sum_of_squares = sum([i**2 for i in range(ceiling+1)])
	square_of_sum = (sum([i for i in range(ceiling+1)]))**2
	diff = abs(sum_of_squares - square_of_sum)
	return diff

"""
Called directly by the program. This function calls sum_square_diff() with the required argument
as provided in the specification and prints the result.
"""
def main():
	ceiling = 100
	diff = sum_square_diff(ceiling)
	print("Difference between sum of squares and square of sum: {}".format(diff))

import time
start = time.time()
main()
print("Runtime: %.3f seconds" % (time.time() - start))
