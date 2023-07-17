"""
Project Euler: Problem 10
Problem link (specification): https://projecteuler.net/problem=10
Author: Hamish Croser
"""

"""
Finds the sum of the primes below ceiling.
ceiling: int - primes below the ceiling will be added to the sum.
prime_sum: int - the sum of all primes below ceiling.
"""
def sum_of_primes(ceiling):
	curr = 3
	primes = [2]
	while curr < ceiling:
		is_prime = True
		for p in primes:
			if p > curr**0.5:
				break
			if curr % p == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(curr)
		curr += 2
	prime_sum = sum(primes)
	return prime_sum

"""
Called directly by the program. This function calls sum_of_primes() with the required argument
as provided in the specification and prints the result.
"""
def main():
	ceiling = 2000000 # 2,000,000
	sum = sum_of_primes(ceiling)
	print("Sum: {}".format(sum))

import time
start = time.time()
main()
print("Runtime: %.3f seconds" % (time.time() - start))
