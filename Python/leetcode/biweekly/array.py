arr = input()

def check(arr):
    plus = []
    minus = []
    for index, item in enumerate(arr):
        if index != 0 and index != len(arr)-1:
            if item > arr[index-1] and item > arr[index+1]:
                minus.append(index)
            elif item < arr[index-1] and item < arr[index+1]:
                plus.append(index)
    if not minus and not plus:
        print(arr)
    else:
        if minus:
            for m in minus:
                arr[m] = arr[m]-1
        if plus:
            for p in plus:
                arr[p] = arr[p]+1
        check(arr)

check(arr)
