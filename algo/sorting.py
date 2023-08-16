n = int(input("enter the no. of element : "))
arr =[]
print("enter the numbers : ")
for i in range(n):
    element = input()
    arr.append(element)

print(arr)

#bubble sorting 
'''for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] >arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
'''
#selection sort 
'''
for i in range(n):
    min = i 
    for j in range(i+1,n):
        if arr[j]< arr[min]:
            min = j 
    arr[min],arr[i] = arr[i],arr[min]

'''
# insertion sort 
''' for i in range(1,n):
    key = arr[i]
    j = i-1
    while j>=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = key    
'''
#merge sort 
'''
def merge(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge(left)
        merge(right)

        i=j=k=0

        while i < len( left ) and j < len( right ):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else :
                arr[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            arr[k] = left [i]
            i+=1
            k+=1
        
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1

        
merge(arr)
'''
#quick sort 

def quick(arr,low,high):
    if low < high:
        pivot_part = partition(arr,low,high)
        quick(arr,low,pivot_part-1)
        quick(arr,pivot_part+1,high)



def partition(arr,low,high):
    i=low
    j=high-1
    pivot = arr[high]
    
    while i < j:
        while i < high and arr[i] < pivot:
            i+=1 
    
        while j > low and arr[j] >= pivot:
            j-=1 

        if i < j:
            arr[i],arr[j]= arr[j],arr[i]
    if arr[i] > pivot:        
        arr[i],arr[high] = arr[high],arr[i]

    return i

quick(arr,0,len(arr)-1)

print("after sorting\n",arr)
