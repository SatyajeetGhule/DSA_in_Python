#  Waveform Sort
#  Rearrange [10, 5, 6, 3, 2, 20] into a wave form like [10, 5, 20, 3, 6, 2] (larger, smaller, larger pattern).


def WaveSort(arr):
    n = len(arr)

    for i in range(0, n-1, 2):
        if arr[i] < arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        
    return arr


def main():
    arr = list(map(int,input("Enter the list : ").split()))

    print(WaveSort(arr))

main()
