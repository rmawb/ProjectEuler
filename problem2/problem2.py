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