#  Binary Search (Sorted Array)
# Given sorted array [1, 3, 5, 7, 9], implement binary search for 5. Return index or -1 if not found.


def binarySearch(arr,key):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] < key:
            start = mid+1
        
        elif arr[mid] > key:
            end = mid-1
        else:
            return mid

    return -1


def main():
    arr = list(map(int,input("Enter the list : ").split()))
    target = int(input("Enter the Searching element : "))

    print(binarySearch(arr,target))

main()
