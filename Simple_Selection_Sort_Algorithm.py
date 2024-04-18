def descending_order(arr):
    n = len(arr)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        if max_index != i:
            arr[i], arr[max_index] = arr[max_index], arr[i]

def ascending_order(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


elements = [79, 45, 23, 67, 88, 12, 54, 93, 36, 28]
elements_1 = ['L', 'G', 'B', 'R', 'Y', 'C', 'K', 'M', 'P', 'A']
elements_d = ['C', 'H', 'O', 'A', 'U', 'W', 'B', 'D', 'E', 'F']


descending_order(elements)
ascending_order(elements_1)
descending_order(elements_d)

print("Sorted List (Descending Order):", elements)
print("Sorted List (Ascending Order):", elements_1)
print("Sorted List (Descending Order):", elements_d)

