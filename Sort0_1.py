# Sort 0s and 1s
# Sort array [0, 1, 0, 1, 1, 0] so all 0s come before 1s (Dutch National Flag, easy version). What’s the time complexity?


# Time Complexity : O(n)
def Sorting(arr):
    count_0 = 0
    count_1 = 0
    n = len(arr)

    for i in range(n):
        if arr[i] == 0:
            count_0 +=1
        else:
            count_1 +=1
                
    indx = 0
    for i in range(count_0):
        arr[indx] = 0
        indx+=1
    for j in range(count_1):
        arr[indx] = 1
        indx+=1

    return arr
    


def main():
    arr = list(map(int,input("Enter the list : ").split()))

    print(Sorting(arr))

main()