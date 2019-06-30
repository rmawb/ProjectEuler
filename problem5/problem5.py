"""
Given some positive integer n, finds the largest integer which 
is evenly divisible by all positive integers less than and equal to n.
Original problem found here:
https://projecteuler.net/problem=5
"""
import time

startt = time.time()
startpt = time.process_time()

def factorize(n):
    """
    Given some n, returns dictionary of prime factors with the key being the factor and the
    value being the number of occurance.
    """
    tfactor = 2
    factors = {}
    i = 0
    while n >= tfactor:
        if n % tfactor == 0:
            while n % tfactor == 0:
                i += 1
                n /= tfactor
            factors[tfactor] = i
        i = 0
        tfactor += 1
    return factors

def ledi_finder(n):
    """
    Given some n, returns largest integer which is evenly divisible
    by all positive integers less than and equal to n.
    """
    p_factors = {}
    ledi = 1
    for i in range(n+1):
        pf = factorize(i)
        primes = pf.keys()
        for p in primes:
            if p in p_factors:
                if pf[p] > p_factors[p]:
                    p_factors[p] = pf[p]
            else:
                p_factors[p] = pf[p]
    for p in p_factors.keys():
        ledi *= p**p_factors[p]
    return ledi

print(ledi_finder(20))
print('wall time:', time.time() - startt)
print('process time:', time.process_time() - startpt)