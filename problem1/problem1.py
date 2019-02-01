"""
Finds the sum of all numbers under 1000.
Original problem found here:
https://projecteuler.net/problem=1
"""
n = 1000
s = 0
for x in range(0, n, 3):
    if x % 5 == 0:
        s += x/2
    else:
        s += x
for x in range(0, n, 5):
    if x % 3 == 0:
        s += x/2
    else:
        s += x
print(int(s))