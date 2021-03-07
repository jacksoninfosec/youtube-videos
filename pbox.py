# n is the number of bits
# P is a list of integers of length m
# The integers in P are between 1 and n
# The input x is a n-bit integer
# The output y is a m-bit integer
def pbox(x, P, n):
	y = 0
	for i in P:
		y <<= 1
		y ^= (x >> (n - i)) & 1
	return y

#--------------------------------------

# Initial Permutation of DES
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17,  9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

x = int('123456ABCD132536', 16)
y = pbox(x, IP, 64)

z = int('14A7D67818CA18AD', 16)
if y == z:
	print("It works!")

