import numpy as np
import time

start = time.process_time()

counter = 0
num = 1

def is_prime(n):
    for i in range(2, int(np.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

while counter < 10001:
    num += 1
    if is_prime(num):
        counter += 1

print(num)
print(time.process_time() - start)