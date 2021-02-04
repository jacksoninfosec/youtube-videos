# Implementation of the Tonelli-Shanks algoritm as described at:
# https://en.wikipedia.org/wiki/Tonelli-Shanks_algorithm



# Determines if n is a quadratic residue of an
# odd prime p by using Euler's criterion.
def is_quadratic_residue(n,p):
	if n % p == 0:
		return True
	return pow(n, (p - 1)//2, p) == 1


# Given an odd prime p and integer n, this is an algorithm to
# find a mod-p square root of n when possible
def tonelli_shanks(n, p):
	# Case when p|n, so n=0(mod p). The square root of 0 is 0.
	if n % p == 0:
		return 0

	# So assume n is coprime to p.
	# Use Eulers criteria to see if n is a quadratic residue.
	if not is_quadratic_residue(n, p):
		print("This value of n is not a quadratic residue.")
		return None
	else:
		print("This value of n is a quadratic residue.")

	# If p=3(mod 4) and since we know that n is a quadratic residue
	# we can get the square root right now and be done.
	if p % 4 == 3:
		return pow(n, (p + 1)//4, p)

	# So now p=1(mod 4) but this is not used in the algorithm.
	# Write p - 1 = (2^S)Q, where Q is odd
	Q = p - 1
	S = 0
	while Q % 2 == 0:
		S += 1
		Q //= 2
	print("Q=", Q)
	print("S=", S)

	# Find a quadratic non-residue of p by brute force search
	z = 2
	while is_quadratic_residue(z, p):
		z += 1
	print("z=", z)

	# Initialize variables
	M = S
	c = pow(z, Q, p)
	t = pow(n, Q, p)
	R = pow(n, (Q + 1)//2, p)

	print("M=", M)
	print("c=", c)
	print("t=", t)
	print("R=", R)

	while t != 1:
		print("Loop")

		# Calculate i
		i = 0
		temp = t
		while temp != 1:
			i += 1
			temp = (temp * temp) % p
		print("i=", i)

		# Calculate b, M, c, t, R
		pow2 = 2 ** (M - i - 1)
		b = pow(c, pow2, p)
		M = i
		c = (b * b) % p
		t = (t * b * b) % p
		R = (R * b) % p
		print("b=", b)
		print("M=", M)
		print("c=", c)
		print("t=", t)
		print("R=", R)

	# We have found a square root
	return R

# Test
# print(tonelli_shanks(5, 41))

#---------------------------------------------------------------
# This is an application of the Tonelli Shanks 

# Given an elliptic curve specified by p, a, b and given an
# x-value this function calculates when possible a corresponding
# y-value such that (x,y) is on the elliptic curve.
def get_y_value_elliptic_curve(p, a, b, x):
	n = (x * x * x + a * x + b) % p
	# We want to solve y^2=n
	# The Tonelli-Shanks algorithm will give us this value (if it exists)
	return tonelli_shanks(n, p)


# The Eliiptic Curve P-224
# https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf
p = 26959946667150639794667015087019630673557916260026308143510066298881
a = -3
b = int('b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4', 16)
x = 2021 # Can make up any number for x
y = get_y_value_elliptic_curve(p, a, b, x)
print(y)

# Check that the point is indeed on the elliptic curve
print(((y * y) - (x * x * x + a * x + b)) % p)  # should be 0
