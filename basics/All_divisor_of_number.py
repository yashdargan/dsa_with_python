import math
#naive solution :problem -> it will iterate upto n
def divisor_naive(n):
    list = []
    for i in range(1, n + 1):
        if n%i == 0:
            list.append(i)
    return list         

def divisor_efficent(n):
    list=[]
    sq = math.isqrt(n)
    for i in range(1, sq+1):
        if n%i==0:
            list.append(i)
            if i!=(n//i):
                list.append(n//i)
    return sorted(list)


n = int(input("enter the number\n"))
print(divisor_efficent(n))
