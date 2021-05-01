arr = [4, 8, 55, 66, 75, 421]
target = 55


def binary_search(arr, target, low, high):
    if high >= low:
        mid = (high+low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid-1)
        else:
            return binary_search(arr, target, mid+1, high)
    else:
        return -1


result = binary_search(arr, target, 0, len(arr)-1)

if result != -1:
    print("target at: ", str(result))
else:
    print("not in the list")
