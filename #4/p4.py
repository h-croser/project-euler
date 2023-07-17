"""
Project Euler: Problem 4
Problem link (specification): https://projecteuler.net/problem=4
Author: Hamish Croser
"""

"""
Finds the largest palindrome made from the product of two numbers within the scope
scope: list of int - only numbers between the given values (inclusive) will be considered as factors
largest: int - largest palindrome made from the product of two numbers within the scope
"""
def largest_palindrome(scope):
	palindromes = []
	for i in range(scope[0],scope[1]+1):
		for j in range(scope[0],scope[1]+1):
			if is_palindrome(i*j):
				palindromes.append(i*j)
	palindromes.sort()
	largest = palindromes[-1]
	return largest

"""
Checks if the given candidate is a palindrome
candidate: int - the number that will be checked
is_palindrome: boolean - will return True if the candidate is a palindrome
"""
def is_palindrome(candidate):
	str_cand = str(candidate)
	is_palindrome = str_cand == str_cand[::-1]
	return is_palindrome

"""
Called directly by the program. This function calls largest_palindrome() with the required argument
as provided in the specification and prints the result.
"""
def main():
	scope = [100,999]
	largest = largest_palindrome(scope)
	print("Largest palindrome: {}".format(largest))

import time
start = time.time()
main()
print("Runtime: %.3f seconds" % (time.time() - start))
