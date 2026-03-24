# Find Minimum
# In sorted rotated array [4, 5, 6, 7, 0, 1, 2], find the minimum element’s index using O(log n) search.

def searchMinEle(arr):
    start = 0
    end = len(arr)-1

    while start < end:
        mid = start + (end - start) // 2

        if arr[mid] > arr[end]:
            start = mid +1
        else:
            end = mid

    return start


def main():
    arr = list(map(int,input("Enter the list : ").split()))

    print(searchMinEle(arr))

main()