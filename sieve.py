import math


def sieve_of_eratosthenes_v1(N):
  P = [True] * (N + 1)
  for i in range(2, N + 1):
    if P[i]:
      m = i + i
      while m <= N:
        P[m] = False
        m += i
  return [i for i in range(2, N + 1) if P[i]]



def sieve_of_eratosthenes_v2(N):
  P = [True] * (N + 1)
  for i in range(2, int(math.sqrt(N))+1):
    if P[i]:
      m = i + i
      while m <= N:
        P[m] = False
        m += i
  return [i for i in range(2, N + 1) if P[i]]




def sieve_of_eratosthenes_v3(N):
  P = [True] * (N + 1)
  for i in range(2, int(math.sqrt(N))+1):
    if P[i]:
      m = i * i
      while m <= N:
        P[m] = False
        m += i
  return [i for i in range(2, N + 1) if P[i]]




def sieve_of_eratosthenes_v4(N):
  P = [True] * (N + 1)
  for i in range(2, int(math.sqrt(N))+1):
    if P[i]:
      k = int(N/i)
      P[2 * i::i] = [False] * (k - 1)
  return [i for i in range(2, N + 1) if P[i]]




def sieve_of_eratosthenes_v5(N):
  P = [True] * (N + 1)
  for i in range(2, int(math.sqrt(N))+1):
    if P[i]:
      k = int((N - i * i) / i)
      P[i * i::i] = [False] * (k + 1)
  return [i for i in range(2, N + 1) if P[i]]








N = 100
print(sieve_of_eratosthenes_v1(N))
print(sieve_of_eratosthenes_v2(N))
print(sieve_of_eratosthenes_v3(N))
print(sieve_of_eratosthenes_v4(N))
print(sieve_of_eratosthenes_v5(N))
