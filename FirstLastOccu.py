#  Peak Element
#  Find any peak element (greater than neighbors) in [1, 3, 20, 4, 1, 0]. A peak exists in every array.


def searchFirstLastOcc(arr,key):
    start1 = 0
    end1 = len(arr)-1

    while start1 < end1:
        mid = start1 + (end1 - start1) // 2

        if arr[mid] == key:
            end1 = mid-1
        else:
            start1 = mid +1


    start2 = 0
    end2 = len(arr)-1

    while start2 < end2:
        mid = start1 + (end2 - start2) // 2

        if arr[mid] == key:
            start2 = mid
        else:
            end2 = mid-1

    return start1, end2

def main():
    arr = list(map(int,input("Enter the list : ").split()))

    target = int(input("Enter the finding element : "))

    index1, index2 = searchFirstLastOcc(arr,target)

    print("Element of ", target," First Occurance is : ",index1)
    print("Element of ", target," Last Occurance is : ",index2)

main()