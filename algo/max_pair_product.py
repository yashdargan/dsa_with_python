n = int(input())
num = [ int(i) for i in input().split()]
num = [int(x) for x in num]
num.sort(reverse = True)
a = num[0]
b = num[1]
product = a*b
print(product)
