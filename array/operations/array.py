def traverse(arr: list):
    print(arr)


def insertion(arr: list, num: int, pos: int):
    # insertion check
    if pos < 0 or pos > len(arr)-1:
        print('invalid postion')
        return

    else:
        arr.append(0)
        for i in range(len(arr)-1, pos, -1):
            arr[i] = arr[i-1]
        arr[pos] = num
        traverse(arr)


def deletion(arr: list, pos: int):
    if pos < 0 or pos > len(arr)-1:
        print("invalid postion")
        return
    else:
        for i in range(pos, len(arr)-1):
            arr[i] = arr[i+1]
        arr.pop(len(arr)-1)
        traverse(arr)


if __name__ == "__main__":
    n = int(input("enter the number\n"))
    arr = []
    for i in range(0, n):
        value = int(input(f"enter the value {i+1} "))
        arr.append(value)
    dis = int(input("want to do insertion -> 0 or deletion -> 1 "))
    if dis == 0:
        pos = int(input("enter the position "))
        num = int(input("enter the number "))

        insertion(arr, num, pos)
    elif dis == 1:
        pos = int(input("enter the position "))
        deletion(arr, pos)
