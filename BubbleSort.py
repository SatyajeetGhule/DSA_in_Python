# Write a function to sort an array [64, 34, 25, 12, 22, 11, 90] in 
# ascending order using bubble sort. Explain the number of swaps needed.

def swapArr(arr):
    n = len(arr)
    count = 0
    for i in range(n):

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                count+=1
    return arr, count

def main():
    arr = list(map(int,input("Enter the list : ").split()))

    sortedArr, count = swapArr(arr)

    print("Sorted Arr : ",sortedArr)
    print("Count : ",count)

main()