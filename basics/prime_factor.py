import math
# naive solution


def prime_factor(n):
    if n <= 1:
        return
    sq = math.isqrt(n)
    for i in range(2, sq+1):
        while n % i == 0:
            print(i)
            n = n/i
    if n > 1:
        print(n)

# prime_factor(n)

# efficent solution


def prime_factor1(n: int):
    if n <= 1:
        return
    while (n % 2 == 0):
        print(2)
        n = n//2
    while (n % 3 == 0):
        print(3)
        n = n//3
    sq = math.isqrt(n)
    for i in range(5, sq+1, 6):
        while (n % i == 0):
            print(i)
            n = n//i
        while (n % (i+2) == 0):
            print(i+2)
            n = n//(i+2)
    if n > 3:
        print(n)


n = int(input("enter the number:\n"))
prime_factor1(n)
