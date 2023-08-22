# testing package-making
# https://packaging.python.org/en/latest/tutorials/packaging-projects/

# binary search
def binarySearch(arr, target):
    n = len(arr)
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid-1
        elif arr[mid] < target:
            left = mid+1
    return -1
