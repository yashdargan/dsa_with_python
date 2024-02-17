
#recusive method
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

#iterative method
def iterative_fact(n):
    sum =1
    for i in range(1,n+1):
        sum = sum*i
    print(sum)
    return sum    
n = int(input("enter the number\n"))
#result = fact(n)
result = iterative_fact(n)
print(result)