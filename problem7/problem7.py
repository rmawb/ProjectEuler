"""
Finds the 10001th prime number
Original problem found here:
https://projecteuler.net/problem=6
"""
import numpy as np
import time

start = time.process_time()

primes = []
count = 0
num = 2
while count < 10001:
    flag = True
    for p in primes:
        if p > np.sqrt(num):
            break
        if num % p == 0:
            num += 1
            flag = False
            break
    if flag:
        primes.append(num)
        count += 1
        num += 1

print(primes[-1])
print(time.process_time() - start)