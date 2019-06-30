"""
Finds the difference between the sum of the squares of the natural numbers
up to n and the square of the sum of the same natural numbers.
Original problem found here:
https://projecteuler.net/problem=6
"""

def sqos(n):
    ans = 0
    for i in range(n+1):
        ans += i
    return ans**2

def sosq(n):
    ans = 0
    for i in range(n+1):
        ans += i**2
    return ans

n = 100
print(sqos(n) - sosq(n))