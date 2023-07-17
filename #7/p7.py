"""
Project Euler: Problem 7
Problem link (specification): https://projecteuler.net/problem=7
Author: Hamish Croser
"""

"""
Finds the nth prime as given by n using the Sieve of Eratosthenes.
n: int - the order of prime the function is to return. If n is 6, the function will return the 6th prime.
prime_n: int - the nth prime.
"""
def find_nth_prime(n):
	first = 2
	primes = [first]
	candidate = 3
	while len(primes) < n:
		is_prime = True
		for p in primes:
			if p > candidate**0.5:
				break
			if candidate % p == 0:
				is_prime = False
				break
		if is_prime:
			primes.append(candidate)
		candidate += 2
	prime_n = primes[-1]
	return prime_n

"""
Called directly by the program. This function calls find_nth_prime() with the required argument
as provided in the specification and prints the result.
"""
def main():
	n = 10001
	prime = find_nth_prime(n)
	print("Prime: {}".format(prime))

import time
start = time.time()
main()
print("Runtime: %.3f seconds" % (time.time() - start))
