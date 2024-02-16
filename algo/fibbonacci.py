#naive solution#
"""
def fib(n):
    if n<=1:
        return n 
    else:
        return fib(n-1)+fib(n-2)

n = int(input())
ans=fib(n)
print(ans)
"""

def fib(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

n = int(input())
ans = fib(n)
print(ans)
