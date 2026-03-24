# Selection Sort Steps
# For array [5, 2, 8, 1, 9], manually show the first two passes of selection sort and the array state after them.

def selectionSort(arr):
    n = len(arr)

    for i in range(2):
        mini = i

        for j in range(i,n):
            if arr[j] < arr[mini]:
                mini = j
        
        arr[i], arr[mini] = arr[mini],arr[i]                

    return arr

def main():
    arr = list(map(int,input("Enter the list : ").split()))

    print("Sorted Arr : ",selectionSort(arr))

main()