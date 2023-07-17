"""
Project Euler: Problem 2
Problem link (specification): https://projecteuler.net/problem=2
Author: Hamish Croser
"""

"""
Returns the sum of all even Fibonacci numbers whose values do not exceed the ceiling.
ceiling: int - the highest Fibonacci number that will be considered.
output_sum: int - the sum of all even Fibonacci numbers whose values do not exceed the ceiling.
"""
def add_even_fibonacci(ceiling):
	output_sum = 0
	prev_fib = [0,1]
	curr_fib = 0
	while curr_fib <= ceiling:
		curr_fib = sum(prev_fib)
		prev_fib = [prev_fib[1],curr_fib]
		# If the current Fibonacci number is even, it is added to the running sum.
		if curr_fib % 2 == 0:
			output_sum += curr_fib
	return output_sum

"""
Called directly by the program. This function calls add_even_fibonacci() with the required argument
as provided in the specification and prints the result.
"""
def main():
	ceiling = 4000000 # four million
	sum = add_even_fibonacci(ceiling)
	print("Sum: {}".format(sum))

import time
start = time.time()
main()
print("Runtime: %.3f seconds" % (time.time() - start))
