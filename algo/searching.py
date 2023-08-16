n = int(input("enter no of element : "))
print("enter the element : ")
#for linear and binary seraching array 
'''
arr = []
for i in range(n):
    element = int(input())
    arr.append(element)

print(arr)
'''
#for hashing table formation
'''
hash_table ={}
def insert(key,value):
    hash_table[key] = value

print("key and value :")
for i in range(n):
    key,value = input().split(" ")
    insert(key,value)

print(hash_table)


target = input("enter the value u want to find : ")
'''
target = int(input("enter the value u want to find : "))
#linear search
'''
def linear(arr,target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1    

s  = linear(arr,target)
'''
#binary search
'''
def binary(arr,target):
    low,high  = 0, len(arr)-1
    while low <= high:
        mid  = low + (high - low)//2 
        if arr[mid] == target:
            return mid
        elif mid < target:
            low  = mid + 1
        else:
            high  = mid - 1
    return -1

s = binary(arr,target)
'''
#hashing search
'''
def search(target):
    if target in hash_table:
        return hash_table[target]
    else: 
        return -1

s = search(target)
'''
print("the index no. is ",s)

