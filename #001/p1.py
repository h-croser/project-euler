"""
Project Euler: Problem 1
Problem link (specification): https://projecteuler.net/problem=1
Author: Hamish Croser
"""

"""
Finds the sum of all multiples of divisors below ceiling.
divisors: list of ints - the output of the function is the sum of the multiples of the numbers within this list
ceiling: int - only multiples below this number will be added
output_sum: int - the sum of all multiples of divisors below ceiling
"""
def sum_multiples(divisors, ceiling):
	output_sum = 0
	# Loop through all integers below the ceiling. If the int is a multiple, add it to the running sum and break the
	# inner loop to prevent doubling up.
	for i in range(ceiling):
		for div in divisors:
			if i % div == 0:
				output_sum += i
				break
	return output_sum

"""
Called directly by the program. This function calls sum_multiples() with required arguments as provided
in the specification and prints the result.
"""
def main():
	divisors = [3,5]
	ceiling = 1000
	sum = sum_multiples(divisors, ceiling)
	print("Sum: {}".format(sum))

import time
start = time.time()
main()
print("Runtime: %.3f seconds" % (time.time() - start))
