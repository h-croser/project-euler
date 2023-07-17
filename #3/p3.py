"""
Project Euler: Problem 3
Problem link (specification): https://projecteuler.net/problem=3
Author: Hamish Croser
"""

"""
Finds the largest prime factor of the target number.
target: int - integer for which the largest prime factor will be found.
"""
def largest_prime_factor(target):
	LPF = 1 # Largest prime factor of the target
	curr = LPF # Current candidate being considered for LPF
	primes = [LPF] # List of primes for prime checking
	# Loops until target is equal to the current candidate, at which point the current candidate will be the LPF
	while curr <= target:
		curr += 1
		curr_is_prime = True
		# Check if curr is a prime
		for p in primes[1:]:
			if curr % p == 0:
				curr_is_prime = False
				break
		# If the current candidate is prime, it is appended to the prime list.
		# If the current candidate is a factor of target, it is set as LPF and target is divided by the candidate.
		if curr_is_prime:
			primes.append(curr)
			while target % curr == 0:
				LPF = curr
				target /= curr
	return LPF

"""
Called directly by the program. This function calls largest_prime_factor() with the required argument
as provided in the specification and prints the result.
"""
def main():
	target = 600851475143 # 600,851,475,143
	LPF = largest_prime_factor(target)
	print("Largest prime factor: {}".format(LPF))

import time
start = time.time()
main()
print("Runtime: %.3f seconds" % (time.time() - start))
