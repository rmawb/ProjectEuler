"""
Calculates the largest prime factor of 600,851,475,143
Original problem found here:
https://projecteuler.net/problem=3
"""
n = 600851475143
lfactor = 0
tfactor = 2
while lfactor < n:
    while n % tfactor == 0:
        n /= tfactor
        lfactor = tfactor
    tfactor += 1
print(lfactor)