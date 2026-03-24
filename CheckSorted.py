# Check if Sorted
# Given array [1, 2, 3, 4, 5], write a function to check if it’s sorted in ascending order. Test on [3, 1, 4, 1, 5].

def Check(arr):
    n = len(arr)

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True


def main():
    arr = list(map(int,input("Enter the list : ").split()))

    iRet = Check(arr)

    if iRet == True:
        print("List is Sorted.")
    else:
        print("List is Not Sorted")


main()
