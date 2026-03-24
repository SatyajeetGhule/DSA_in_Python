# Linear Search
# Implement linear search to find index of 7 in [4, 2, 7, 1, 5]. How many comparisons?

def linearSearch(arr):
    n = len(arr)
    compar = 0
    for i in range(n):
        compar+=1
        if arr[i] == 7:
            return i, compar
        
    return -1, compar

def main():
    arr = list(map(int,input("Enter the list : ").split()))

    index, Comp = linearSearch(arr)
    print("Index Number is : ",index)
    print("Comparisons : ",Comp)

main()