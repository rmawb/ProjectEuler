"""
Finds the sum of even valued terms in the Fibonacci sequence up to 4,000,000.
Original problem found here:
https://projecteuler.net/problem=2
"""
a = 1
b = 2
c = 0
s = 0
while c < 4000000:
	if b % 2 == 0:
		s += b
	c = a + b
	a = b
	b = c
print(s)