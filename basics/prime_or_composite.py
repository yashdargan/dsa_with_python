import math
#naive approach

def check_for_prime(n):
    for i in range(2,n//2):
        if n % i == 0:
            return False
    return True

#most efficient way
def check_for_prime1(n):
    if n==2 or n==3:
        return True
    
    if n%2 ==0 or n%3==0:
        return False
    sq = math.isqrt(n)
    for i in range(5,sq+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True  

n = int(input("enter the number\n"))
result = check_for_prime1(n)

[print("prime number") if result == True else print("Composite")]