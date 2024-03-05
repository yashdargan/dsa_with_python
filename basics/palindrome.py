def palindrome(n):
    m = int(str(n)[::-1])
    if m == n:
        return True
    return False


def iterative_palindrome(n):
    sum = 0
    m = n
    while (n != 0):
        l = n % 10
        n = n//10
        sum = sum*10+l
    print(sum)
    if m == sum:
        return True
    return False


n = int(input("enter the number:\n"))
# result=palindrome(n)
result = iterative_palindrome(n)
[print('yes palindrome') if result == True else print("Not")]
