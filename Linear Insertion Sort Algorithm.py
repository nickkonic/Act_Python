def linear_insertion_sort(arr, order):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((order == "ASCENDING" and arr[j] > key) or (order == "DESCENDING" and arr[j] < key)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Pass {i}: {arr}")

n = int(input("Enter the number of elements to be sorted: "))
arr = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)

sort_order = input("Enter sort order (ASCENDING or DESCENDING): ").upper()

linear_insertion_sort(arr, sort_order)
