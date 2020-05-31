import random


# If False is returned then it is False that n is prime
# If True is returned then it is probably True that n is prime
def miller_rabin(n, k):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def binary_digits_to_integer(B):
    n = 0
    pow2 = 1
    for i in reversed(range(len(B))):
        n += pow2 * B[i]
        pow2 *= 2
    return n



def random_odd_value(bits):
    B = [0] * bits
    B[0] = 1
    B[-1] = 1
    for i in range(1, bits-1):
        B[i] = random.randint(0, 1)
    return binary_digits_to_integer(B)



def generate_probable_prime(bits):
    while True:
        n = random_odd_value(bits)
        if miller_rabin(n, 40):
            print(n)
            break



def random_odd_value2(bits):
    n = random.randint(2 ** (bits - 1), 2 ** bits - 1)
    if n % 2 == 0:
        n += 1
    return n


def random_odd_gap_length(bits):
  gap = 0
  n = random_odd_value2(bits)
  while miller_rabin(n, 40) == False:
    gap += 1
    n += 2
  return gap


def prime_distribution_stats(bits, number_of_samples):
  gap_list = []
  for i in range(number_of_samples):
    gap_list.append(random_odd_gap_length(bits))
  return sum(gap_list) / number_of_samples



















