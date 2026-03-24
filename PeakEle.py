# Peak Element
# Find any peak element (greater than neighbors) in [1, 3, 20, 4, 1, 0]. A peak exists in every array.

def peakSearch(arr):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid-1] < arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] < arr[mid+1]:
            start = mid +1
        else:
            end = mid -1

    return mid


def main():
    arr = list(map(int,input("Enter the list : ").split()))

    print(peakSearch(arr))

main()