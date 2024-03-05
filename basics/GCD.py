# naive solution :problem -> if they both are prime number
# it will iterate upto 1
def gcd_naive(a, b):
    res = min(a, b)
    while (res > 0):
        if a % res == 0 and b % res == 0:
            break
        res -= 1
    return res
# using euclidean alogrithm :problem -> iterative subraction performance


def gcd_euclidean(a, b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a


def gcd_optimize(a, b):
    if b == 0:
        return a
    else:
        return gcd_optimize(b, a % b)


a, b = map(int, input("enter two number\n").split())
print(gcd_optimize(a, b))
