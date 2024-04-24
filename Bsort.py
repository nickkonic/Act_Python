def bubble_sort(numbers, order):
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if order == 'ASCENDING':
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    swapped = True
            elif order == 'DESCENDING':
                if numbers[j] < numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    swapped = True
        if not swapped:
            break
        print(f"Pass {i+1}: {numbers}")
    return numbers

n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)

sort_order = input("Enter sort order (ASCENDING or DESCENDING): ").upper()

if sort_order not in ['ASCENDING', 'DESCENDING']:
    print("Invalid sort order. Please enter ASCENDING or DESCENDING.")
else:
    sorted_numbers = bubble_sort(numbers, sort_order)
    print(f"Sorted List ({sort_order} Order): {sorted_numbers}")
