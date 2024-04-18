def simple_selection_sort(arr, order):
    n = len(arr)
    steps = []  # To store steps for display
    for i in range(n - 1):
        if order == 1:  # Ascending Order
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        elif order == 2:  # Descending Order
            max_index = i
            for j in range(i + 1, n):
                if arr[j] > arr[max_index]:
                    max_index = j
            arr[i], arr[max_index] = arr[max_index], arr[i]
        steps.append(arr[:])  # Append a copy of the current list at each step

    return steps

# Input
print("Simple Selection Sort Algorithm")
data_type = int(input("Type of Data [1] Numbers [2] Alphabets: "))
n = int(input("How many items to sort? : "))

if data_type == 1:  # Numeric Data
    data = []
    for i in range(n):
        num = int(input(f"Input Number {i + 1}: "))
        data.append(num)
elif data_type == 2:  # Alphabetic Data
    data = []
    for i in range(n):
        char = input(f"Input Alphabet {i + 1}: ")
        data.append(char)
else:
    print("Invalid input for data type.")

order = int(input("Order [1] Ascending [2] Descending: "))

# Sorting using Simple Selection Sort and getting steps
steps = simple_selection_sort(data, order)

# Displaying the input elements and sorting steps
print("\nInput Elements:")
print(data)
print("\nSorting Steps:")
for step_no, step in enumerate(steps):
    print(f"[{step_no}] {step}")
