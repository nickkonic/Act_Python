def Bubblesort(arr):
    for i in range (len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [5, 1, 4, 2]
Sortedarr = Bubblesort(arr)

print("Bubble Sort", Sortedarr)

def SelectingSort(A):
    for i in range(len(A)):
        minind = i
        for j in range(i+1, len(A)):
            if A[minind] > A[j]:
                minind = j
        A[i], A[minind] = A[minind], A[i]
    return A

arr = [8, 12, 5, 9, 2]
Sortedarr = SelectingSort(arr)

print("Selecting Sort", Sortedarr)

def InsertionSort(arr):
    for i in range (1, len(arr)):
        store = arr[i]
        j = i-1
        while j >=0 and store < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr [j+1] = store
    return arr

arr = [12, 6, 5, 14, 3]
Sortedarr = InsertionSort(arr)

print("Insertion Sort", Sortedarr)