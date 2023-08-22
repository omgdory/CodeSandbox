import time

# global vars
score = 0
test = [77, 100, 20, 2, 1, 1, 8, 80, 9999, 123]

# quicksort
# https://www.geeksforgeeks.org/python-program-for-quicksort/
def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # put pivot in proper spot
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i+1

def quickSortTrue(arr, low, high):
    if low < high:
        pivot_ind = partition(arr, low, high)
        quickSortTrue(arr, low, pivot_ind-1)
        quickSortTrue(arr, pivot_ind+1, high)

def quickSort(arr):
    quickSortTrue(arr, 0, len(arr)-1)

def main() -> None:
    print(test)
    quickSort(test)
    print(test)
    return

if __name__ == "__main__":
    main()
