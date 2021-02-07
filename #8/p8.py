"""
Project Euler: Problem 8
Problem link (specification): https://projecteuler.net/problem=8
Author: Hamish Croser
"""

"""
Finds the greatest product of seq_length number of adjacent digits in the number given by the digits parameter.
digits: int - the number to be iterated through and the source of the product factors. Will be converted to a list in
this function.
seq_length: int - the length of the sequence of digits to be considered for greatest product.
greatest_product: int - the largest product that can be produced by seq_length number of adjacent digits in the number
given by the digits parameter.
"""
def greatest_product(digits,seq_length):
	greatest_product = 0
	greatest_idx = 0
	dig_list = [int(i) for i in str(digits)]
	for i in range(0,len(dig_list)-12):
		product = 1
		for j in range(i,i+seq_length):
			product *= dig_list[j]
		if product > greatest_product:
			greatest_product = product
			greatest_idx = i
	return greatest_product

"""
Called directly by the program. This function calls greatest_product() with the required arguments
as provided in the specification and prints the result.
"""
def main():
	digits = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
	seq_length = 13
	product = greatest_product(digits,seq_length)
	print("Greatest product: {}".format(product))

import time
start = time.time()
main()
print("Runtime: %.3f seconds" % (time.time() - start))
