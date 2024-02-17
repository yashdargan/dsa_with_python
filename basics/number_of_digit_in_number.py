import math

#Recursive solution
def countDigit(n):
    if n==0:
        return 0
    return 1 + countDigit(n//10)

# using log
def countDigit1(n):
    return math.floor(math.log10(n)+1)

n = int(input("Number: \n"))
print(countDigit1(n))
#iterative solution#
''' 
count = 0
while n != 0:
    n=n//10
    count += 1
print("number of digits are ",count)  
'''
