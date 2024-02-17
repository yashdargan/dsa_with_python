#5! -> 120 have (1 zero in end)
#10! -> have (2 zero in end)
#100! -> have (24 zero in end)
#trailing zero are multiple of 5 like n =100 then, 100/5 -> 20(atleast zero)
#but 25 have two 5 in it, 100/25 =4 -> 20 +4 =24 
def trailing_zero(m):
    sum=0
    i=5
    while i<=m :
        sum+= m//i
        i*=5
    return sum    
        
        

m = (int(input("enter the number:\n")))
result=trailing_zero(m)
print(result)