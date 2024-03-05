
def Complixity_contrant(n):
    return (n*(n+1)/2)


def Complixity_linear(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


n = int(input("enter the nth number\n"))
click = input("Enter L for Liner & C for Const\n")
if click == 'L':
    print(Complixity_contrant(n))
if click == 'O':
    print(Complixity_linear(n))
