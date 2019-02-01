"""
Given some number n, finds the largest integer palindrome made from the products of
two numbers less than or equal to n. Shown with n = 999.
Original problem found here:
https://projecteuler.net/problem=4
"""
def palfinder(pal, loops):
    """Given an integer palindrome, returns next lowest integer palindrome"""
    length = len(str(pal))
    pivot = 0
    index = 0
    if length % 2 == 0:
        while True:
            loops += 1
            pivot = int(length/2) - 1 - index
            pal = str(pal)
            if pal[pivot] != '0':
                pal = pal[:pivot] + str(int(pal[pivot])-1) + pal[pivot+1:]
                pal = pal[:len(pal)-pivot-1] + pal[pivot] + pal[len(pal)-pivot:]
                for i in range(index):
                    loops += 1
                    pal = pal[:pivot + i + 1] + '9' + pal[pivot + i + 2:]
                    pal = pal[:len(pal)-pivot-2-i] + '9' + pal[len(pal)-pivot-i-1:]
                return int(pal), loops
            else:
                index += 1
    else:
        while True:
            loops += 1
            pivot = int(length // 2) - index
            pal = str(pal)
            if pal[pivot] != '0':
                pal = pal[:pivot] + str(int(pal[pivot])-1) + pal[pivot+1:]
                pal = pal[:len(pal)-pivot-1] + pal[pivot] + pal[len(pal)-pivot:]
                for i in range(index):
                    loops += 1
                    pal = pal[:pivot + i + 1] + '9' + pal[pivot + i + 2:]
                    pal = pal[:len(pal)-pivot-2-i] + '9' + pal[len(pal)-pivot-i-1:]
                return int(pal), loops
            else:
                index += 1

def highpalfinder(hnum):
    """
    Finds largest integer palindrome that can be made as a product from two integers
    less than or equal to given integer.
    """
    loops = 0
    if hnum <= 45:
        for x in range(hnum**2, 0, -1):
            loops += 1
            if str(x) == str(x)[::-1]:
                for y in range(hnum, 0, -1):
                    loops += 1
                    if x % y == 0 and x // y <= hnum:
                        return x // y, int(x / (x//y)), x, loops
    for x in range(hnum**2, 0, -1):
        loops += 1
        if str(x) == str(x)[::-1]:
            highpal = x
            break
    while True:
        loops += 1
        for y in range(hnum, hnum - int(hnum/10) , -1):
            loops += 1
            if highpal % y == 0 and highpal // y <= hnum:
                return highpal // y, int(highpal / (highpal//y)), highpal, loops
        highpal, loops = palfinder(highpal, loops)

palfinder(2000002, 0)
f1, f2, pal, loops = highpalfinder(999)
print('Palindrome', str(pal) + ',', 'which is', f1, '*', str(f2) + ',', 'was found in', loops, 'loops.')