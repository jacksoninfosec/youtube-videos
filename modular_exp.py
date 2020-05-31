
def mod_power(a, n, m):
	r = 1
	while n > 0:
		if n & 1 == 1:
			r = (r * a) % m
		a = (a * a) % m
		n >>= 1
	return r